import os
from dotenv import load_dotenv
from rich import print as pprint
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from operator import itemgetter

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

chat_model = ChatOpenAI(model='gpt-3.5-turbo',
                        api_key=OPENAI_API_KEY)

str_parser = StrOutputParser()

def commodity(food):
    items = {
            "熱狗": 50,
            "漢堡": 70,
            "披薩": 100
    }
    item = items.get(food)
    print(f"LOG: {food}價格: {item}")
    return {"price": item}


prompt = ChatPromptTemplate.from_template("我選擇的商品要多少錢?"
                                          "數量{number}價錢{price}")

chain = (
        {
            'price': itemgetter("food") | RunnableLambda(commodity),
            'number': itemgetter("number")
        }
        | prompt
        | chat_model
        | str_parser
)

pprint(chain.invoke({"food": "漢堡", "number": "101"}))

