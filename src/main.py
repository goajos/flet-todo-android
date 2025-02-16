import flet as ft
from todo_app import TodoApp


def main(page: ft.Page):
    page.padding = ft.padding.only(top=50)
    page.title = 'To-Do App'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo1 = TodoApp()
    todo2 = TodoApp()

    def refresh_tasks(e):
        tab = e.control.tabs[int(e.data)]
        tab.content.refresh_tasks()
        page.update()

    tabs = ft.Tabs(
        tabs=[
            ft.Tab(
                text='To-Do 1',
                content=todo1,
            ),
            ft.Tab(
                text='To-Do 2',
                content=todo2,
            ),
        ],
        on_click=refresh_tasks,
    )

    page.add(tabs)

    # load in the persisted tasks
    # todo1.refresh_tasks()
    # todo2.refresh_tasks()


ft.app(main)
