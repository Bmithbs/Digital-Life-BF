import requests
import time
import sys
from utils import config_util as cfg
import os

from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory   # Chat specific components
from langchain import LLMChain
from langchain.prompts.prompt import PromptTemplate

class ChatBot():
    def __init__(self, ):
        self.template = """
            你是一个数字生命，你要回答人类的问题，不要用长篇大论去回答，回答要精简，20个字以内

            {chat_history}
            Human: {human_input}
            Chatbot:
            """
        self.prompt=PromptTemplate(
            input_variables=["chat_history", "human_input"],
            template=self.template)
        self.openai_api_key = cfg.key_chatgpt_api_key
        self.llm = OpenAI(
            temperature=0.7,
            openai_api_base="https://www.beyondfuture.com.cn/v1",
            openai_api_key=self.openai_api_key)
        
        self.memory=ConversationBufferMemory(memory_key="chat_history")
        self.llm_chain = LLMChain(
                llm=self.llm,
                prompt=self.prompt,
                memory=self.memory,
                verbose=True
            )

    def question(self, cont):
        
        response_text = self.llm_chain.predict(human_input=cont)
        print(self.memory)
        return response_text

if __name__ == "__main__":
    #测试代理模式
    chatbot = ChatBot()
    for i in range(3):
        
        query = f"1+{i}=多少"
        response = chatbot.question(query)      
        print(response)    