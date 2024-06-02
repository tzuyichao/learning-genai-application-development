import os
from dotenv import load_dotenv
from rich import print as pprint
import openai

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = openai.OpenAI(api_key = OPENAI_API_KEY)

assistant = client.beta.assistants.create(
        name="系統管理專家",
        instructions="你是一個熱愛程式設計的系統管理專機師, 你擅長各種程式語言、作業系統與相關知識",
        model="gpt-3.5-turbo"
)

pprint(assistant)



