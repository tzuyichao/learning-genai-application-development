from rich import print as pprint
from langchain.memory import ChatMessageHistory
from langchain_core.messages import (
        AIMessage,
        HumanMessage,
        SystemMessage
)

memory = ChatMessageHistory()
memory.add_user_message("妳好")
memory.add_ai_message("妳好, 有什麼需要幫忙的嗎?")

pprint(memory)

print('-' * 10)

def print_message(history):
    for message in history.messages:
        pprint(message)

print_message(memory)

print('-' * 10)

memory.add_messages([
    AIMessage("沒關係, 妳可以隨時找我"),
    HumanMessage("好的")
])

print_message(memory)

print('-' * 10)

memory.clear()

print_message(memory)
