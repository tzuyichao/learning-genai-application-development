from langchain.prompts import ChatPromptTemplate
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from rich import print as pprint

chat_template = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一位會教{topic}的教師"),
            ("human",  "可以再說一次嗎?"),
            ("ai", "好的, 我再講解一次"),
            ("human", "{input}"),
        ]
)
pprint(chat_template)

message_list = chat_template.format_messages(topic="數學", input="什麼是三角函數?")
pprint(message_list)

prompt = ChatPromptTemplate(
        messages=[SystemMessage(content="你是一名醫師"),
                  HumanMessage(content="我生病了"),
                  AIMessage(content="哪裡不舒服")]
)
pprint(prompt)

