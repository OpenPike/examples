import { createAnthropic } from "@ai-sdk/anthropic";
import { createOpenAI } from "@ai-sdk/openai";
import { generateText, streamText } from "ai";

const headers = { "x-openpike-tags": "agent=vercel-ai-sdk" };

// OpenAI format: OpenPike serves Chat Completions, so use openpike.chat(...), not openpike(...).
const openpike = createOpenAI({
  baseURL: "https://api.openpike.dev/v1",
  apiKey: process.env.OPENPIKE_API_KEY,
  headers,
});

const { text } = await generateText({
  model: openpike.chat("deepseek/deepseek-flash"),
  prompt: "Name one river in Europe.",
});
console.log(text);

// Anthropic format, for Claude models.
const openpikeClaude = createAnthropic({
  baseURL: "https://api.openpike.dev/v1",
  apiKey: process.env.OPENPIKE_API_KEY,
  headers,
});

const result = streamText({
  model: openpikeClaude("anthropic/claude-haiku-5-5"),
  prompt: "Count from one to five.",
});
for await (const delta of result.textStream) process.stdout.write(delta);
process.stdout.write("\n");
