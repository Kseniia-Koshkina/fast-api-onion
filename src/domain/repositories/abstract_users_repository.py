from src.domain.repositories.abstract_repository import AbstractRepository
from abc import abstractmethod

class AbstractUserRepository(AbstractRepository):
	@abstractmethod
	def get_by_username(self, username):
		pass