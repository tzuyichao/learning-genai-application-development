import os
from dotenv import load_dotenv
from rich import print as pprint
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

chat_model = ChatOpenAI(model='gpt-3.5-turbo',
                        api_key=OPENAI_API_KEY)

str_parser = StrOutputParser()

prompt = ChatPromptTemplate.from_template('{city} 位於哪個國家?')

lang_prompt = ChatPromptTemplate.from_template('{city} 講那些語言?')

find_country_chain = prompt | chat_model | str_parser
find_lang_chain = lang_prompt | chat_model | str_parser

# pprint(find_country_chain.invoke({'city': '高雄'}))
# pprint(find_lang_chain.invoke({'city': '高雄'}))

find_country_and_lang_chain = RunnableParallel(
        country=find_country_chain,
        lang=find_lang_chain
)
pprint(find_country_and_lang_chain.invoke({'city': '高雄'}))
