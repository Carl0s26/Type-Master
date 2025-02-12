import flet as ft



def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = 'Game & Slice'
    page.window.width = 600
    page.window.height = 800
    page.bgcolor = '#c8eed8'
    page.scroll = True
    page.window.resizable = False

    def on_keyboard(e: ft.KeyboardEvent):
        print(e.key)

        page.update()

    page.on_keyboard_event = on_keyboard

    def colorUpdater(label,value):
        pass

    def acurracyCalculator(label,correctWords,WordsShown):
        pass

    

    words = [""]
    title = ft.Text(value="Hello Word")
    userInput = ft.TextField()
    acurracyLabel = ft.Text()
    wordLabel = ft.Text(value="Current Word")



    page.bgcolor = '#c8eed8'
    page.add(title,userInput,acurracyLabel,wordLabel)
    page.update()
ft.app(target=main, assets_dir="assets")
