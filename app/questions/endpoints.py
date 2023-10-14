import logging
import traceback

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.questions.crud import get_last_question, save_question
from app.questions.gateways import fetch_trivia_questions
from app.questions.schemas import QuestionSchema, QuestionRequest

router = APIRouter()


@router.post("/questions/", response_model=QuestionSchema)
async def get_and_save_question(request: QuestionRequest, db: AsyncSession = Depends(get_db)) -> QuestionSchema:
    """Получить и сохранить вопросы для викторины."""
    logging.info("Receiving a request to fetch and save trivia questions.")

    try:
        last_question = await get_last_question(db)
    except Exception as e:
        logging.error(f"An error occurred while fetching the last trivia question: {e}\n{traceback.format_exc()}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    try:
        questions = await fetch_trivia_questions(request.questions_num)
    except Exception as e:
        logging.error(
            f"An error occurred while fetching trivia questions from the external API: {e}\n{traceback.format_exc()}")
        raise HTTPException(status_code=500, detail="Failed to fetch trivia questions.")

    for question_data in questions:
        try:
            await save_question(db, question_data)
        except Exception as e:
            logging.error(f"An error occurred while saving a trivia question: {e}\n{traceback.format_exc()}")
            raise HTTPException(status_code=500, detail="Failed to save trivia question.")

    return last_question
