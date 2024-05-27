import os
from dotenv import load_dotenv
from rich import print as pprint
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

chat_model = ChatOpenAI(model='gpt-3.5-turbo',
                        api_key=OPENAI_API_KEY)

str_parser = StrOutputParser()

person_prompt = ChatPromptTemplate.from_template("是誰發明{invention}?")
country_prompt = ChatPromptTemplate.from_template("{person}來自哪個國家?")

person_chain = ({"invention": RunnablePassthrough()}
                | person_prompt
                | chat_model
                | str_parser)

person_summary_chain = (
        {"person": person_chain}
        | country_prompt
        | chat_model
        | str_parser
)

pprint(person_summary_chain.invoke("珍珠奶茶"))

compare_prompt = ChatPromptTemplate.from_template("{invention}發明自那個國家?")
compare_chain = compare_prompt | chat_model | str_parser

pprint(compare_chain.invoke({"invention": "珍珠奶茶"}))
