from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from typing import List

from langchain_community.document_loaders import WikipediaLoader, YoutubeLoader

from langchain_core.documents import Document
from langchain_core.runnables import RunnableLambda

documents = [
    Document(
        page_content="Dogs are great companions, known for their loyalty and friendliness.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Cats are independent pets that often enjoy their own space.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Goldfish are popular pets for beginners, requiring relatively simple care.",
        metadata={"source": "fish-pets-doc"},
    ),
    Document(
        page_content="Parrots are intelligent birds capable of mimicking human speech.",
        metadata={"source": "bird-pets-doc"},
    ),
    Document(
        page_content="Rabbits are social animals that need plenty of space to hop around.",
        metadata={"source": "mammal-pets-doc"},
    ),
]

vectorstore = Chroma.from_documents(
    documents,
    embedding=OpenAIEmbeddings(
        openai_api_base="https://api.aigc369.com/v1",
    ),
)

# retriever = RunnableLambda(vectorstore.similarity_search).bind(k=1)  # select top result
#
#
# for item in retriever.batch(["cat", "shark"]):
#     print(item)

loder = YoutubeLoader(video_id="中国")
print(loder.load())

