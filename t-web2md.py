urls = [
    "https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/start-with-ets-stage-0000001477980905-V3",
]

# from langchain_community.document_loaders import WebBaseLoader
# loader = WebBaseLoader(urls)
# # loader.requests_kwargs = {'verify':False}
# data = loader.load()
# print(data)


# from langchain_community.document_loaders import UnstructuredURLLoader
# loader = UnstructuredURLLoader(urls=urls)
# data = loader.load()
# print(data)


import requests
def get_url_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return str(e)
content = get_url_content(urls[0])
print(content)

