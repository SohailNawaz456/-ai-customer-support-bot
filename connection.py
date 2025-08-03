import os
from dotenv import load_dotenv
from agents import (
    OpenAIChatCompletionsModel,
    AsyncOpenAI,
    RunConfig,
    set_tracing_disabled
)

# Load .env file
load_dotenv()
set_tracing_disabled(disabled=True)

# Load Gemini API key
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise Exception("GEMINI_API_KEY is not set in .env file")

# Create Gemini-compatible OpenAI client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Define Gemini model using OpenAI-compatible wrapper
model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True  # ✅ صحیح: "tracing_disabled"
)
