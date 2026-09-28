import os

from ai_client import generate_text


def explain_topic(topic: str) -> str:

    # Optional local LaMini model
    use_local = os.getenv(
        "USE_LOCAL_EXPLANATION",
        "false"
    ).lower() == "true"

    if use_local:

        try:

            return local_explanation(topic)

        except Exception:

            # If local model fails,
            # use Gemini instead.
            pass


    prompt = f"""
You are EduGenie.

Explain the following topic to a beginner.

Topic:

{topic}

Use the following structure:

1. Meaning
2. How it works
3. Simple example
4. Important points

Requirements:

- Use very simple language.
- Avoid unnecessary technical words.
- Make it easy for a student to understand.
- Keep the explanation reasonably short.
"""

    try:

        return generate_text(prompt)

    except Exception as error:

        return (
            "Unable to explain the topic right now.\n\n"
            f"Error: {error}"
        )


def local_explanation(topic: str) -> str:

    from transformers import pipeline


    model_name = os.getenv(
        "LOCAL_EXPLANATION_MODEL",
        "MBZUAI/LaMini-Flan-T5-783M"
    )


    generator = pipeline(
        "text2text-generation",
        model=model_name,
        tokenizer=model_name
    )


    prompt = f"""
Explain this educational topic in simple language.

Topic:
{topic}

Include:
- Meaning
- How it works
- Example
- Key points
"""


    result = generator(
        prompt,
        max_new_tokens=300,
        do_sample=False
    )


    return result[0][
        "generated_text"
    ].strip()