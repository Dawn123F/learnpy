from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("./论文介绍.pdf")
docs = loader.load()

for item in docs:
    print(item)