import logging
import traceback

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.questions.crud import get_last_question, save_questions, question_exists
from app.questions.gateways import fetch_trivia_questions
from app.questions.models import TriviaQuestion
from app.questions.schemas import QuestionRequest, QuestionSchema

router = APIRouter()


@router.post('/questions/', response_model=QuestionSchema | None)
async def get_and_save_question(request: QuestionRequest, db: AsyncSession = Depends(get_db)) -> TriviaQuestion | None:
    """Получить и сохранить вопросы для викторины."""
    logging.info('Receiving a request to fetch and save trivia questions.')
    try:
        last_question = await get_last_question(db)
    except Exception as e:
        logging.error(f'An error occurred while fetching the last trivia question: {e}\n{traceback.format_exc()}')
        raise HTTPException(status_code=500, detail='Internal Server Error')
    try:
        unique_question_received = False
        while not unique_question_received:
            questions = await fetch_trivia_questions(request.questions_num)
            for question in questions:
                if not await question_exists(db, question.id):
                    unique_question_received = True
                    break
            if not unique_question_received:
                logging.warning('Received a non-unique question. Fetching again.')

        await save_questions(db, questions)
    except Exception as e:
        logging.error(f'An error occurred while saving trivia questions: {e}\n{traceback.format_exc()}')
        raise HTTPException(status_code=500, detail='Failed to save trivia questions.')
    return last_question
