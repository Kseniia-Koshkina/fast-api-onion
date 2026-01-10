from src.repository.abstract import AbstractRepository

class TaskService():
	def __init__(self, repository):
		self.repository: AbstractRepository = repository

	def get_task(self, task_id):
		return self.repository.get(task_id)

	def list_tasks(self):
		return self.repository.list()