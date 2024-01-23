import os
_mod = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys
sys.path.append(_mod)
from module.local.textgen import TextGen
llm = TextGen(
    model_url="http://127.0.0.1:5552",
    temperature=0.01,
    top_p=0.9,
    seed=10,
    max_tokens=2000,
    stop=[],
    streaming=True,
)

model = llm

from dotenv import load_dotenv
load_dotenv()


from langchain_community.tools.tavily_search import TavilySearchResults
tools = [TavilySearchResults(max_results=1)]

# from langchain_core.pydantic_v1 import BaseModel, Field
# class SearchTool(BaseModel):
#     """Look up things online, optionally returning directly"""
#     query: str = Field(description="query to look up online")
#     return_direct: bool  = Field(
#         description="Whether or the result of this should be returned directly to the user without you seeing what it is", 
#         default = False
#     )
# from langchain_community.tools.tavily_search import TavilySearchResults
# search_tool = TavilySearchResults(max_results=1, args_schema=SearchTool)
# tools = [search_tool]

from langgraph.prebuilt import ToolExecutor
tool_executor = ToolExecutor(tools)
# from langchain_openai import ChatOpenAI
# model = ChatOpenAI(temperature=0, streaming=True)



from langchain.tools.render import format_tool_to_openai_function
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.utils.function_calling import convert_pydantic_to_openai_function
class Response(BaseModel):
    """Final response to the user"""
    temperature: float = Field(description="温度")
    other_notes: str = Field(description="关于天气的其他信息")
functions = [format_tool_to_openai_function(t) for t in tools]
functions.append(convert_pydantic_to_openai_function(Response))
print(functions)
# exit()
model = model.bind_functions(functions)



# from langgraph.prebuilt import chat_agent_executor
# app = chat_agent_executor.create_function_calling_executor(model, tools)



# from langchain.tools.render import format_tool_to_openai_function
# functions = [format_tool_to_openai_function(t) for t in tools]
# model = model.bind_functions(functions)

from typing import TypedDict, Annotated, Sequence
import operator
from langchain_core.messages import BaseMessage
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]

from langgraph.prebuilt import ToolInvocation
import json
from langchain_core.messages import FunctionMessage
def should_continue(state):
    messages = state['messages']
    last_message = messages[-1]
    if "function_call" not in last_message.additional_kwargs:
        return "end"
    elif last_message.additional_kwargs["function_call"]["name"] == "Response":
        return "end"
    else:
        # arguments = json.loads(last_message.additional_kwargs["function_call"]["arguments"])
        # if arguments.get("return_direct", False):
        #     return "final"
        # else:
        #     return "continue"
        return "continue"

def call_model(state):
    messages = state['messages'][-5:]
    response = model.invoke(messages)
    return {"messages": [response]}

def call_tool(state):
    messages = state['messages']
    last_message = messages[-1]
    action = ToolInvocation(
        tool=last_message.additional_kwargs["function_call"]["name"],
        tool_input=json.loads(last_message.additional_kwargs["function_call"]["arguments"]),
    )
    response = input(f"[y/n] continue with: {action}?")
    if response == "n":
        raise ValueError
    response = tool_executor.invoke(action)
    function_message = FunctionMessage(content=str(response), name=action.tool)
    return {"messages": [function_message]}

from langchain_core.messages import AIMessage
import json
def first_model(state):
    human_input = state['messages'][-1].content
    return {
        "messages": [
            AIMessage(
                content="", 
                additional_kwargs={
                    "function_call": {
                        "name": "tavily_search_results_json", 
                        "arguments": json.dumps({"query": human_input})
                        }
                    }
                )
            ]
    }


from langgraph.graph import StateGraph, END
workflow = StateGraph(AgentState)
workflow.add_node("agent", call_model)
workflow.add_node("action", call_tool)
# workflow.add_node("final", call_tool)
# workflow.add_node("first_agent", first_model)
# workflow.set_entry_point("first_agent")
workflow.set_entry_point("agent")
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "action",
        # "final": "final",
        "end": END
    }
)
workflow.add_edge('action', 'agent')
# workflow.add_edge('first_agent', 'action')
# workflow.add_edge('final', END)

app = workflow.compile()


from langchain_core.messages import HumanMessage
inputs = {"messages": [HumanMessage(content="明天长沙的天气怎么样")]}
# print(app.invoke(inputs))
for output in app.stream(inputs):
    for key, value in output.items():
        print(f"Output from node '{key}':")
        print("---")
        print(value)
    print("\n---\n")


# inputs = {"messages": [HumanMessage(content="what is the weather in sf? return this result directly by setting return_direct = True")]}
# for output in app.stream(inputs):
#     for key, value in output.items():
#         print(f"Output from node '{key}':")
#         print("---")
#         print(value)
#     print("\n---\n")

