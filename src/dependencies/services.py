from src.repository.tasks import TasksRepository
from src.services.tasks import TaskService
from src.dependencies.repositories import get_tasks_repo
from fastapi import Depends

def get_tasks_service(
	tasks_repository = Depends(get_tasks_repo),
):
    return TaskService(tasks_repository)