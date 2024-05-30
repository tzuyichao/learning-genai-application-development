import os
from dotenv import load_dotenv
from rich import print as pprint
from langchain_openai import ChatOpenAI
from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.memory import ChatMessageHistory

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(model="gpt-3.5-turbo",
                        api_key=OPENAI_API_KEY)

prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "妳是一個聊天助理, 請根據問題做回應"),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ]
)

pprint(prompt)

chain = prompt | chat_model

memory = ChatMessageHistory()

memories = {'0': memory, '1': ChatMessageHistory()}

chat_history = RunnableWithMessageHistory(
        chain,
        lambda session_id: memories[session_id],
        input_messages_key = 'input',
        history_messages_key = 'history',
)

content = chat_history.invoke(
        {"input": "這個公園裡有一個小狗叫Lucky"},
        config={"configurable": {"session_id": "0"}}
).content

pprint(content)
pprint(memory)
print('-' * 10)

content = chat_history.invoke(
        {"input": "公園裡的小狗叫甚麼? "},
        config={"configurable": {"session_id": "0"}}
).content

pprint(content)
pprint(memory)
print('-' * 10)

