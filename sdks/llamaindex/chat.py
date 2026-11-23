import os

from llama_index.core.llms import ChatMessage
from llama_index.llms.openai_like import OpenAILike

llm = OpenAILike(
    model="deepseek/deepseek-flash",
    api_base="https://api.openpike.dev/v1",
    api_key=os.environ["OPENPIKE_API_KEY"],
    is_chat_model=True,
    context_window=128000,
    default_headers={"x-openpike-tags": "agent=llamaindex"},
)

reply = llm.chat([ChatMessage(role="user", content="Name one river in Europe.")])
print(reply.message.content)
