from openai import OpenAI
import os
from dotenv import load_dotenv
from rich import print as pprint

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding

pprint(get_embedding("甚麼是OpenAI?"))

