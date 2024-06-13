import os 
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from rich import print as pprint

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

embedding_models = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key=OPENAI_API_KEY
)

docs = [
    {"page_content": "天空是藍色的"},
    {"page_content": "天空不是紅色的"},
    {"page_content": "Sky is blue"},
    {"page_content": "莓果是藍色的"},
    {"page_content": "我今天吃了漢堡"}
]

persist_dir = "/home/terencechao/chroma/db"

Chroma.from_documents(
    documents=docs,
    embedding=embedding_models,
    persist_directory=persist_dir,
    collection_metadata={"hnsw:space": "cosine"}
)

db = Chroma(
    persist_directory=persist_dir,
    embedding=embedding_model
)

pprint(db.search("天空的顏色是?"))

