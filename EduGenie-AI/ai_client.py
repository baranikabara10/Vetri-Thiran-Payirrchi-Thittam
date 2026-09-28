import os
from functools import lru_cache

from dotenv import load_dotenv


load_dotenv()


# Gemini model
MODEL_NAME = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)


@lru_cache(maxsize=1)
def get_client():

    api_key = os.getenv(
        "GEMINI_API_KEY",
        ""
    ).strip()

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. "
            "Please add your Gemini API key to the .env file."
        )

    try:

        from google import genai

    except ImportError:

        raise RuntimeError(
            "google-genai package is not installed. "
            "Run: pip install -r requirements.txt"
        )

    client = genai.Client(
        api_key=api_key
    )

    return client


def generate_text(prompt: str) -> str:

    client = get_client()

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    text = getattr(
        response,
        "text",
        None
    )

    if not text:

        raise RuntimeError(
            "Gemini returned an empty response."
        )

    return text.strip()