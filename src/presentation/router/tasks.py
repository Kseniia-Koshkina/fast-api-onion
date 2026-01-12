from fastapi import APIRouter, Depends
from ..schema.tasks import TaskAddSchema
from src.dependencies.services import get_tasks_service
from src.application.services.tasks_service import TaskService

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

@router.post("")
def create_task(
	task_data: TaskAddSchema,
	task_service: TaskService = Depends(get_tasks_service),
):
    task = task_service.create_task(task_data)
    return task.id

@router.delete("/{task_id}")
def delete_task(
	task_id: int,
	task_service: TaskService = Depends(get_tasks_service),
):
	task = task_service.delete_task(task_id)
	return task.id