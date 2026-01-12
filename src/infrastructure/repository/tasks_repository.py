from ..repository.sqlalchemy_repository import SQLAlchemyRepository
from ..entities.tasks import TasksEntity

class TasksRepository(SQLAlchemyRepository):
	model = TasksEntity