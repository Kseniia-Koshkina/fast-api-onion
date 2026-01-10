from fastapi import FastAPI
from src.router.tasks import router as tasks_router

app = FastAPI()

app.include_router(tasks_router)