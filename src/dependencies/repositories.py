from fastapi import Depends
from sqlalchemy.orm import Session

from src.infrastructure.repository.users_repository import UsersRepository
from src.infrastructure.repository.tasks_repository import TasksRepository
from src.infrastructure.db.session import get_session

def get_tasks_repo(
    db_session: Session = Depends(get_session),
) -> TasksRepository:
    return TasksRepository(db_session)

def get_users_repo(
	db_session: Session = Depends(get_session),
) -> UsersRepository:
	return UsersRepository(db_session)