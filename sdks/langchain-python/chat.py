import os

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="deepseek/deepseek-flash",
    base_url="https://api.openpike.dev/v1",
    api_key=os.environ["OPENPIKE_API_KEY"],
    default_headers={"x-openpike-tags": "agent=langchain-python"},
)

reply = llm.invoke("Name one river in Europe.")
print(reply.content)
