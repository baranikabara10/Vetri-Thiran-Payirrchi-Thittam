from ai_client import generate_text


def answer_question(question: str) -> str:

    prompt = f"""
You are EduGenie, a friendly educational AI assistant.

Answer the student's question accurately and clearly.

Rules:

- Use simple student-friendly language.
- Keep the answer concise but useful.
- Explain difficult terms.
- Give an example when appropriate.
- Do not invent information.
- If the question is unclear, mention the assumption.

Student question:

{question}
"""

    try:

        return generate_text(prompt)

    except Exception as error:

        return (
            "Unable to answer the question right now.\n\n"
            f"Error: {error}"
        )