from dotenv import load_dotenv
load_dotenv()

from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
tools = [TavilySearchResults(max_results=1)]
prompt = hub.pull("hwchase17/openai-functions-agent")
llm = ChatOpenAI(model="gpt-3.5-turbo-1106", streaming=True)
agent_runnable = create_openai_functions_agent(llm, tools, prompt)



# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# prompt = ChatPromptTemplate.from_messages([
#     ("human", "Respond to the user question: {question}. Answer in this language: {language}"),
#     MessagesPlaceholder(variable_name="agent_scratchpad")
# ])
# agent_runnable = create_openai_functions_agent(llm, tools, prompt)
# from typing import TypedDict
# class InputSchema(TypedDict):
#     question: str
#     language: str
# app = create_agent_executor(agent_runnable, tools, input_schema=InputSchema)
# inputs = {"question": "what is the weather in sf", "language": "italian"}
# for s in app.stream(inputs):
#     print(list(s.values())[0])
#     print("----")



# from langgraph.prebuilt import create_agent_executor
# app = create_agent_executor(agent_runnable, tools)



from typing import TypedDict, Annotated, Union
from langchain_core.agents import AgentAction, AgentFinish
from langchain_core.messages import BaseMessage
import operator
class AgentState(TypedDict):
    input: str
    chat_history: list[BaseMessage]
    agent_outcome: Union[AgentAction, AgentFinish, None]
    intermediate_steps: Annotated[list[tuple[AgentAction, str]], operator.add]

from langchain_core.agents import AgentFinish
from langgraph.prebuilt.tool_executor import ToolExecutor
tool_executor = ToolExecutor(tools)

from langgraph.graph import END, StateGraph
workflow = StateGraph(AgentState)

def run_agent(data):
    # agent_outcome = agent_runnable.invoke(data)
    inputs = data.copy()
    if len(inputs['intermediate_steps']) > 5:
        inputs['intermediate_steps'] = inputs['intermediate_steps'][-5:]
    agent_outcome = agent_runnable.invoke(inputs)
    return {"agent_outcome": agent_outcome}

def execute_tools(data):
    agent_action = data['agent_outcome']
    response = input(f"[y/n] continue with: {agent_action}?")
    if response == "n":
        raise ValueError
    output = tool_executor.invoke(agent_action)
    return {"intermediate_steps": [(agent_action, str(output))]}

def should_continue(data):
    if isinstance(data['agent_outcome'], AgentFinish):
        return "end"
    else:
        return "continue"

from langchain_core.agents import AgentActionMessageLog
def first_agent(inputs):
    action = AgentActionMessageLog(
      tool="tavily_search_results_json",
      tool_input=inputs["input"],
      log="",
      message_log=[]
    )
    return {"agent_outcome": action}

workflow.add_node("agent", run_agent)
workflow.add_node("action", execute_tools)
# workflow.add_node("first_agent", first_agent)
# workflow.set_entry_point("first_agent")
workflow.set_entry_point("agent")
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "action",
        "end": END
    }
)
workflow.add_edge('action', 'agent')
# workflow.add_edge('first_agent', 'action')
app = workflow.compile()



inputs = {"input": "明天长沙的天气怎么样", "chat_history": []}
# print(app.invoke(inputs))
for s in app.stream(inputs):
    print(list(s.values())[0])
    print("----")

