import os
from dotenv import load_dotenv
from rich import print as pprint
from langchain_openai import OpenAIEmbeddings
import numpy as np

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

embeddings_model = OpenAIEmbeddings(
        model="text-embedding-3-large",
        api_key=OPENAI_API_KEY
)

docs = [
        "天空是藍色的",
        "天空不是紅色的",
        "Sky is blue",
        "莓果是藍色的",
        "我今天吃了漢堡"
]

embeddings = embeddings_model.embed_documents(docs)
print(f"length of embedding: {len(embeddings[0])}")

embedded_query = embeddings_model.embed_query("天空的顏色是?")

def cosine_similarity(a, b):
    return np.dot(a, b)

for doc_res, doc in zip(embeddings, docs):
    similarity = cosine_similarity(embedded_query, doc_res)
    print(f'"{doc}" 與問題的相似度是{similarity}')
