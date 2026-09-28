from ai_client import generate_text


def summarize_text(text: str) -> str:

    prompt = f"""
You are EduGenie, an educational assistant.

Summarize the following educational passage.

Requirements:

- Keep the important information.
- Remove unnecessary repetition.
- Use simple language.
- Make it useful for quick revision.
- Use bullet points when useful.
- Do not add information that is not present.
- Keep the main meaning unchanged.

Educational passage:

{text}
"""


    try:

        return generate_text(
            prompt
        )

    except Exception as error:

        return (
            "Unable to summarize the text right now.\n\n"
            f"Error: {error}"
        )