from src.domain.repositories.abstract_repository import AbstractRepository
from sqlalchemy.orm import Session

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
