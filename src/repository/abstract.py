from abc import ABC, abstractmethod
from src.db.session import get_session

class AbstractRepository(ABC):
	# @abstractmethod
	# def add(self, item):
	# 	pass

	@abstractmethod
	def get(self, item_id):
		pass

	@abstractmethod
	def list(self):
		pass

class SQLAlchemyRepository(AbstractRepository):
	model = None

	# def add(self, item):
	# 	self.session.add(item)
	# 	self.session.commit()
	# 	return item

	def get(self, item_id):
		session = get_session()
		return session.query(self.model).get(item_id)

	def list(self):
		session = get_session()
		return session.query(self.model).all()