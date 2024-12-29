from turtle import Screen

class CreateScreen:
    def __init__(self):
        self.screen = Screen()
        self.createScreen()

    def createScreen(self):
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor('black')
        self.screen.title("The snake game!")
        self.screen.tracer(0)

    def exit_on_click(self):
        self.screen.exitonclick()
