import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.document_loaders import PyPDFLoader
from rich import print as pprint

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(
        model="gpt-3.5-turbo",
        api_key=OPENAI_API_KEY
)

embeddings_model = OpenAIEmbeddings(
        model='text-embedding-3-large',
        api_key=OPENAI_API_KEY
)

loader = PyPDFLoader(file_path="https://ppt.cc/f9nc5x")

docs = loader.load()

pprint(docs[0])

index = VectorstoreIndexCreator(embedding=embeddings_model).from_loaders([loader])

query = "酒後開車且酒精濃度超過規定標準應罰款多少?"

response = index.query(llm=chat_model, question=query)

print(f"1: {query}\n")
pprint(response)

query = "酒後開車但酒精濃度未超標應罰款多少?"
print(f"2: {query}\n")

response = index.query(llm=chat_model, question=query)
pprint(response)

