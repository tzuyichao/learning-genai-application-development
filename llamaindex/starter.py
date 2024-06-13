import os
from dotenv import load_dotenv
import logging
import sys
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from rich import print as pprint

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")

pprint(response)
