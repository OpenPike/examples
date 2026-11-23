import os

from anthropic import Anthropic

client = Anthropic(
    base_url="https://api.openpike.dev",
    api_key=os.environ["OPENPIKE_API_KEY"],
    default_headers={"x-openpike-tags": "agent=anthropic-python"},
)

with client.messages.stream(
    model="anthropic/claude-haiku-5-5",
    max_tokens=200,
    messages=[{"role": "user", "content": "Count from one to five."}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
print()
