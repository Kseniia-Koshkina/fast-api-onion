from fastapi import APIRouter, Depends
from src.dependencies.services import get_tasks_service

router = APIRouter(
	prefix="/tasks",
	tags=["tasks"],
)

@router.get("")
def get_tasks(
	task_service = Depends(get_tasks_service)
):
	tasks = task_service.list()
	return tasks

@router.get("/{task_id}")
def get_task(
  task_id: int,
	task_service = Depends(get_tasks_service),
):
	task = task_service.get_task(task_id)
	return task