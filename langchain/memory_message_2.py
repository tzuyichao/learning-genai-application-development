import os
from dotenv import load_dotenv
from rich import print as pprint
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()

memory.save_context({"input": "你也來散步阿"},
                    {"output": "這個中正公園很適合運動"})

pprint(memory)
print('-' * 10)
pprint(memory.buffer_as_messages)
print('-' * 10)
pprint(memory.buffer)
print('-' * 10)
memory.return_messages = True
pprint(memory.buffer)

