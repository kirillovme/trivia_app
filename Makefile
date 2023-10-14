SHELL := /bin/bash

up:
	docker compose up

up-d:
	docker compose up -d

down:
	docker compose down

build:
	docker compose build

migrate:
	docker compose exec web alembic upgrade head

makemigrations:
	docker compose exec web alembic revision --autogenerate
