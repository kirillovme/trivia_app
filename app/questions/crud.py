import logging

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.questions.models import TriviaQuestion
from app.questions.schemas import QuestionSchema


async def get_last_question(db: AsyncSession) -> TriviaQuestion | None:
    """Получить последний вопрос из базы данных."""
    logging.info('Fetching the last trivia question from the database.')
    result = await db.execute(
        select(TriviaQuestion).order_by(TriviaQuestion.insertion_order.desc()).limit(1)
    )
    question = result.scalar_one_or_none()
    if question:
        logging.info(f'Fetched question: {question.id}, {question.question}')
    else:
        logging.info('No questions found in the database.')
    return question


async def question_exists(db: AsyncSession, question_id: int) -> bool:
    """Проверка на существование вопроса в базе."""
    result = await db.execute(
        select(TriviaQuestion).filter(TriviaQuestion.id == question_id)
    )
    question = result.scalar_one_or_none()
    return question is not None


async def save_questions(db: AsyncSession, questions_data: list[QuestionSchema]) -> None:
    """Сохранить вопрос в базе данных."""
    new_questions = []
    for question_data in questions_data:
        question = TriviaQuestion(
            id=question_data.id,
            question=question_data.question,
            answer=question_data.answer,
            created_at=question_data.created_at
        )
        new_questions.append(question)
    if new_questions:
        db.add_all(new_questions)
        await db.commit()
