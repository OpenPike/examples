import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  baseURL: "https://api.openpike.dev",
  apiKey: process.env.OPENPIKE_API_KEY,
  defaultHeaders: { "x-openpike-tags": "agent=anthropic-typescript" },
});

const stream = client.messages.stream({
  model: "anthropic/claude-haiku-5-5",
  max_tokens: 200,
  messages: [{ role: "user", content: "Count from one to five." }],
});
stream.on("text", (text) => process.stdout.write(text));
await stream.finalMessage();
process.stdout.write("\n");
