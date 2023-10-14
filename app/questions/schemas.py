from datetime import datetime

from pydantic import BaseModel


class QuestionRequest(BaseModel):
    """Схема запроса для получения вопросов."""

    questions_num: int

    class Config:
        orm_mode = True


class QuestionSchema(BaseModel):
    """Схема вопроса, содержащая информацию о вопросе для викторины."""

    id: int | None
    question: str | None
    answer: str | None
    created_at: datetime | None

    class Config:
        orm_mode = True
