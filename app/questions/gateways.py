import httpx

from app.questions.schemas import QuestionSchema


async def fetch_trivia_questions(count: int) -> list[QuestionSchema]:
    """Получить вопросы для викторины из внешнего API."""
    url = f'https://jservice.io/api/random?count={count}'
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            questions = response.json()
            return [QuestionSchema(**question) for question in questions]
    except httpx.HTTPError as e:
        print(f'An error occurred while fetching trivia questions: {e}')
        raise
