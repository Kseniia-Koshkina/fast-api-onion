from src.repository.abstract_repository import SQLAlchemyRepository
from src.models.tasks import Tasks

class TasksRepository(SQLAlchemyRepository):
		model = Tasks