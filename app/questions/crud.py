import logging
from datetime import datetime
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.questions.models import TriviaQuestion
from app.questions.schemas import QuestionSchema


async def get_last_question(db: AsyncSession) -> Optional[TriviaQuestion]:
    """Получить последний вопрос из базы данных."""
    logging.info("Fetching the last trivia question from the database.")
    result = await db.execute(
        select(TriviaQuestion).order_by(TriviaQuestion.insertion_order.desc()).limit(1)
    )
    question = result.scalar_one_or_none()
    if question:
        logging.info(f"Fetched question: {question.id}, {question.question}")
    else:
        logging.info("No questions found in the database.")

    return question


async def save_question(db: AsyncSession, question_data: QuestionSchema) -> None:
    """Сохранить вопрос в базе данных."""
    question = TriviaQuestion(
        id=question_data.id,
        question=question_data.question,
        answer=question_data.answer,
        created_at=datetime.date(question_data.created_at)
    )
    db.add(question)
    await db.commit()
