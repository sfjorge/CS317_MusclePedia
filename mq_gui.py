import PySimpleGUI as sg
from mp_query import Query


result = []
query = Query()

result = query.selectEx()
print(result)

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
workoutText = []
for i in result:
    workoutText.append([sg.Text(i[0])])


layout = [ 
            [sg.Text('Search Muscle'), sg.InputText()],
            [sg.Text('Search Workout'), sg.InputText()],
            workoutText,
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]
        ]

# Create the Window
window = sg.Window('!! MusclePedia !!', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Ok':
        layout = [sg.Text(values[0])]
        print('You entered ', values[0])

window.close()

query.kill()