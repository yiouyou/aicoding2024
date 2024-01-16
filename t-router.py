from semantic_router import Route
from getpass import getpass
from semantic_router import RouteLayer
from semantic_router.encoders import OpenAIEncoder
from semantic_router.utils.function_call import get_schema
from datetime import datetime
from zoneinfo import ZoneInfo


def get_time(timezone: str) -> str:
    """Finds the current time in a specific timezone.
    :param timezone: The timezone to find the current time in, should be a valid timezone from the IANA Time Zone Database like "America/New_York" or "Europe/London". Do NOT put the place name itself like "rome", or "new york", you must provide the IANA format.
    :type timezone: str
    :return: The current time in the specified timezone."""
    now = datetime.now(ZoneInfo(timezone))
    return now.strftime("%H:%M")
schema = get_schema(get_time)
print(schema)
# print(get_time("Asia/Tokyo"))


politics = Route(
    name="politics",
    utterances=[
        "isn't politics the best thing ever",
        "why don't you tell me about your political opinions",
        "don't you just love the president" "don't you just hate the president",
        "they're going to destroy this country!",
        "they will save the country!",
    ],
)
chitchat = Route(
    name="chitchat",
    utterances=[
        "how's the weather today?",
        "how are things going?",
        "lovely weather today",
        "the weather is horrendous",
        "let's go to the chippy",
    ],
)
time_route = Route(
    name="get_time",
    utterances=[
        "what is the time in new york city?",
        "what is the time in london?",
        "I live in Rome, what time is it?",
    ],
    function_schema=schema,
)

routes = [politics, chitchat, time_route]



# from dotenv import load_dotenv
# load_dotenv()
# encoder = OpenAIEncoder()
# rl = RouteLayer(encoder=encoder, routes=routes)
# out = rl("how's the weather today?")
# print(type(out))
# print(out)
# print(out.name)
# print(out.function_call)
# print(out.similarity_score)
# print(out.trigger)



from semantic_router.encoders import HuggingFaceEncoder
encoder = HuggingFaceEncoder()
from llama_cpp import Llama
from semantic_router.llms import LlamaCppLLM
enable_gpu = False  # offload LLM layers to the GPU (must fit in memory)
_llm = Llama(
    model_path="./mistral-7b-instruct-v0.2.Q4_K_M.gguf",
    n_gpu_layers=-1 if enable_gpu else 0,
    n_ctx=2048,
    verbose=False,
)
llm = LlamaCppLLM(name="Mistral-7B-v0.2-Instruct", llm=_llm, max_tokens=None)
rl = RouteLayer(encoder=encoder, routes=routes, llm=llm)



out = rl("what is the time in Beijing?")
print(out)
print(type(out.function_call))
print(out.function_call)
print(out.function_call['timezone'])
print(get_time(**out.function_call))

