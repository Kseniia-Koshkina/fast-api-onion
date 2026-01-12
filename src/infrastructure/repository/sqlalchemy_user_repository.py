from src.domain.repositories.abstract_users_repository import AbstractUserRepository
from src.infrastructure.repository.sqlalchemy_repository import SQLAlchemyRepository
from sqlalchemy import select

class SQLAlchemyUserRepository(SQLAlchemyRepository, AbstractUserRepository):
	def get_by_username(self, username):
		stmt = select(self.model).where(self.model.username == username)
		return self.session.execute(stmt).scalar_one_or_none()