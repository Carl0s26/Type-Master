import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = 'Game & Slice'
    page.window.width = 600
    page.window.height = 800
    page.bgcolor = '#c8eed8'
    page.scroll = True
    page.window.resizable = False

    words = [""]
    title = ft.Text(label="Hello Word")
    userInput = ft.TextField()
    presicionLabel = ft.Text()
    wordLabel = ft.Text(label="Current Word")



    page.add(title,userInput,presicionLabel,wordLabel)
    page.update()
ft.app(target=main, assets_dir="assets")
