from fastapi import Depends
from sqlalchemy.orm import Session

from src.repository.tasks import TasksRepository
from src.db.session import get_session

def get_tasks_repo(
    db_session: Session = Depends(get_session),
) -> TasksRepository:
    return TasksRepository(db_session)