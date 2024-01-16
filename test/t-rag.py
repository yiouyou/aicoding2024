import os
_module = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys
sys.path.append(_module)

from module.rag.digest_dir import (
    dir_to_faiss_HuggingFace,
    md_dir_to_faiss_HuggingFace,
)
from module.rag.vdb_faiss import get_faiss_HuggingFace
from module.rag.qa_chain import qa_vdb_multi_query


_dir = '/home/songz/aicoding2024/GPTsData/鸿蒙开发助手/all'
_db_name = 'test_hf'
_clean_txt_dir = 'test_clean'

db = get_faiss_HuggingFace(_db_name)
if db is None:
    md_dir_to_faiss_HuggingFace(_dir, _db_name, _clean_txt_dir)

# simdoc = db.similarity_search('线性布局是什么？')
# print(simdoc[0].page_content)


while True:
    query = input("问题：\n")
    # print(query)
    ans, steps, token_cost = qa_vdb_multi_query(query, db, 'stuff')
    # print(steps)
    print(ans)
    print(token_cost)

