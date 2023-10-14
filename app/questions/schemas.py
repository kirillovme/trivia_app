from datetime import datetime

from pydantic import BaseModel
from typing import Optional


class QuestionRequest(BaseModel):
    """Схема запроса для получения вопросов."""

    questions_num: int

    class Config:
        orm_mode = True


class QuestionSchema(BaseModel):
    """Схема вопроса, содержащая информацию о вопросе для викторины."""

    id: Optional[int]
    question: Optional[str]
    answer: Optional[str]
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
