from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings


##### embedding
def get_embedding_OpenAI():
    _model_name = "openai"
    _embedding = OpenAIEmbeddings()
    return _model_name, _embedding


def get_embedding_HuggingFace():
    ### all-mpnet-base-v2/multi-qa-mpnet-base-dot-v1/all-MiniLM-L12-v2
    _model_name = "all-mpnet-base-v2"
    _embedding = HuggingFaceEmbeddings(
        model_name=f"sentence-transformers/{_model_name}",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': False}
    )
    return _model_name, _embedding

