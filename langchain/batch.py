from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from rich import print as pprint

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

chat_model = ChatOpenAI(model='gpt-3.5-turbo', api_key=OPENAI_API_KEY)

pprint(chat_model.batch(["我家的小狗叫lucky，請使用繁體中文",
                         "請使用繁體中文，我家的小狗叫什麼?"]))

