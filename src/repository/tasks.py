from src.repository.abstract import SQLAlchemyRepository
from src.models.tasks import Tasks

class TasksRepository(SQLAlchemyRepository):
		model = Tasks