from time import sleep

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
import os
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough


model = ChatOpenAI(
    openai_api_base="https://api.aigc369.com/v1",
    model_name="gpt-3.5-turbo",
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability in {language}.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)


def filter_messages(messages, k=10):
    return messages[-k:]



chain = (
        RunnablePassthrough.assign(messages=lambda x: filter_messages(x["messages"]))
        | prompt
        | model
)

store = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


messages = [
    HumanMessage(content="hi! I'm bob"),
    AIMessage(content="hi!"),
    HumanMessage(content="I like vanilla ice cream"),
    AIMessage(content="nice"),
    HumanMessage(content="whats 2 + 2"),
    AIMessage(content="4"),
    HumanMessage(content="thanks"),
    AIMessage(content="no problem!"),
    HumanMessage(content="having fun?"),
    AIMessage(content="yes!"),
]

with_message_history = RunnableWithMessageHistory(chain, get_session_history, input_messages_key="messages")
with_message_history.invoke()
config = {"configurable": {"session_id": "abc2"}}

# response = with_message_history.invoke(
#     {
#         "messages": messages + [HumanMessage(content="whats my name?")],
#         "language": "English",
#     },
#     config=config,
# )
#
# print(response.content)
# todo 流媒体打印
config = {"configurable": {"session_id": "abc15"}}
for r in with_message_history.stream(
    {
        "messages": [HumanMessage(content="hi! I'm todd. tell me a joke")],
        "language": "English",
    },
    config=config,
):
    sleep(1)
    print(r.content)