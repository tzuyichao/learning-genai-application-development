import os 
from dotenv import load_dotenv
from rich import print as pprint
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.runnables import RunnablePassthrough
from operator import itemgetter

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

chat_model = ChatOpenAI(model='gpt-3.5-turbo',
                        api_key=OPENAI_API_KEY)

json_parser = JsonOutputParser()
format_instructions = json_parser.get_format_instructions()

str_parser = StrOutputParser()

pprint(format_instructions)

prompt1 = ChatPromptTemplate.from_template("請根據{attribute}特性，推薦一個環保的再生能源。請僅提供能源的名稱:")

model_parser = chat_model | str_parser

#energy_generator = (
#        {"attribute": RunnablePassthrough()}
#        | prompt1
#        | model_parser
#)

# pprint(energy_generator.invoke("零汙染"))

prompt2 = ChatPromptTemplate.from_template(
        "在永續發展中, {energy}能源通常用於製造哪種環保材料? 請僅提供能源材料的名稱"
        "{format_instructions}"
)

prompt3 = ChatPromptTemplate.from_template("假設每個國家的能源發展是相等的, 哪個國家使用{energy}能源可以做得最好? 請僅提供國家/地區名稱")

prompt4 = ChatPromptTemplate.from_template("請結合{material}和{country}, 描述一個環境友善的未來生活場景。")

prompt2 = prompt2.partial(format_instructions=format_instructions)

# pprint(chat_model.invoke(prompt2.invoke({"energy": "太陽能"})))

energy_generator = (
        {"attribute": RunnablePassthrough()}
        | prompt1
        | {"energy": model_parser}
)

energy_to_material = prompt2 | chat_model | json_parser

material_to_country = prompt3 | model_parser

question_generator = (
        energy_generator
        | {"material": energy_to_material | itemgetter('環保材料'), "country": material_to_country}
        | prompt4
)

pprint(question_generator)
question_generator.get_graph().print_ascii()

prompt = question_generator.invoke("零污染")
pprint(f"最終產生問題: {prompt.messages[0].content}\n\n"
       f"Model回答結果: {chat_model.invoke(prompt).content}")
