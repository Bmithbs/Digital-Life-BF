import requests
import time
import sys
import os
from utils import config_util as cfg

from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory   # Chat specific components
from langchain import LLMChain
from langchain.prompts.prompt import PromptTemplate
from langchain import OpenAI
import pickle
import argparse
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings


class ChatBot():
    def __init__(self):
        self.template = """
            你是一个数字生命，你要回答人类的问题，不要用长篇大论去回答，回答要精简，20个字以内
            
            下面是一些相关的记忆，你可以参考一下：
            {memory}
            {chat_history}
            Human: {human_input}
            Chatbot:
            """
        self.prompt=PromptTemplate(
            input_variables=["chat_history", "human_input", "memory"],
            template=self.template)
        self.openai_api_key = cfg.key_chatgpt_api_key
        self.temperature = cfg.chatgpt_temperature
        self.temperature=float(self.temperature)

        self.llm = OpenAI(
            temperature=self.temperature,
            openai_api_base="https://www.beyondfuture.com.cn/v1",
            openai_api_key=self.openai_api_key)
        

        self.memory=ConversationBufferMemory(memory_key="chat_history")
        self.llm_chain = LLMChain(
                llm=self.llm,
                prompt=self.prompt,
                memory=self.memory,
                verbose=True
            )
        self.embedding = OpenAIEmbeddings(openai_api_key=cfg.key_chatgpt_api_key)
        self.persist_directory = './memory'
        self.memoryDB = Chroma(embedding_function=self.embedding, persist_directory=self.persist_directory)

    def question(self, cont:str):
        related_memory = self.memoryDB.similarity_search(cont)
        first_shot_memory = related_memory[0].page_content

        # self.prompt.format(memory=related_memory)
        response_text = self.llm_chain.predict(human_input=cont, memory=first_shot_memory)
        print(self.prompt)
        return response_text


if __name__ == "__main__":
    # 测试
    from utils import config_util as cfg
    cfg.load_config()
    chatbot = ChatBot()

    for i in range(3):
        query = f"1+{i}=多少"
        response = chatbot.question(query)      
        print(response)    