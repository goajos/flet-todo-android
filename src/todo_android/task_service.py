from typing import List

from .schemas.task_schema import TaskSchema
from .storages.task_storage import TaskStorage

ts = TaskStorage()


def get_tasks() -> List[TaskSchema]:
    return ts.get_tasks()


def create_task(name: str):
    ts.create_task(name)


def update_task(old_name: str, new_name: str):
    ts.update_task(old_name, new_name)


def delete_task(name: str):
    ts.delete_task(name)
