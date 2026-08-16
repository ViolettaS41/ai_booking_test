import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://api.orcarouter.ai/v1",
    api_key=os.environ["ORCAROUTER_API_KEY"],
)

def get_ai_response(text: str, passport_received: bool):
    passport_status = (
        "паспорт получен"
        if passport_received
        else "паспорт не получен"
    )

    messages = [
        {
            "role": "system",
            "content": """
Ты помощник гостя при заселении в отель.

Отвечай вежливо, понятно и кратко.
Учитывай текущий статус паспорта гостя.

Если паспорт не получен, объясни гостю, что сначала
необходимо предоставить паспорт для заселения.
Для предоставления паспорта используй ссылку:
https://example.com/passport

Если паспорт получен, сообщи гостю, что паспорт принят,
и объясни, что следующим этапом будет оплата залога.
"""
        },
        {
            "role": "user",
            "content": f"""
Статус паспорта: {passport_status}

Сообщение гостя:
{text}
"""
        }
    ]

    response = client.chat.completions.create(
        model="deepseek/deepseek-v4-flash-free",
        messages=messages,
    )

    return response.choices[0].message.content

