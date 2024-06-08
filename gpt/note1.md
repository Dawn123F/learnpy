## 什么是langchain
LangChain是一个由大型语言模型 (LLM) 驱动的应用程序开发框架。
LangChain 简化了 LLM 应用程序生命周期的每个阶段：

开发：使用 LangChain 的开源构建块和组件构建您的应用程序。使用第三方集成和模板快速开始运行。
生产化：使用LangSmith检查、监控和评估您的链，以便您可以不断优化和自信地部署。
部署：使用LangServe将任何链转变为 API 。                                     

## 为什么要用langchain
langchain解决了大模型没有记忆，不能读取外部知识库，不能调用外部工具等问题，
langchain提供了一套接口来适配不同模型的差异，降低开发复杂度

## langchain基础
使用langchain框架开发需要了解如下五个名词概念方便我们进行后续的开发任务

模型(model)
    抽象了大语言模型的客户端,用于理解输入并输出相关结果
记忆(memory)
    记住上下文的消息列表                        
链(chain)
    链接构建应用所需的组件
检索(retriever)
    增加模型的知识面和回答的准确性
agent(agent)
    智能体 根据ai理解根据任务动态评估和确定行动路径


## langchain agent


