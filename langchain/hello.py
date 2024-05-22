from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

chat_model = ChatOpenAI(model='gpt-3.5-turbo', api_key = OPENAI_API_KEY)

response = chat_model.invoke("你好，請使用繁體中文")
print(response)

