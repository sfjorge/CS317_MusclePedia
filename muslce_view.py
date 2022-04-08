import PySimpleGUI as sg

class MuscleView:
    def __init__(self, name, desc):
        sg.theme('DarkAmber')
        self.name = name
        layout = [
            [sg.Text(name)],
            [sg.Text(desc)]
        ]
        self.window = sg.Window(name, layout)