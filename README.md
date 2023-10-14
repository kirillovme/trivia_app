# Trivia App

## Описание проекта

Trivia App - это приложение на FastAPI для получения вопросов для викторины. Приложение взаимодействует с внешним API для получения вопросов, проверяет их на уникальность и сохраняет в базу данных PostgreSQL.

## Установка

Клонируйте репозиторий:

```bash
git clone https://github.com/kirillovme/trivia_app.git
```

Перейдите в директорию проекта:

```bash
cd trivia_app
```

### Используя Docker

Соберите и запустите контейнеры Docker:

```bash
make up
```

или запустите в фоновом режиме:

```bash
make up-d
```


## Использование

Доступ к приложению:

```
http://localhost:8000
```

Получение и сохранение вопросов для викторины:

```http
POST /questions/
```

## Пример работы

Запрос к пустой базе:
![First Request](https://cdn.discordapp.com/attachments/800849536540868642/1162885321260814356/first_request.png?ex=653d9059&is=652b1b59&hm=133f4d70836145bcd3d7ea28b50a18a63cd5088a592518d276e0750da958d1be&)

Запрос к непустой базе:
![First Request](https://cdn.discordapp.com/attachments/800849536540868642/1162885333097136279/next_request.png?ex=653d905c&is=652b1b5c&hm=5df41df3a1f8aa0d56f16be3b0c2889333b195f82ad48f32021fd29de2b4d53e&)

## Использование Makefile

- `make up`: Запустить проект
- `make up-d`: Запустить проект в фоновом режиме
- `make down`: Остановить проект
- `make build`: Собрать Docker контейнеры
- `make migrate`: Применить миграции базы данных
- `make makemigrations`: Создать новые миграции базы данных