from langchain.prompts import PromptTemplate
from rich import print as pprint

prompt_template = PromptTemplate(template="告訴我一個關於{topic}的知識",
                                 input_variables=["topic"])

pprint(prompt_template)

prompt_string = prompt_template.format(topic="貓咪")
print(prompt_string)

prompt_value = prompt_template.invoke({"topic": "貓咪"})
pprint(prompt_value)
print(f"prompt_string: {type(prompt_string)}, \n"
      f"prompt_value: {type(prompt_value)}")
