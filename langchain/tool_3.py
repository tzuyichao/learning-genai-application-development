import os
from dotenv import load_dotenv
from rich import print as pprint
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI
from langchain.output_parsers import JsonOutputToolsParser, JsonOutputKeyToolsParser
from operator import itemgetter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

chat_model = ChatOpenAI(
        model = "gpt-3.5-turbo",
        api_key = OPENAI_API_KEY
)

class ItemGetter(RunnableLambda):
    def __init__(self, index):
        super().__init__(lambda x: x[index])

class SearchRun(BaseModel):
    query: str = Field(description="給搜尋引擎的關鍵字, 請使用繁體中文")

search_run = DuckDuckGoSearchRun(
        name="ddg-search",
        description="使用網路搜尋你不知道的事物",
        args_schema=SearchRun
)

print(f"工具名稱: {search_run.name}")
print(f"工具描述: {search_run.description}")
print(f"工具參數: {search_run.args}")

model_with_tool = chat_model.bind_tools([search_run])

chain = model_with_tool | JsonOutputToolsParser()

pprint(chain.invoke("2023年金馬獎影帝是誰?"))
print(f"type of chain: {type(chain)}")

chain = model_with_tool | JsonOutputKeyToolsParser(key_name="ddg-search")

pprint(chain.invoke("2023年金馬獎影帝是誰?"))
print(f"type of chain: {type(chain)}")

chain_test = model_with_tool | JsonOutputKeyToolsParser(key_name="ddg-search") | itemgetter(0)

pprint(chain_test.invoke("2023年金馬獎影帝是誰?"))

str_parser = StrOutputParser()
result_prompt = ChatPromptTemplate.from_template("請回答下列問題: {input}\n 以下為搜尋結果\n {results}")

print(f"type of chain: {type(chain)}")

chain = (
        chain
        | itemgetter(0)
        | (lambda x: print(f"LOG: before search_run: {x}") or x)
        | {"results": search_run, "input": RunnablePassthrough()}
        | (lambda x: print(f"LOG: before prompt: {x}") or x)
        | result_prompt
        | (lambda x: print(f"LOG: before to chat_model: {x}") or x)
        | chat_model
        | (lambda x: pprint(x) or x)
        | str_parser
)

print(chain.invoke("2023年金馬獎影帝是誰?"))
