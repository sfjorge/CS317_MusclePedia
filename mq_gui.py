import PySimpleGUI as sg
from mp_query import Query


def makeMuscleWindow(name, desc):
    layout = [
        [sg.Text(name)],
        [sg.Text(desc)]
    ]
    return sg.Window(name, layout, location = (400, 300), finalize=True)

def makeWorkoutWindow(workout):
    result = []
    temp = query.selectExercise(workout)
    print("raw result of selectExercise: ", temp)
    for w in temp[0]:
        result.append(w)
    print("result: ", result)
    muscleTargets = []
    temp = query.muscleTargetsOfExercise(workout)
    for m in temp:
        muscleTargets.append(m[0])
    print("raw result of muscleTargetsOfExercise: ", temp)
    layout = [
        [sg.Text(result[0])],
        [sg.Text('Equipment needed: '), sg.Text(result[1])],
        [sg.Text(result[2])],
        [sg.Text('Muscles worked out: '), sg.Text(arrToText(muscleTargets))]
    ]
    return sg.Window(workout, layout, location=(400,150), finalize=True)


result = []
query = Query()
equipmentList = []

def toggleEquipment(equip):
    global equipmentList
    if equip in equipmentList:
        equipmentList.remove(equip)
    elif equip not in equipmentList:
        equipmentList.append(equip)
def toggleMuscle(muscle):
    global muscles
    if muscle in muscles:
        muscles.remove(muscle)
    elif muscle not in muscles:
        muscles.append(muscle)

def arrToText(arr):
    text = ''
    for a in arr:
        text = text + a + ', '
    return text
# buttons for selecting individual muscle under muscle group to work out
# logic of IF statements will be replaced with result of query (input would be muscle group and query for selecting muscles)
def makeMuscleArray(group): # was makeMuscleButtons
    # muscles = []
    muscleList = []
    tempArray = query.selectMusclesFromGroup(group)
    for m in tempArray:
        muscleList.append(m[0])
    return muscleList

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.

# array for muscle group layout
muscleGroupButtons = []
muscleGroups = []

# muscleButtons = []
muscleList = [sg.Listbox(values = [], size=(30,12), key='muscleSelect', enable_events=True, visible = False)]
muscles = []

# listbox array from muscles


# band, 
mainLayout = [
        [sg.Text('Search Muscle  '), sg.InputText(key='muscleIn'), sg.Button('Muscle Search')],
        [sg.Text('Search Workout'), sg.InputText(key='workoutIn'), sg.Button('Workout Search')],
        [sg.Text('Equipment: '), sg.Text(arrToText(equipmentList), key='equipText')],
        [sg.Button('Bodyweight'),sg.Button('Dumbells'),sg.Button('Barbells'),sg.Button('Kettlebells'),sg.Button('Bench'),sg.Button('Cables'),sg.Button('Machines')],
        [sg.Text('Pick a muscle group:')],
        [sg.Button('Arms'),sg.Button('Back'),sg.Button('Chest'),sg.Button('Core'),sg.Button('Legs')],
        muscleList,
        [sg.Button('Clear Muscles', visible = False)],
        [sg.Text('Selected muscles: ', key='txt1', visible=False), sg.Text(arrToText(muscles), key = 'muscleText', visible = False)],
        [sg.Button('Search', visible=False)],
        [sg.Text(size=(12,1), key='muscleOut')],
        [sg.Text(size=(12,1), key='workoutOut')]
    ]

exerciseLayout = [
    
]

# Create the Window
window1, muscleWindow, workoutWindow = sg.Window('!! MusclePedia !!', mainLayout, finalize=True, location = (500, 100)), None, None
# Event Loop to process "events" and get the "values" of the inputs
while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED: # if user closes window
        window.close()
        if window == muscleWindow:       # if closing win 2, mark as closed
            muscleWindow = None
        elif window == workoutWindow:
            workoutWindow = None
        elif window == window1:     # if closing win 1, exit program
            break
    elif event == 'Search':
        window1['muscleOut'].update(values['muscleIn'])
        window1['workoutOut'].update(values['workoutIn'])
    elif event == 'Bodyweight' or event == 'Dumbells' or event == 'Barbells' or event == 'Kettlebells' or event == 'Bench' or event == 'Cables' or event == 'Machines':
        toggleEquipment(event)
        window['equipText'].update(arrToText(equipmentList))
    elif event == 'Muscle Search' and not muscleWindow:
        muscleWindow = makeMuscleWindow(values['muscleIn'], 'This is a description of the bicep muscle. This is a description of the bicep muscle. This is a description of the bicep muscle.')
    elif event == 'Workout Search' and not workoutWindow:
        workoutWindow = makeWorkoutWindow(values['workoutIn'])
    elif event == 'Arms' or event == 'Back' or event == 'Chest' or event == 'Core' or event == 'Legs': ## replace with groupXxxx
        window['muscleSelect'].update( makeMuscleArray(event), visible = True)
        window['Clear Muscles'].update(visible = True)
        window['txt1'].update(visible = True)
        window['muscleText'].update(visible = True)
        window['Search'].update(visible = True)
    elif event == 'muscleSelect':
        toggleMuscle(values['muscleSelect'][0])
        window['muscleText'].update(arrToText(muscles))
    elif event == 'Clear Muscles':
        muscles = []
        window['muscleText'].update(arrToText(muscles))


window.close()

query.kill()