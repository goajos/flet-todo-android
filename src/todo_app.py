import flet as ft
from task import Task
from todo_android.task_service import create_task, delete_task, get_tasks, update_task


class TodoApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="What's needs to be done!", expand=True)
        self.tasks = ft.Column()
        self.width = 600
        self.controls = [
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD, on_click=self.add_clicked
                    ),
                ]
            ),
            self.tasks,
        ]

    def add_clicked(self, e):
        create_task(self.new_task.value)
        self.refresh_tasks()
        self.new_task.value = ''
        self.update()

    def task_update(self, old_name, new_name):
        update_task(old_name, new_name)
        self.refresh_tasks()
        self.update()

    def task_delete(self, task):
        delete_task(task.task_name)
        self.refresh_tasks()
        self.update()

    def refresh_tasks(self):
        self.tasks.controls.clear()
        tasks = get_tasks()
        for task in tasks:
            self.tasks.controls.append(
                Task(task.name, self.task_delete, self.task_update)
            )
        self.update()
