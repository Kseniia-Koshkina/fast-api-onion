from src.application.services.users_service import UserService
from src.application.services.tasks_service import TaskService
from src.dependencies.repositories import get_tasks_repo, get_users_repo
from fastapi import Depends

def get_tasks_service(
	tasks_repository = Depends(get_tasks_repo),
):
    return TaskService(tasks_repository)

def get_users_service(
	users_repository = Depends(get_users_repo),
):
	return UserService(users_repository)