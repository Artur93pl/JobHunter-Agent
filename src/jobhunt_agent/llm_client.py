# Thin wrapper around the Anthropic Claude API client

import os

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()  # reads .env and loads its values into the environment

# Cheapest, fastest current model - good for development and testing.
MODEL = "claude-haiku-4-5"


def get_client() -> Anthropic:
    """Create an Anthropic client using the API key from .env."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError(
            "ANTHROPIC_API_KEY not found. Did you create a .env file? "
            "See .env.example for the format."
        )
    return Anthropic(api_key=api_key)


def say_hello() -> str:
    """A minimal test call - proves the API connection works."""
    client = get_client()
    response = client.messages.create(
        model=MODEL,
        max_tokens=100,
        messages=[{"role": "user", "content": "Say hello in one short sentence."}],
    )
    return response.content[0].text
