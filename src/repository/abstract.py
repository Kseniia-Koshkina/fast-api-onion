from abc import ABC, abstractmethod
from sqlalchemy import select
from sqlalchemy.orm import Session

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

class AbstractUserRepository(AbstractRepository):
	@abstractmethod
	def get_by_username(self, username):
		pass

class SQLAlchemyRepository(AbstractRepository):
	model = None

	def __init__(self, session):
		self.session: Session = session

	def get(self, item_id):
		return self.session.query(self.model).get(item_id)

	def list(self):
		return self.session.query(self.model).all()

	def create(self, item_data):
		new_item = self.model(**item_data.dict())
		self.session.add(new_item)
		return new_item

	def delete(self, item_id):
		item = self.get(item_id)
		if item:
			self.session.delete(item)
		return item

class SQLAlchemyUserRepository(SQLAlchemyRepository, AbstractUserRepository):
	def get_by_username(self, username):
		stmt = select(self.model).where(self.model.username == username)
		return self.session.execute(stmt).scalar_one_or_none()