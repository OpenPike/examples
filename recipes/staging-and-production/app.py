import os

from openai import OpenAI

client = OpenAI(
    base_url="https://api.openpike.dev/v1",
    api_key=os.environ["OPENPIKE_API_KEY"],
    default_headers={"x-openpike-tags": f"agent=my-service,env={os.environ.get('APP_ENV', 'staging')}"},
)

reply = client.chat.completions.create(
    model="deepseek/deepseek-flash",
    messages=[{"role": "user", "content": "Name one river in Europe."}],
)
print(reply.choices[0].message.content)
