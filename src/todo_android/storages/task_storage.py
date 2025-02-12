from todo_android.models.task_model import TaskModel

from .base_storage import BaseStorage


class TaskStorage(BaseStorage):
    def get_tasks(self):
        session = self.session()
        try:
            tasks = session.query(TaskModel).all()
            return tasks
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
