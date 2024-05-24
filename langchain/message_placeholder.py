import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.schema import HumanMessage, AIMessage
from rich import print as pprint

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

human_prompt = "用 {word_count} 個字總結我們迄今為止的對話"
human_message_template = HumanMessagePromptTemplate.from_template(human_prompt)

chat_prompt = ChatPromptTemplate.from_messages(
        [MessagesPlaceholder(variable_name="conversation"), human_message_template]
)

pprint(chat_prompt)

human_message = HumanMessage(content="學習程式設計的最佳方法是甚麼?")
ai_message = AIMessage(content="""\
        1. 選擇程式語言: 決定想要學習的程式語言。

        2. 從基礎開始: 熟悉變數、資料類型和控制結構等基本程式設計概念。

        3. 練習、練習、再練習: 學習程式設計最好的方法就是透過實作經驗。\
""")

new_chat_prompt = chat_prompt.format_prompt(
        conversation=[human_message, ai_message],
        word_count="20"
)

pprint(new_chat_prompt)

chat_model = ChatOpenAI(model='gpt-3.5-turbo',
                        api_key=OPENAI_API_KEY)

pprint(chat_model.invoke(new_chat_prompt))
