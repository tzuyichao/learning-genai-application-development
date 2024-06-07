import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import rdflib
from rich import print as pprint

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

embeddings_model = OpenAIEmbeddings(
        model = 'text-embedding-3-large',
        api_key = OPENAI_API_KEY
)

documents = [
        {"text": "Apple iPhone 13 is the latest model with A15 Bionic chip."},
        {"text": "Samsung Galaxy S21 has a great camera and display."},
        {"text": "Google Pixel 6 offers excellent software integration."}
]

faiss_index = FAISS.from_texts([doc["text"] for doc in documents], embeddings_model)
pprint(faiss_index)

for result in faiss_index.similarity_search("Bionic chip", k=3):
    pprint(result)

print('-' * 10)

kg_data = """
@prefix ex: <http://example.org/products#> .
ex:iPhone13 ex:hasFeature "A15 Bionic chip" .
ex:GalaxyS21 ex:hasFeature "Great Camera" .
ex:Pixel6 ex:hasFeature "Excellent Software" .
"""

kg = rdflib.Graph()
kg.parse(data=kg_data, format="turtle")

kg_query = """
SELECT ?product ?feature WHERE {
    ?product ex:hasFeature ?feature .
    }
"""

pprint(kg)

for row in kg.query(kg_query):
    if "Bionic chip".lower() in row[1].lower():
        pprint(row)
