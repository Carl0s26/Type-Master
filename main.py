import flet as ft
import random as rand

def main(page: ft.Page):
    global words
    global currentWords
    global currentWord
    global correctWords
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = 'Type Master'
    page.window.width = 600
    page.window.height = 800
    page.bgcolor = '#c8eed8'
    page.scroll = True
    page.window.resizable = False
    words = ["Individuo","Sebastian","Varillas","Negativo","Sirve","Ademas","Debido","Circunstancias","Blockeado","Whatsapp","Imagenes","Megabites","Grandes","Projecto","Explosion","Historia","Terminar","Necesito","Multitud","Palabras","Ideas","Pocas","Ayuda","Profe","Esternocleidomastoideo"]
    currentWords = words.copy()
    currentWord = ""
    correctWords = 0

    def on_keyboard(e: ft.KeyboardEvent):
        global correctWords
        global currentWord

        print(e.key)
        if e.key == "Enter":
            print("passed enter")
            if userInput.value == currentWord:  
                print("Is correct")
                correctWords += 1
                score.value = f"Points: {correctWords}"
                colorUpdater(True)
            else:
                print("Is Wrong")
                colorUpdater(False)
                
            acurracyCalculator()
            userInput.value = ""
            nextWord()
        page.update()
        userInput.focus()

    page.on_keyboard_event = on_keyboard

    def colorUpdater(value):
        if value == False:
            print("here")
            status.color = ft.Colors.RED
        else:
            print("Color green")
            status.color = ft.Colors.GREEN

    def acurracyCalculator():
        global correctWords
        global currentWords
        wordstracked.value = f'{(len(words)) - len(currentWords)}/{len(words)-1}'
        if (len(words)) - len(currentWords) != 0:
            print(f"{correctWords},{len(words)} - {len(currentWords)}")
            acurracyLabel.value = f"Accuracy: {int(abs((correctWords / ((len(words)) - len(currentWords))) * 100))}%"

    def retryTest():
        global currentWords
        global correctWords
        currentWords = words.copy()
        status.color = ft.Colors.PINK
        correctWords = 0
        score.value = f"Points: 0"
        nextWord()
        acurracyCalculator()
        userInput.disabled = False
        userInput.value = ""
        acurracyLabel.value = "Start the test to see your acurracy!"
        wordstracked.value= f"0/{len(words)}"
        page.update()

    def nextWord():
        global currentWords
        global currentWord
        global words
        if (len(words)) - len(currentWords) != (len(words)-1):
            print(currentWord)
            randomNum = rand.randint(0,len(currentWords)-1)
            currentWord = currentWords[randomNum]
            wordLabel.value = currentWord
            currentWords.pop(randomNum)
            print(currentWord)
            page.update()
        else:
            userInput.disabled = True
            userInput.value = "You Finished The Test :)"



    title = ft.Text(value="The Typing Test!")
    userInput = ft.TextField()
    score = ft.Text(value="0 Points")
    wordstracked = ft.Text(value=f"0/{len(words)}")
    acurracyLabel = ft.Text("Start the test to see your acurracy!")
    status = ft.Text(value="STATUS")
    wordLabel = ft.Text(value="Current Word")
    retryButton = ft.ElevatedButton(text="Retry",on_click= lambda _: retryTest())


    page.bgcolor = '#c8eed8'
    page.add(title,status,wordstracked,wordLabel,userInput,acurracyLabel,score,retryButton)
    page.update()

    retryTest()
    acurracyLabel.value = "Start the test to see your acurracy!"
ft.app(target=main, assets_dir="assets")
