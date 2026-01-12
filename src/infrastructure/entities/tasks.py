from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from ..db.base import Base

class TasksEntity(Base):
	__tablename__ = "tasks"

	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str] = mapped_column(String)