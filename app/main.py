from fastapi import FastAPI

from app.questions import endpoints

app = FastAPI()

app.include_router(endpoints.router)
