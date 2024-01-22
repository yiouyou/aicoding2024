from dotenv import load_dotenv
load_dotenv()


from typing import Any, Callable, List, Optional, TypedDict, Union
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import Runnable
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph
import uuid

def create_worker_agent(
    graph_builder: StateGraph,
    name: str,
    llm: ChatOpenAI,
    tools: list,
    system_prompt: str,
    prelude: Optional[Union[Runnable, Callable]] = None,  # Optional required steps
) -> str:
    """Create a function-calling agent and add it to the graph."""
    system_prompt += "\nWork autonomously according to your specialty, using the tools available to you."
    " Do not ask for clarification."
    " Your other team members (and other teams) will collaborate with you with their own specialties."
    " You are chosen for a reason! You are one of the following team members: {team_members}."
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                system_prompt,
            ),
            MessagesPlaceholder(variable_name="messages"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )
    agent = create_openai_functions_agent(llm, tools, prompt)
    executor = AgentExecutor(agent=agent, tools=tools)
    chain = executor | (
        lambda x: {"messages": [HumanMessage(content=x["output"], name=name)]}
    )
    if prelude is not None:
        chain = prelude | chain
    graph_builder.add_node(name, chain)
    return name

def create_team_supervisor(
    graph_builder: StateGraph, llm: ChatOpenAI, system_prompt: str
) -> str:
    """An LLM-based router."""
    supervisor_id = uuid.uuid4().hex[:4]
    supervisor_name = f"supervisor - {supervisor_id}"
    members = list(graph_builder.nodes)
    options = ["FINISH"] + members
    function_def = {
        "name": "route",
        "description": "Select the next role.",
        "parameters": {
            "title": "routeSchema",
            "type": "object",
            "properties": {
                "next": {
                    "title": "Next",
                    "anyOf": [
                        {"enum": options},
                    ],
                },
            },
            "required": ["next"],
        },
    }
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
            (
                "system",
                "Given the conversation above, who should act next?"
                " Or should we FINISH? Select one of: {options}",
            ),
        ]
    ).partial(options=str(options), team_members=", ".join(members))
    chain = (
        prompt
        | llm.bind_functions(functions=[function_def], function_call="route")
        | JsonOutputFunctionsParser()
    )
    graph_builder.add_node(supervisor_name, chain)
    conditional_map = {k: k for k in members}
    conditional_map["FINISH"] = END
    for member in members:
        graph_builder.add_edge(member, supervisor_name)
    graph_builder.add_conditional_edges(
        supervisor_name, lambda x: x["next"], conditional_map
    )
    return supervisor_name



from typing import Annotated, List, Tuple, Union
import matplotlib.pyplot as plt
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
from langsmith import trace
tavily_tool = TavilySearchResults(max_results=5)
@tool
def scrape_webpages(urls: List[str]) -> str:
    """Use requests and bs4 to scrape the provided web pages for detailed information."""
    loader = WebBaseLoader(urls)
    docs = loader.load()
    return "\n\n".join(
        [
            f'<Document name="{doc.metadata["title"]}">\n{doc.page_content}\n</Document>'
            for doc in docs
        ]
    )



import functools
import operator
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_openai.chat_models import ChatOpenAI
# Research team graph state
class State(TypedDict):
    # A message is added after each team member finishes
    messages: Annotated[List[BaseMessage], operator.add]
    # The team members are tracked so they are aware of
    # the others' skill-sets
    team_members: List[str]
    # Used to route work. The supervisor calls a function
    # that will update this every time it makes a decision
    next: str

research_graph = StateGraph(State)
# llm = ChatOpenAI(model="gpt-4-1106-preview")
llm = ChatOpenAI(model="gpt-3.5-turbo-1106")
create_worker_agent(
    research_graph,
    "Search",
    llm,
    [tavily_tool],
    "You are a research assistant who can search for up-to-date info"
    " using the tavily search engine.",
)
create_worker_agent(
    research_graph,
    "Web Scraper",
    llm,
    [scrape_webpages],
    "You are a research assistant who can scrape"
    " specified urls for more detailed information using"
    " the scrape_webpages function.",
)
supervisor_node = create_team_supervisor(
    research_graph,
    llm,
    "You are a supervisor tasked with managing a conversation between the"
    " following workers:  {team_members}. Given the following user request,"
    " respond with the worker to act next. Each worker will perform a"
    " task and respond with their results and status. When finished,"
    " respond with FINISH.",
)
research_graph.set_entry_point(supervisor_node)
def enter_chain(message: str, members: Optional[list] = None):
    results = {
        "messages": [HumanMessage(content=message)],
    }
    if members:
        results["team_members"] = "\n".join(sorted(members))
    return results
def return_final_response(state):
    return {"final_response": state["messages"][-1]}
research_chain = (
    functools.partial(enter_chain, members=research_graph.nodes)
    | research_graph.compile()
    | return_final_response
)



from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Dict
from langchain_experimental.utilities import PythonREPL
from typing_extensions import TypedDict
_TEMP_DIRECTORY = TemporaryDirectory()
WORKING_DIRECTORY = Path(_TEMP_DIRECTORY.name)
@tool
def create_outline(
    points: Annotated[List[str], "List of main points or sections."],
    file_name: Annotated[str, "File path to save the outline."],
) -> Annotated[str, "Path of the saved outline file."]:
    """Create and save an outline."""
    with (WORKING_DIRECTORY / file_name).open("w") as file:
        for i, point in enumerate(points):
            file.write(f"{i + 1}. {point}\n")
    return f"Outline saved to {file_name}"
@tool
def read_document(
    file_name: Annotated[str, "File path to save the document."],
    start: Annotated[Optional[int], "The start line. Default is 0"] = None,
    end: Annotated[Optional[int], "The end line. Default is None"] = None,
) -> str:
    """Read the specified document."""
    with (WORKING_DIRECTORY / file_name).open("r") as file:
        lines = file.readlines()
    if start is not None:
        start = 0
    return "\n".join(lines[start:end])
@tool
def write_document(
    content: Annotated[str, "Text content to be written into the document."],
    file_name: Annotated[str, "File path to save the document."],
) -> Annotated[str, "Path of the saved document file."]:
    """Create and save a text document."""
    with (WORKING_DIRECTORY / file_name).open("w") as file:
        file.write(content)
    return f"Document saved to {file_name}"
@tool
def edit_document(
    file_name: Annotated[str, "Path of the document to be edited."],
    inserts: Annotated[
        Dict[int, str],
        "Dictionary where key is the line number (1-indexed) and value is the text to be inserted at that line.",
    ],
) -> Annotated[str, "Path of the edited document file."]:
    """Edit a document by inserting text at specific line numbers."""
    # Read the contents of the file
    with (WORKING_DIRECTORY / file_name).open("r") as file:
        lines = file.readlines()
    # Adjust the line numbers for 0-indexing and sort
    sorted_inserts = sorted(inserts.items())
    # Perform the insertions
    for line_number, text in sorted_inserts:
        if 1 <= line_number <= len(lines) + 1:
            # Insert the text at the specified line number
            lines.insert(line_number - 1, text + "\n")
        else:
            return f"Error: Line number {line_number} is out of range."
    # Write the modified content back to the file
    with (WORKING_DIRECTORY / file_name).open("w") as file:
        file.writelines(lines)
    return f"Document edited and saved to {file_name}"
repl = PythonREPL()
@tool
def python_repl(
    code: Annotated[str, "The python code to execute to generate your chart."]
):
    """Use this to execute python code. If you want to see the output of a value,
    you should print it out with `print(...)`. This is visible to the user."""
    try:
        result = repl.run(code)
    except BaseException as e:
        return f"Failed to execute. Error: {repr(e)}"
    return f"Succesfully executed:\n```python\n{code}\n```\nStdout: {result}"



import operator
from pathlib import Path
# Document writing team graph state
class AuthoringState(TypedDict):
    # This tracks the team's conversation internally
    messages: Annotated[List[BaseMessage], operator.add]
    # This provides each worker with context on the others' skill sets
    team_members: str
    # This is how the supervisor tells langgraph who to work next
    next: str
    # This tracks the shared directory state
    current_files: str
# This will be run before each worker agent begins work
# It makes it so they are more aware of the current state
# of the working directory.
def prelude(state):
    written_files = []
    if not WORKING_DIRECTORY.exists():
        WORKING_DIRECTORY.mkdir()
    try:
        written_files = [
            f.relative_to(WORKING_DIRECTORY) for f in WORKING_DIRECTORY.rglob("*")
        ]
    except:
        pass
    if not written_files:
        return {**state, "current_files": "No files written."}
    return {
        **state,
        "current_files": "\nBelow are files your team has written to the directory:\n"
        + "\n".join([f" - {f}" for f in written_files]),
    }
# Create the graph here:
authoring_graph = StateGraph(AuthoringState)
llm = ChatOpenAI(model="gpt-4-1106-preview")
create_worker_agent(
    authoring_graph,
    "Author Docs",
    llm,
    [write_document, edit_document, read_document],
    "You are an expert writing a research document.\n"
    # The {current_files} value is populated automatically by the graph state
    "Below are files currently in your directory:\n{current_files}",
    prelude=prelude,
)
create_worker_agent(
    authoring_graph,
    "Outline + Notetaker",
    llm,
    [create_outline, read_document],
    "You are an expert senior researcher tasked with writing a paper outline and"
    " taking notes to craft a perfect paper.{current_files}",
    prelude=prelude,
)
create_worker_agent(
    authoring_graph,
    "Generate Charts",
    llm,
    [read_document, python_repl],
    "You are a data viz expert tasked with generating charts for a research project."
    "{current_files}",
)
supervisor_node = create_team_supervisor(
    authoring_graph,
    llm,
    "You are a supervisor tasked with managing a conversation between the"
    " following workers:  {team_members}. Given the following user request,"
    " respond with the worker to act next. Each worker will perform a"
    " task and respond with their results and status. When finished,"
    " respond with FINISH.",
)
authoring_graph.set_entry_point(supervisor_node)
# We re-use the enter/exit functions to wrap the graph
authoring_chain = (
    functools.partial(enter_chain, members=authoring_graph.nodes)
    | authoring_graph.compile()
    | return_final_response
)



from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_openai.chat_models import ChatOpenAI
# Research team graph
class State(TypedDict):
    messages: Annotated[List[BaseMessage], operator.add]
    next: str
def get_last_message(state: State) -> str:
    return state["messages"][-1].content
def join_graph(response: dict):
    return {"messages": [response["final_response"]]}
super_graph = StateGraph(State)
super_graph.add_node("Research team", get_last_message | research_chain | join_graph)
super_graph.add_node(
    "Paper writing team", get_last_message | authoring_chain | join_graph
)
llm = ChatOpenAI(model="gpt-4-1106-preview")
supervisor_node = create_team_supervisor(
    super_graph,
    llm,
    "You are a supervisor tasked with managing a conversation between the"
    " following teams: {team_members}. Given the following user request,"
    " respond with the worker to act next. Each worker will perform a"
    " task and respond with their results and status. When finished,"
    " respond with FINISH.",
)
super_graph.set_entry_point(supervisor_node)
super_graph = enter_chain | super_graph.compile()



results = super_graph.invoke(
    "Write a brief research report on the North American sturgeon. Include a chart.",
    {"recursion_limit": 150},
)
print(results["messages"][-1])

