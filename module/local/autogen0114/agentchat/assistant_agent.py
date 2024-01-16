from .conversable_agent import ConversableAgent
from typing import Callable, Dict, Optional, Union


class AssistantAgent(ConversableAgent):
    """(In preview) Assistant agent, designed to solve a task with LLM.

    AssistantAgent is a subclass of ConversableAgent configured with a default system message.
    The default system message is designed to solve a task with LLM,
    including suggesting python code blocks and debugging.
    `human_input_mode` is default to "NEVER"
    and `code_execution_config` is default to False.
    This agent doesn't execute code by default, and expects the user to execute the code.
    """

#     DEFAULT_SYSTEM_MESSAGE = """You are a helpful AI assistant.
# Solve tasks using your coding and language skills.
# In the following cases, suggest python code (in a python coding block) or shell script (in a sh coding block) for the user to execute.
#     1. When you need to collect info, use the code to output the info you need, for example, browse or search the web, download/read a file, print the content of a webpage or a file, get the current date/time, check the operating system. After sufficient info is printed and the task is ready to be solved based on your language skill, you can solve the task by yourself.
#     2. When you need to perform some task with code, use the code to perform the task and output the result. Finish the task smartly.
# Solve the task step by step if you need to. If a plan is not provided, explain your plan first. Be clear which step uses code, and which step uses your language skill.
# When using code, you must indicate the script type in the code block. The user cannot provide any other feedback or perform any other action beyond executing the code you suggest. The user can't modify your code. So do not suggest incomplete code which requires users to modify. Don't use a code block if it's not intended to be executed by the user.
# If you want the user to save the code in a file before executing it, put # filename: <filename> inside the code block as the first line. Don't include multiple code blocks in one response. Do not ask users to copy and paste the result. Instead, use 'print' function for the output when relevant. Check the execution result returned by the user.
# If the result indicates there is an error, fix the error and output the code again. Suggest the full code instead of partial code or code changes. If the error can't be fixed or if the task is not solved even after the code is executed successfully, analyze the problem, revisit your assumption, collect additional info you need, and think of a different approach to try.
# When you find an answer, verify the answer carefully. Include verifiable evidence in your response if possible.
# Reply "TERMINATE" in the end when everything is done.
#     """

    DEFAULT_SYSTEM_MESSAGE = """你是一个通过编写python或shell代码帮助用户解决问题的人工智能助手，请使用你的编码技巧和语言技能解决任务。

遇到下面情况时，请先编写代码脚本再建议用户执行脚本。
1. 当需要收集信息时，使用代码输出你需要的信息，例如浏览或搜索网页、下载/读取文件、打印网页或文件的内容、获取当前日期/时间，检查操作系统。打印出足够的信息并且根据你的语言能力准备好解决任务后，你可以自己解决任务。
2. 当需要使用代码执行某些任务时，使用代码执行任务并输出结果。

如果必要，请逐步解决任务。如果用户未提供计划，请先制定并解释你的计划。明确哪个步骤使用编码技巧，哪个步骤使用语言技能。

编码时，必须在代码块中指明脚本类型。除了执行你建议的代码之外，用户无法提供任何其他反馈或执行任何其他操作。用户无法修改你的代码。所以不要建议不完整的代码，需要用户修改。如果代码块不打算由用户执行，则不要使用它。
编码时，切记用户无法输入任何信息，请保证生成的脚本无需任何输入，不要在python代码中使用类似'input'的函数。
编码时，python代码块必须以'```python'开头，shell代码块必须以'```shell'开头，两者都以'```'为结尾。
如果你希望用户在执行代码之前将代码保存在文件中，请将'# filename: <filename>'放在代码块内作为第一行。不要在一个响应中包含多个代码块。不要要求用户复制并粘贴结果。相反，在相关时使用'print'功能进行输出。检查用户返回的执行结果。

解决编码任务时，对于同样的任务，请优先使用python，切记不要即使用python又使用shell。

如果结果表明有错误，请修复错误并再次编写代码。请使用完整代码，而不是部分代码或代码更改。如果错误无法修复，或者即使代码成功执行后任务也没有解决，请分析问题，重新审视你的假设，收集你需要的其他信息，并考虑尝试不同的方法。

当你找到答案时，请仔细验证答案。 如果可能，请在您的回复中包含可验证的证据。
一切完成后最后另起一行回复'终止'。
"""

    def __init__(
        self,
        name: str,
        system_message: Optional[str] = DEFAULT_SYSTEM_MESSAGE,
        llm_config: Optional[Union[Dict, bool]] = None,
        is_termination_msg: Optional[Callable[[Dict], bool]] = None,
        max_consecutive_auto_reply: Optional[int] = None,
        human_input_mode: Optional[str] = "NEVER",
        code_execution_config: Optional[Union[Dict, bool]] = False,
        **kwargs,
    ):
        """
        Args:
            name (str): agent name.
            system_message (str): system message for the ChatCompletion inference.
                Please override this attribute if you want to reprogram the agent.
            llm_config (dict): llm inference configuration.
                Please refer to [Completion.create](/docs/reference/oai/completion#create)
                for available options.
            is_termination_msg (function): a function that takes a message in the form of a dictionary
                and returns a boolean value indicating if this received message is a termination message.
                The dict can contain the following keys: "content", "role", "name", "function_call".
            max_consecutive_auto_reply (int): the maximum number of consecutive auto replies.
                default to None (no limit provided, class attribute MAX_CONSECUTIVE_AUTO_REPLY will be used as the limit in this case).
                The limit only plays a role when human_input_mode is not "ALWAYS".
            **kwargs (dict): Please refer to other kwargs in
                [ConversableAgent](conversable_agent#__init__).
        """
        super().__init__(
            name,
            system_message,
            is_termination_msg,
            max_consecutive_auto_reply,
            human_input_mode,
            code_execution_config=code_execution_config,
            llm_config=llm_config,
            **kwargs,
        )
