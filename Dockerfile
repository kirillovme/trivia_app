FROM python:3.10-slim

WORKDIR /trivia_app

ENV PYTHONUNBUFFERED=1

COPY ./poetry.lock ./pyproject.toml ./alembic.ini ./entrypoint.sh ./

RUN pip install poetry==1.6.1

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --no-root --only main

COPY ./app /trivia_app/app
COPY ./alembic /trivia_app/alembic
