import os
import time

from openai import APIStatusError, OpenAI

client = OpenAI(
    base_url="https://api.openpike.dev/v1",
    api_key=os.environ["OPENPIKE_API_KEY"],
    default_headers={
        "x-openpike-tags": "agent=runaway-demo",
        "x-openpike-run": f"runaway-demo-{int(time.time())}",
        "x-openpike-run-label": "Deliberate loop",
    },
)

for attempt in range(1, 201):
    try:
        client.chat.completions.create(
            model="deepseek/deepseek-flash",
            max_tokens=16,
            messages=[{"role": "user", "content": "Reply with the word ok."}],
        )
        print(f"request {attempt}: ok")
    except APIStatusError as error:
        print(f"request {attempt}: stopped with {error.status_code} {error.code}")
        break
    time.sleep(0.2)
