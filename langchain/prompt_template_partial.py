from langchain.prompts import PromptTemplate, ChatPromptTemplate
from rich import print as pprint

prompt = PromptTemplate(template="試著以{role}的角度, "
                                 "告訴我一個關於{topic}的知識",
                        input_variables=['role', 'topic'])

pprint(prompt)

partial_prompt = prompt.partial(topic="洗手")

pprint(partial_prompt)

print(partial_prompt.format(role="老師對兒童"))

prompt2 = PromptTemplate(template="試著以{role}的角度, "
                                  "告訴我一個關於{topic}的知識",
                         input_variables=['role'],
                         partial_variables={'topic': '洗手'})

pprint(prompt2)

chat_template = ChatPromptTemplate.from_messages(
        [
            ("system", "試著以{role}的角度說明"),
            ("human", "告訴我一個關於{topic}的知識"),
        ]
)

pprint(chat_template)

partial_chat_template = chat_template.partial(topic="洗手")
pprint(partial_chat_template)

print(partial_chat_template.format(role="老師對兒童"))
