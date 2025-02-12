from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class TaskModel(Base):
    __tablename__ = 'exercise_templates'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
