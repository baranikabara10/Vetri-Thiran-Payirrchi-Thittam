import json
import re

from ai_client import generate_text


def clean_json_block(text: str) -> str:

    text = text.strip()


    # Remove ```json
    text = re.sub(
        r"^```(?:json)?\s*",
        "",
        text,
        flags=re.IGNORECASE
    )


    # Remove ```
    text = re.sub(
        r"\s*```$",
        "",
        text
    )


    return text.strip()


def validate_quiz(data):

    if not isinstance(data, list):

        raise ValueError(
            "Quiz response must be a list."
        )


    validated = []


    for item in data[:3]:

        if not isinstance(item, dict):

            continue


        question = str(
            item.get("question", "")
        ).strip()


        options = item.get(
            "options",
            []
        )


        answer = str(
            item.get("answer", "")
        ).strip()


        explanation = str(
            item.get("explanation", "")
        ).strip()


        if not question:

            continue


        if not isinstance(options, list):

            continue


        if len(options) != 4:

            continue


        options = [
            str(option).strip()
            for option in options
        ]


        if answer not in options:

            continue


        validated.append({

            "question": question,

            "options": options,

            "answer": answer,

            "explanation": explanation

        })


    if len(validated) != 3:

        raise ValueError(
            "Gemini did not return "
            "exactly three valid questions."
        )


    return validated


def generate_quiz(text: str):

    prompt = f"""
Create exactly 3 multiple-choice questions
from the educational content below.

Return ONLY valid JSON.

Do not use Markdown.

Use exactly this structure:

[
  {{
    "question": "Question",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "answer": "Correct option",
    "explanation": "Short explanation"
  }}
]

Rules:

- Exactly 3 questions.
- Exactly 4 options per question.
- Only one correct answer.
- The answer must exactly match one option.
- Questions must be based on the supplied content.
- Make distractors realistic.
- Use simple student-friendly language.

Educational content:

{text}
"""


    try:

        response = generate_text(
            prompt
        )


        cleaned = clean_json_block(
            response
        )


        data = json.loads(
            cleaned
        )


        questions = validate_quiz(
            data
        )


        return {
            "questions": questions
        }


    except Exception as error:

        return {
            "error":
                f"Quiz generation failed: {error}"
        }