from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from rich import print as pprint
from langchain.globals import set_llm_cache
from langchain_community.cache import InMemoryCache

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

chat_model = ChatOpenAI(model='gpt-3.5-turbo', 
                        api_key=OPENAI_API_KEY,
                        cache=True)

set_llm_cache(InMemoryCache())

print(chat_model.invoke("Hello, 請使用繁體中文").id)
print(chat_model.invoke("Hello, 請使用繁體中文").id)

