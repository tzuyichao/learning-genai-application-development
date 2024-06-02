import os
from dotenv import load_dotenv
from rich import print as pprint
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

response = client.chat.completions.create(
        model='gpt-4-vision-preview',
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "圖片裡有甚麼?"},
                    {
                        "type": "image_url", 
                        "image_url": {
                            "url": "https://flagtech.github.io/F3762/images/cat1.jpg",
                            "detail": "high"
                        }
                    }
                ]
            }
        ],
        max_tokens=1000
)

pprint(response)
pprint(response.choices[0])
