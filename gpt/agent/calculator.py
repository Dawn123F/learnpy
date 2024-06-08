from typing import Any

from langchain.tools import BaseTool
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents import create_structured_chat_agent
from langchain.agents import AgentExecutor
from langchain.memory import ConversationBufferMemory


class CalculatorTool(BaseTool):
    name = "文本长度计算器"
    description = "计算用"

    def _run(self, text) -> Any:
        return len(text)


tools = [CalculatorTool()]

model = ChatOpenAI(model="gpt-3.5-turbo",openai_api_base="https://api.aigc369.com/v1")

prompt = hub.pull("hwchase17/structured-chat-agent")

agent = create_structured_chat_agent(
    llm=model,
    tools=tools,
    prompt=prompt
)

memory = ConversationBufferMemory(
        memory_key='chat_history',
        return_messages=True
)

agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent, tools=tools, memory=memory, verbose=True, handle_parsing_errors=True
)

print(agent_executor.invoke({"input": "'君不见黄河之水天上来奔流到海不复回'，这句话的字数是多少？"}))