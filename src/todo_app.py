import flet as ft
from task import Task


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
        task = Task(self.new_task.value, self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ''
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()
