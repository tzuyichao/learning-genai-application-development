from openai import OpenAI
import os
from dotenv import load_dotenv
from rich import print as pprint
import numpy as np

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding

def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2)

embedding1 = get_embedding("甚麼是OpenAI?")
embedding2 = get_embedding("甚麼是ChatGPT?")

similarity = cosine_similarity(embedding1, embedding2)
print(f"Cosine similarity: {similarity}")

