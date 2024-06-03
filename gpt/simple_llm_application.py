import getpass
import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

#os.environ["LANGCHAIN_TRACING_V2"] = "true"

parser = StrOutputParser()

model = ChatOpenAI(
    openai_api_base="https://api.aigc369.com/v1",
    model_name="gpt-3.5-turbo",
)

system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

result = prompt_template.invoke({"language": "italian", "text": "hi"})

chain = prompt_template | model | parser

print(type(chain))

print(chain)

print(chain.invoke({"language": "italian", "text": "hi"}))