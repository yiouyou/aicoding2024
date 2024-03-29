from .._log import logger_rag

from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
)
from langchain.schema import StrOutputParser
from langchain.chains import (
    LLMChain,
    RetrievalQA,
    RetrievalQAWithSourcesChain,
    StuffDocumentsChain,
)
from langchain_community.document_loaders import TextLoader
from langchain.chains.question_answering import load_qa_chain
from langchain.chains.summarize import load_summarize_chain
from langchain_community.callbacks import get_openai_callback
from langchain_core.callbacks import (
    AsyncCallbackManagerForRetrieverRun,
    CallbackManagerForRetrieverRun,
)
from langchain_community.retrievers import BM25Retriever

from .retriever import (
    get_vdb_multi_query_retriever,
    get_vdb_multi_query_retriever_textgen,
    get_docs_ensemble_retriever,
    get_docs_parent_retriever,
)
from ..toolset.load_file import load_text_to_doc
from ..local.textgen import get_textgen_llm


def pretty_print_docs(docs):
    # _pretty = f"\n{'-' * 100}\n".join([f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(docs)])
    _doc = []
    _doc_meta = []
    for i, doc in enumerate(docs):
        _doc.append(f"Document {i+1}:\n\n" + str(doc.metadata) + "\n\n" + doc.page_content)
        _doc_meta.append(f"Document {i+1}:\n\n" + str(doc.metadata)+ "\n" + str(len(doc.page_content)))
    _pretty = f"\n{'-' * 60}\n".join(_doc)
    # print(_pretty)
    _meta = f"\n{'-' * 60}\n".join(_doc_meta)
    # print(_meta)
    return _pretty


##### Multi Query
def qa_vdb_multi_query(_query, _vdb, _chain_type):
    if _chain_type not in ['stuff', 'map_reduce', 'refine', 'map_rerank']:
        logger_rag.error("_chain_type must be one of 'stuff', 'map_reduce', 'refine', or 'map_rerank'")
    _ans, _steps, _token_cost = "", "", ""
    llm = ChatOpenAI(model_name="gpt-3.5-turbo-16k", temperature=0)
    with get_openai_callback() as cb:
        _multi_retriever = get_vdb_multi_query_retriever(_vdb)
        ##### _docs
        _docs = _multi_retriever.get_relevant_documents(_query)
        #####
        _qa = load_qa_chain(
            llm,
            chain_type=_chain_type
        )
        _ans = _qa.invoke(
            {
                "input_documents": _docs,
                "question": _query
            },
            return_only_outputs=True
        )
        #####
        _token_cost = f"Tokens: {cb.total_tokens} = (Prompt {cb.prompt_tokens} + Completion {cb.completion_tokens}) Cost: ${format(cb.total_cost, '.5f')}"
        # print(_token_cost)
        _run_manager = CallbackManagerForRetrieverRun.get_noop_manager()
        _generated_queries = _multi_retriever.generate_queries(_query, _run_manager)
        logger_rag.info(f"Q: {_query}")
        for i in _generated_queries:
            logger_rag.info(i)
        _steps = "\n".join(_generated_queries)
        _steps += f"\n\n{'=' * 40}docs\n" + pretty_print_docs(_docs)
        logger_rag.info(f"A: {_ans['output_text']}")
        logger_rag.info(f"[{_chain_type}] {_token_cost}")
        logger_rag.debug(f"[{_chain_type}] {_steps}")
    return [_ans['output_text'], _steps, _token_cost]


def qa_vdb_multi_query_textgen(_query, _vdb, _chain_type, _textgen_url):
    if _chain_type not in ['stuff', 'map_reduce', 'refine', 'map_rerank']:
        logger_rag.error("_chain_type must be one of 'stuff', 'map_reduce', 'refine', or 'map_rerank'")
    _ans, _steps, _token_cost = "", "", ""
    _multi_retriever = get_vdb_multi_query_retriever_textgen(_vdb, _textgen_url)
    _run_manager = CallbackManagerForRetrieverRun.get_noop_manager()
    _generated_queries = _multi_retriever.generate_queries(_query, _run_manager)
    ##### _docs
    _docs = _multi_retriever.get_relevant_documents(_query)
    _bm25_retriever = BM25Retriever.from_documents(_docs)
    _docs = _bm25_retriever.get_relevant_documents(_query)
    ##### TheBloke_Yi-34B-200K-Llamafied-GPTQ
#     _template = """### 系统:

# 你是问答任务助手，请使用以下检索到的上下文信息来回答问题。如果没有明确答案，请回复"不知道"。

# ### 操作说明: 

# 上下文: 
# {context} 

# 请回答如下问题：
# {question}

# ### 回复:
# """
    ##### TheBloke_SUS-Chat-34B-GPTQ / SUS-Chat-34B-function-calling-v3-AWQ / Yi-34B-200K-Llamafied-chat-SFT-function-calling-v3-GPTQ
    _template = """### Human:
你是问答任务助手，请使用下面的上下文信息来回答给定问题。如果没有明确答案，请回复"不知道"，务必不要重复问题。

上下文: 
{context} 

给定问题：
{question}

### Assistant:
"""
    rag_prompt_yi = PromptTemplate(
        input_variables=["question", "context"],
        template=_template,
    )
    # llm = get_textgen_llm(_textgen_url, _top_p=0.1, _max_tokens=3000, _stopping_strings=["```", "###", "\n\n"])
    llm = get_textgen_llm(
        _textgen_url,
        _top_p=0.1,
        _max_tokens=5000,
        _stopping_strings=[]
    )
    _qa = load_qa_chain(
        llm,
        chain_type=_chain_type,
        prompt=rag_prompt_yi
    )
    _ans = _qa.invoke(
        {
            "input_documents": _docs,
            "question": _query
        },
        return_only_outputs=False
    )
    logger_rag.info(_ans)
    #####
    logger_rag.info(f"Q: {_query}")
    for i in _generated_queries:
        logger_rag.info(i)
    _steps = "\n".join(_generated_queries)
    _steps += f"\n\n{'=' * 40}docs\n" + pretty_print_docs(_docs)
    logger_rag.info(f"A: {_ans['output_text']}")
    logger_rag.info(f"[{_chain_type}] {_token_cost}")
    logger_rag.debug(f"[{_chain_type}] {_steps}")
    return [_ans['output_text'], _steps, _token_cost]


##### Ensemble
def qa_docs_ensemble_query(_query, _docs, _chain_type):
    if _chain_type not in ['stuff', 'map_reduce', 'refine', 'map_rerank']:
        logger_rag.error("_chain_type must be one of 'stuff', 'map_reduce', 'refine', or 'map_rerank'")
    _ans, _steps, _token_cost = "", "", ""
    llm = ChatOpenAI(model_name="gpt-3.5-turbo-16k", temperature=0)
    with get_openai_callback() as cb:
        _ensemble_retriever = get_docs_ensemble_retriever(_docs)
        ##### _docs
        _docs = _ensemble_retriever.get_relevant_documents(_query)
        #####
        _qa = load_qa_chain(
            llm,
            chain_type=_chain_type
        )
        _ans = _qa.invoke(
            {
                "input_documents": _docs,
                "question": _query
            },
            return_only_outputs=True
        )
        #####
        _token_cost = f"Tokens: {cb.total_tokens} = (Prompt {cb.prompt_tokens} + Completion {cb.completion_tokens}) Cost: ${format(cb.total_cost, '.5f')}"
        # print(_token_cost)
        _steps = f"\n\n{'=' * 40}docs\n" + pretty_print_docs(_docs)
        logger_rag.info(f"A: {_ans['output_text']}")
        logger_rag.info(f"[{_chain_type}] {_token_cost}")
        logger_rag.debug(f"[{_chain_type}] {_steps}")
    return [_ans['output_text'], _steps, _token_cost]


##### Parent Document
def qa_docs_parent_query(_query, _docs, _chain_type):
    if _chain_type not in ['stuff', 'map_reduce', 'refine', 'map_rerank']:
        logger_rag.error("_chain_type must be one of 'stuff', 'map_reduce', 'refine', or 'map_rerank'")
    _ans, _steps, _token_cost = "", "", ""
    llm = ChatOpenAI(model_name="gpt-3.5-turbo-16k", temperature=0)
    with get_openai_callback() as cb:
        _parent_retriever = get_docs_parent_retriever(_docs)
        ##### _docs
        _docs = _parent_retriever.get_relevant_documents(_query)
        #####
        _qa = load_qa_chain(
            llm,
            chain_type=_chain_type
        )
        _ans = _qa.invoke(
            {
                "input_documents": _docs,
                "question": _query
            },
            return_only_outputs=True
        )
        #####
        _token_cost = f"Tokens: {cb.total_tokens} = (Prompt {cb.prompt_tokens} + Completion {cb.completion_tokens}) Cost: ${format(cb.total_cost, '.5f')}"
        # print(_token_cost)
        _steps = f"\n\n{'=' * 40}docs\n" + pretty_print_docs(_docs)
        logger_rag.info(f"A: {_ans['output_text']}")
        logger_rag.info(f"[{_chain_type}] {_token_cost}")
        logger_rag.debug(f"[{_chain_type}] {_steps}")
    return [_ans['output_text'], _steps, _token_cost]


##### summerize the qa ans txt file
def qa_summerize(_txt_fp: str, _chain_type: str):
    docs = TextLoader(_txt_fp).load()
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    with get_openai_callback() as cb:
        chain = load_summarize_chain(llm, chain_type=_chain_type)
        _sum = chain.run(docs)
        _token_cost = f"Tokens: {cb.total_tokens} = (Prompt {cb.prompt_tokens} + Completion {cb.completion_tokens}) Cost: ${format(cb.total_cost, '.5f')}"
        logger_rag.info(f"summarize: {_sum}")
        logger_rag.info(f"[{_chain_type}] {_token_cost}")
    return [_sum, _token_cost]


##### summerize text
def summerize_text(_text: str, _chain_type: str):
    doc = load_text_to_doc(_text)
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    with get_openai_callback() as cb:
        chain = load_summarize_chain(llm, chain_type=_chain_type)
        _sum = chain.run([doc])
        _token_cost = f"Tokens: {cb.total_tokens} = (Prompt {cb.prompt_tokens} + Completion {cb.completion_tokens}) Cost: ${format(cb.total_cost, '.5f')}"
        logger_rag.info(f"summarize: {_sum}")
        logger_rag.info(f"[{_chain_type}] {_token_cost}")
    return [_sum, _token_cost]


##### qa with context as lawyer
def qa_with_context_as_lawyer(_query, _context):
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template ="""Giving following context:
{_context}

Completely answer the following questions from all angles as a perfessional lawyer without any bias:
{_query}
"""
    prompt = PromptTemplate.from_template(template)
    with get_openai_callback() as cb:
        chain = prompt | llm | StrOutputParser()
        _ans = chain.invoke({"_query": _query, "_context": _context})
        _token_cost = f"Tokens: {cb.total_tokens} = (Prompt {cb.prompt_tokens} + Completion {cb.completion_tokens}) Cost: ${format(cb.total_cost, '.5f')}"
        logger_rag.info(f"{_ans}")
        logger_rag.info(f"{_token_cost}")
    return [_ans, _token_cost]


##### qa with context as military intelligence officer
def qa_with_context_as_mio(_query, _context):
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template ="""给定下面信息：
{_context}

作为一名军事情报人员，请从各个角度完整清晰的回答以下问题：
{_query}
"""
    prompt = PromptTemplate.from_template(template)
    with get_openai_callback() as cb:
        chain = prompt | llm | StrOutputParser()
        _ans = chain.invoke({"_query": _query, "_context": _context})
        _token_cost = f"Tokens: {cb.total_tokens} = (Prompt {cb.prompt_tokens} + Completion {cb.completion_tokens}) Cost: ${format(cb.total_cost, '.5f')}"
        logger_rag.info(f"{_ans}")
        logger_rag.info(f"{_token_cost}")
    return [_ans, _token_cost]


##### qa with context as military intelligence officer
def qa_with_context_as_mio_textgen(_query, _context, _textgen_url):
    _ans, _steps, _token_cost = "", "", ""
    llm = get_textgen_llm(
        _textgen_url,
        _top_p=0.1,
        _max_tokens=1000,
        _stopping_strings=[]
    )
    template ="""### Human:
你是一名军事情报人员，请根据给定上下文，从各维度全面回答给定问题，并给出具体的解释。如果没有明确答案，请回复"不知道"，务必不要重复问题。

上下文:
{_context}

问题:
{_query}

### Assistant:
"""
    prompt = PromptTemplate.from_template(template)
    chain = prompt | llm | StrOutputParser()
    _ans = chain.invoke({"_query": _query, "_context": _context})
    logger_rag.info(f"{_ans}")
    logger_rag.info(f"{_token_cost}")
    return [_ans, _token_cost]


##### qa with context as government officer
def qa_with_context_as_go(_query, _context):
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template ="""给定下面信息：
{_context}

作为一名政府事务专家，请从各个角度完整清晰的回答以下问题：
{_query}
"""
    prompt = PromptTemplate.from_template(template)
    with get_openai_callback() as cb:
        chain = prompt | llm | StrOutputParser()
        _ans = chain.invoke({"_query": _query, "_context": _context})
        _token_cost = f"Tokens: {cb.total_tokens} = (Prompt {cb.prompt_tokens} + Completion {cb.completion_tokens}) Cost: ${format(cb.total_cost, '.5f')}"
        logger_rag.info(f"{_ans}")
        logger_rag.info(f"{_token_cost}")
    return [_ans, _token_cost]


##### create_rag_subtask_list_textgen
def create_rag_subtask_list_textgen(_query, _textgen_url):
    _ans, _token_cost = "", ""
    llm = get_textgen_llm(
        _textgen_url,
        _top_p=0.1,
        _max_tokens=500,
        _stopping_strings=[]
    )
    template ="""### Human:
你是一名军事情报人员，请将给定的复杂问题从多个方面和多个角度拆解为3个左右更简单的子问题。
请注意子问题中不能含有'是否'类的提问，且必须与原问题密切相关。
仅输出子问题列表，不能重复，不输出其他任何内容。

复杂问题:
"{_query}"

### Assistant:
"""
    prompt = PromptTemplate.from_template(template)
    chain = prompt | llm | StrOutputParser()
    _ans = chain.invoke({"_query": _query})
    logger_rag.info(f"{_ans}")
    logger_rag.info(f"{_token_cost}")
    _ans = f"{_query}\n{_ans}"
    return _ans, _token_cost

