import os

from openai import OpenAI

client = OpenAI(
    base_url="https://api.openpike.dev/v1",
    api_key=os.environ["OPENPIKE_API_KEY"],
    default_headers={"x-openpike-tags": "agent=fallback-demo"},
)

raw = client.chat.completions.with_raw_response.create(
    model="openpike/fast",
    messages=[{"role": "user", "content": "Name one river in Europe."}],
)
completion = raw.parse()
print("served by", raw.headers["x-openpike-model"], "after", raw.headers["x-openpike-attempts"], "attempt(s)")
print(completion.choices[0].message.content)
