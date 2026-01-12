from fastapi import FastAPI
from src.presentation.router.tasks import router as tasks_router
from src.presentation.router.auth import router as auth_router

app = FastAPI()

app.include_router(tasks_router)
app.include_router(auth_router)