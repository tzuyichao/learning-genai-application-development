import os
from dotenv import load_dotenv
import openai

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = openai.OpenAI(
        api_key=OPENAI_API_KEY
)

chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": "I had 25 eggs. I gave away 12. I now have "
            }
        ],
        max_tokens=1,
        temperature=0,
        logprobs=True
)

print(chat_completion)
