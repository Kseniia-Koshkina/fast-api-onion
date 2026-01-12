from ..repository.sqlalchemy_user_repository import SQLAlchemyUserRepository
from ..entities.users import UsersEntity

class UsersRepository(SQLAlchemyUserRepository):
	model = UsersEntity