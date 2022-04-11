import PySimpleGUI as sg
from mp_query import Query


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
equipmentList = []

def toggleEquipment(equip):
    global equipmentList
    if equip in equipmentList:
        equipmentList.remove(equip)
    elif equip not in equipmentList:
        equipmentList.append(equip)
def equipmentText():
    text = ''
    for eq in equipmentList:
        text = text + eq + ' '
    return text


result = query.selectAllEx()
print(result)

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
workoutText = []
for i in result:
    workoutText.append(sg.Text(i[0]))

# band, 
layout = [
        [sg.Text('Equipment: '), sg.Text(equipmentText(), key='equipText')],
        [sg.Button('Bodyweight'),sg.Button('Dumbells'),sg.Button('Barbells'),sg.Button('Kettlebells'),sg.Button('Bench'),sg.Button('Cables'),sg.Button('Machines')],
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
    elif event == 'Bodyweight' or event == 'Dumbells' or event == 'Barbells' or event == 'Kettlebells' or event == 'Bench' or event == 'Cables' or event == 'Machines':
        toggleEquipment(event)
        window['equipText'].update(equipmentText())
    elif event == 'Muscle Search' and not muscleWindow:
        muscleWindow = makeMuscleWindow(values['muscleIn'], 'This is a description of the bicep muscle. This is a description of the bicep muscle. This is a description of the bicep muscle.')
    elif event == 'Workout Search' and not workoutWindow:
        workoutWindow = makeMuscleWindow(values['workoutIn'], 'A bicep curl is done with a dumbbell where the arm begins extended with the hand holding the weight with a motion of curling the arm.')
window.close()

query.kill()