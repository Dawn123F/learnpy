
from langchain_openai import ChatOpenAI
from langchain.schema.messages import (SystemMessage,HumanMessage)

# 安装lanchain pip install langchain
# 安装lanchain pip install langchain_openai
# 安装lanchain pip install langchain_community
model = ChatOpenAI(
    openai_api_base="https://api.aigc369.com/v1",
    model_name="gpt-3.5-turbo",
)

human_message = HumanMessage(content="帮我写一篇关于人类未来的博文")

resource = model.invoke([human_message])

print(resource)