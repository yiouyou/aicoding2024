from dotenv import load_dotenv
load_dotenv()


from typing import Annotated, List, Tuple, Union
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
from langchain_experimental.tools import PythonREPLTool
tavily_tool = TavilySearchResults(max_results=5)

python_repl_tool = PythonREPLTool()


from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph
def create_worker_node(
    workflow: StateGraph, name: str, llm: ChatOpenAI, tools: list, system_prompt: str
):
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
    agent = create_openai_tools_agent(llm, tools, prompt)
    executor = AgentExecutor(agent=agent, tools=tools)
    chain = executor | (
        lambda x: {"messages": [HumanMessage(content=x["output"], name=name)]}
    )
    workflow.add_node(name, chain)


import operator
from typing import Annotated, Any, Dict, List, Optional, Sequence, TypedDict
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    next: str
workflow = StateGraph(AgentState)
# llm = ChatOpenAI(model="gpt-4-1106-preview")
llm = ChatOpenAI(model="gpt-3.5-turbo-1106")

create_worker_node(
    workflow, "Researcher", llm, [tavily_tool], "You are a web researcher."
)
create_worker_node(
    workflow,
    "Coder",
    llm,
    [python_repl_tool],
    "You may generate safe python code to analyze data "
    "and generate charts using matplotlib.",
)


from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
members = ["Researcher", "Coder"]
system_prompt = (
    "You are a supervisor tasked with managing a conversation between the"
    " following workers:  {members}. Given the following user request,"
    " respond with the worker to act next. Each worker will perform a"
    " task and respond with their results and status. When finished,"
    " respond with FINISH."
)
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
            }
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
).partial(options=str(options), members=", ".join(members))
supervisor_chain = (
    prompt
    | llm.bind_functions(functions=[function_def], function_call="route")
    | JsonOutputFunctionsParser()
)

workflow.add_node("supervisor", supervisor_chain)

for member in members:
    workflow.add_edge(member, "supervisor")
conditional_map = {k: k for k in members}
conditional_map["FINISH"] = END
workflow.add_conditional_edges("supervisor", lambda x: x["next"], conditional_map)
workflow.set_entry_point("supervisor")

graph = workflow.compile()

results = graph.invoke(
    {
        "messages": [
            HumanMessage(content="Code hello world and print it to the terminal")
        ]
    }
)
print(results["messages"][-1].pretty_print())


results = graph.invoke(
    {
        "messages": [
            HumanMessage(content="Write a brief research report on pikas.")
        ]
    },
    {"recursion_limit": 100},
)
print(results["messages"][-1].pretty_print())

