from langchain_openai import ChatOpenAI
from langchain.schema.messages import (SystemMessage, HumanMessage)
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system", "{instructions}"
        ),
        (
            "user", "帮我生成{color}的5个颜色码"
        )
    ]
)

# 安装lanchain pip install langchain
# 安装lanchain pip install langchain_openai
# 安装lanchain pip install langchain_community
model = ChatOpenAI(
    openai_api_base="https://api.aigc369.com/v1",
    model_name="gpt-3.5-turbo"
)

parser = CommaSeparatedListOutputParser()

chain = prompt | model | parser

response = chain.invoke(input={"instructions": parser.get_format_instructions(), "color": "红褐色系"})

print(response)
#
# resource = model.invoke([human_message])
