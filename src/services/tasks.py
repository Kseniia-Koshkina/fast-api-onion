from src.repository.abstract import AbstractRepository

class TaskService():
	def __init__(self, repository):
		self.repository: AbstractRepository = repository

	def get_task(self, task_id):
		return self.repository.get(task_id)

	def list_tasks(self):
		return self.repository.list()

	def create_task(self, task_data):
		new_task = self.repository.create(task_data)
		return new_task.id

	def delete_task(self, task_id):
		return self.repository.delete(task_id)