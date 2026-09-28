from ai_client import generate_text


def get_learning_recommendations(
    topic: str
) -> str:

    prompt = f"""
You are EduGenie, an AI learning assistant.

Create a personalized learning path
for a student who wants to learn:

{topic}

Organize the learning journey from
beginner level to advanced level.

Include:

1. Learning goal

2. Beginner topics

3. Intermediate topics

4. Advanced topics

5. Suggested timeline

6. Practice activities

7. Revision strategy

8. Recommended resource types
   such as videos, articles,
   documentation and books

Make the plan practical and easy
for a student to follow.

Do not invent URLs.
"""


    try:

        return generate_text(
            prompt
        )

    except Exception as error:

        return (
            "Unable to create the learning path "
            "right now.\n\n"
            f"Error: {error}"
        )