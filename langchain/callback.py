from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from rich import print as pprint
from langchain.callbacks import get_openai_callback
from langchain.globals import set_llm_cache
from langchain_community.cache import InMemoryCache


load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

chat_model = ChatOpenAI(model='gpt-3.5-turbo',
                        api_key=OPENAI_API_KEY,
                        cache=True)

set_llm_cache(InMemoryCache())

with get_openai_callback() as cb:
    result = chat_model.invoke("你好, 請使用繁體中文")
    print(result.response_metadata['token_usage'])
    print(result.id)
    pprint(cb)

