# import PySimpleGUI as sg

# class MainView:
#     def __init__(self, name, desc):
#         sg.theme('DarkAmber')
#         self.name = name
#         self.layout = [
#             [sg.Text(name)],
#             [sg.Text(desc)]
#         ]
#         self.window = sg.Window(name, self.layout)
#     while True:
#         event, values = window.read()
#         if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
#             break