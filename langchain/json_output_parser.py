import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from rich import print as pprint
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

json_parser = JsonOutputParser()
format_instructions = json_parser.get_format_instructions()

pprint(format_instructions)

chat_model = ChatOpenAI(model='gpt-3.5-turbo',
                        api_key=OPENAI_API_KEY)

message = chat_model.invoke("""請提供一個國家的名稱和首都, 
                            {format_instructions}, 使用台灣語言, 格式是
                            {
                            "國家": "國家名稱",
                            "首都": "國家首都"
                            }
""")

pprint(message)
print(message.content)

json_output = json_parser.invoke(message)

pprint(json_output)
