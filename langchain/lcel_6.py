import os
from dotenv import load_dotenv
from rich import print as pprint
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableBranch
from operator import itemgetter

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

chat_model = ChatOpenAI(model='gpt-3.5-turbo',
                        api_key=OPENAI_API_KEY)

str_parser = StrOutputParser()

chain = (
        PromptTemplate.from_template(
            "根據使用者問題作回答，將問題分為要求命令或者查詢問題。\n"
            "<問題>\n{question}\n</問題>\n"
            "分類:"
        )
        | chat_model
        | str_parser
)

# pprint(chain.invoke({"question": "立刻使用google搜尋台積電股票"}))
# pprint(chain.invoke({"question": "告訴我甚麼是極光"}))

order_chain = (
        PromptTemplate.from_template(
            "你不會思考只根據命令做回應, 每次回答開頭都以'是的, 主人'"
            "回覆命令\n"
            "問題: {question}\n"
            "回覆:"
        )
        | chat_model
)

ask_chain = (
        PromptTemplate.from_template(
            "你只能回答知識性相關問題, 任何要求命令不會照做也不會回答"
            "每次回答都以 '根據我的知識' 回覆命令\n"
            "問題: {question}"
            "回覆: "
        )
        | chat_model
)

default_chain = (
        PromptTemplate.from_template(
            "請回答問題\n"
            "問題: {question}"
            "回覆: "
        )
        | chat_model
)

branch = RunnableBranch(
        (lambda x: "查詢答案" in x["topic"], ask_chain),
        (lambda x: "要求命令" in x["topic"], order_chain),
        default_chain
)

full_chain = (
        {
            "topic": chain, "question": lambda x: x["question"]
        }
        | branch
        | str_parser
)

pprint(full_chain.invoke({"question": "幫我寫一篇哈利波特小說短評"}))
print('- ' * 10)
pprint(full_chain.invoke({"question": "台北101有多高?"}))
