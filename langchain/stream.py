from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from rich import print as pprint

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

chat_model = ChatOpenAI(model='gpt-3.5-turbo', api_key=OPENAI_API_KEY)

chunks = chat_model.stream("你好, 請使用繁體中文")
print(chunks)

for chunk in chunks:
    print(chunk, end="", flush=True)

