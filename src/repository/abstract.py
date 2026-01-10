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
	def __init__(self, session):
		self.session = session

	def get(self, item_id):
		return self.session.query(self.model).get(item_id)

	def list(self):
		return self.session.query(self.model).all()