from sqlalchemy import Column, Integer, String, DateTime, func, Sequence, Identity

from app.database import Base


class TriviaQuestion(Base):
    __tablename__ = 'trivia_questions'
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, index=True)
    answer = Column(String)
    insertion_order = Column(Integer, Identity(always=True), nullable=False)
    created_at = Column(DateTime(timezone=True))
