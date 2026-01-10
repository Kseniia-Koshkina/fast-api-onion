from fastapi import APIRouter, Depends
from src.dependencies.services import get_tasks_service
from src.services.tasks import TaskService

router = APIRouter(
	prefix="/tasks",
	tags=["tasks"],
)

@router.get("")
def get_tasks(
	task_service: TaskService = Depends(get_tasks_service)
):
	tasks = task_service.list_tasks()
	return tasks

@router.get("/{task_id}")
def get_task(
  task_id: int,
	task_service: TaskService = Depends(get_tasks_service),
):
	task = task_service.get_task(task_id)
	return task