from weakref import finalize
import PySimpleGUI as sg
from mp_query import Query
from muslce_view import MuscleView


def makeMuscleWindow(name, desc):
    layout = [
        [sg.Text(name)],
        [sg.Text(desc)]
    ]
    return sg.Window(name, layout, location = (400, 300), finalize=True)

def makeWorkouteWindow(name, desc):
    layout = [
        [sg.Text(name)],
        [sg.Text(desc)]
    ]
    return sg.Window(name, layout, location=(800,600), finalize=True)


result = []
query = Query()
# muscle pages
# musclesOpened = []
# # workout pages
# workoutsOpened = []



result = query.selectEx()
print(result)

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
workoutText = []
for i in result:
    workoutText.append(sg.Text(i[0]))


layout = [ 
            [sg.Text('Search Muscle'), sg.InputText(key='muscleIn'), sg.Button('Muscle Search')],
            [sg.Text('Search Workout'), sg.InputText(key='workoutIn'), sg.Button('Workout Search')],
            [sg.Text('Query for ex_name below:')],
            workoutText,
            [sg.Button('Ok'), sg.Button('Cancel')],
            [sg.Text(size=(12,1), key='muscleOut')],
            [sg.Text(size=(12,1), key='workoutOut')]
        ]

# Create the Window
window1, muscleWindow, workoutWindow = sg.Window('!! MusclePedia !!', layout, finalize=True), None, None
# Event Loop to process "events" and get the "values" of the inputs
while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        window.close()
        if window == muscleWindow:       # if closing win 2, mark as closed
            muscleWindow = None
        elif window == workoutWindow:
            workoutWindow = None
        elif window == window1:     # if closing win 1, exit program
            break
    elif event == 'Ok':
        window1['muscleOut'].update(values['muscleIn'])
        window1['workoutOut'].update(values['workoutIn'])
    elif event == 'Muscle Search' and not muscleWindow:
        muscleWindow = makeMuscleWindow(values['muscleIn'], 'This is a description of the bicep muscle. This is a description of the bicep muscle. This is a description of the bicep muscle.')
    elif event == 'Workout Search' and not workoutWindow:
        workoutWindow = makeMuscleWindow(values['workoutIn'], 'A bicep curl is done with a dumbbell where the arm begins extended with the hand holding the weight with a motion of curling the arm.')
window.close()

query.kill()