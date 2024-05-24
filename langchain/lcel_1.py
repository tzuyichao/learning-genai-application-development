import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from rich import print as pprint
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

chat_model = ChatOpenAI(model='gpt-3.5-turbo',
                        api_key=OPENAI_API_KEY)

str_parser = StrOutputParser()

prompt = ChatPromptTemplate.from_template(
        '{city} 位於哪一個國家?'
)

chain = prompt | chat_model | str_parser

pprint(chain.invoke({"city": "台北"}))
