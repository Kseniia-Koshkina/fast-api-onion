from src.repository.abstract import SQLAlchemyUserRepository
from src.models.users import Users

class UsersRepository(SQLAlchemyUserRepository):
	model = Users