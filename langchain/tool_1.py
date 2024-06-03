import os
from dotenv import load_dotenv
from rich import print as pprint
from langchain_openai import ChatOpenAI
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from operator import itemgetter, attrgetter
from langchain_core.runnables import (
        RunnableLambda, RunnablePassthrough
)

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(
        model="gpt-3.5-turbo",
        api_key=OPENAI_API_KEY
)

search = DuckDuckGoSearchAPIWrapper()

result = search.results("2023年金馬獎影后是?", 10)

for item in result:
    print(f"標題: {item['title']}\n")
    print(f"摘要: {item['snippet']}\n")

result_template = "請回答下列問題: {input}\n 以下為搜尋結果\n {results}"

result_prompt = ChatPromptTemplate.from_template(result_template)
str_parser = StrOutputParser()

chain = (
        {"results": search.run, "input": RunnablePassthrough()}
        | result_prompt
        | chat_model
        | str_parser
)

print(chain.invoke("2023年金馬獎影帝是?"))

