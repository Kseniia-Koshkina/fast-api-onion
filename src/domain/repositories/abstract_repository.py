from abc import ABC, abstractmethod

class AbstractRepository(ABC):
	@abstractmethod
	def create(self, item):
		pass

	@abstractmethod
	def get(self, item_id):
		pass

	@abstractmethod
	def list(self):
		pass

	@abstractmethod
	def delete(self, item_id):
		pass