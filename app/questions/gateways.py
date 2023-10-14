import httpx
from typing import List, Dict
from app.questions.schemas import QuestionSchema


async def fetch_trivia_questions(count: int) -> List[QuestionSchema]:
    """Получить вопросы для викторины из внешнего API."""
    url = f"https://jservice.io/api/random?count={count}"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)

            # Check if the request was successful
            response.raise_for_status()

            questions = response.json()
            return [QuestionSchema(**question) for question in questions]
    except httpx.HTTPError as e:
        # Log the error and re-raise it or handle it as you prefer
        print(f"An error occurred while fetching trivia questions: {e}")
        raise
