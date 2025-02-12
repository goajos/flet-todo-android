import flet as ft
from todo_app import TodoApp


def main(page: ft.Page):
    page.padding = ft.padding.only(top=50)
    page.title = 'To-Do App'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo = TodoApp()
    page.add(todo)


ft.app(main)
