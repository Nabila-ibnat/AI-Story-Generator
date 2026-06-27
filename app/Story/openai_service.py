from openai import AsyncOpenAI
from app.core.config import settings
from app.utils.prompt_template import build_story_prompt


async def generate_story(prompt: str) -> str:
    """Send prompt to OpenAI and return a generated story."""
    if not settings.OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY is not configured")

    client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
    system_message, user_message = build_story_prompt(prompt)

    response = await client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ],
        max_tokens=settings.MAX_TOKENS,
        temperature=settings.TEMPERATURE,
    )

    story = response.choices[0].message.content.strip()
    return story
