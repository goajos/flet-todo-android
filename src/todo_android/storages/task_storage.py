from typing import List

from todo_android.models.task_model import TaskModel
from todo_android.schemas.task_schema import TaskSchema

from .base_storage import BaseStorage


class TaskStorage(BaseStorage):
    def get_tasks(self) -> List[TaskSchema]:
        session = self.session()
        try:
            tasks = session.query(TaskModel).all()
            return [TaskSchema.model_validate(task) for task in tasks]
        except Exception as e:
            raise e
        finally:
            session.close()

    def create_task(self, name: str):
        session = self.session()
        try:
            task = TaskModel(name=name)
            session.add(task)
            session.commit()
            return TaskSchema.model_validate(task)
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def update_task(self, old_name, new_name: str):
        session = self.session()
        try:
            task = session.query(TaskModel).filter_by(name=old_name).first()
            task.name = new_name
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete_task(self, name: str):
        session = self.session()
        try:
            task = session.query(TaskModel).filter_by(name=name).first()
            session.delete(task)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
