from fastapi import APIRouter
from src.repository.tasks_repository import TasksRepository

router = APIRouter(
	prefix="/tasks",
	tags=["tasks"],
)

@router.get("")
def get_tasks():
	task_repo = TasksRepository()
	tasks = task_repo.list()
	return tasks

@router.get("/{task_id}")
def get_task(task_id: int):
	task_repo = TasksRepository()
	task = task_repo.get(task_id)
	return task