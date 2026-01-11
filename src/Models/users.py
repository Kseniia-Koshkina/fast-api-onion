from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from src.db.base import Base

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String)
    # registered_date: Mapped[Date] = mapped_column(Date)