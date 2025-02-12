import flet as ft
from todo_android.storages import BaseStorage

storage = BaseStorage()

def main(page: ft.Page):
    storage.get_session()
    storage.close()

    page.add(ft.Text(value="Hello, World!"))

ft.app(main)