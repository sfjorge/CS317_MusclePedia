import PySimpleGUI as sg
from mp_query import Query


def makeMuscleWindow(muscle):
    result = []
    temp = query.selectMuscle(muscle)
    print('raw result from selectMuscle: ', temp)
    for m in temp[0]:
        result.append(m)

    layout = [
        [sg.Text(result[0])],
        [sg.Text('Description: '), sg.Text(result[3])]
    ]
    return sg.Window(muscle, layout, location = (400, 200), finalize=True)

def makeWorkoutWindow(workout):
    print('workout', workout)
    result = []
    temp = query.selectExercise(workout)
    print("raw result of selectExercise: ", temp)
    for w in temp[0]:
        if w == None:
            result.append('Bodyweight')
        else:
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
        [sg.Text('Muscles worked out: '), sg.Text(arrToText(muscleTargets))],
        [sg.Button('DELETE EXERCISE!')],
        [sg.Text('Exercise Deleted!', visible = False, key='confirm_delete')]
    ]
    return sg.Window(workout, layout, location=(400,150), finalize=True)

def makeAddWindow():
    layout = [
        [sg.Text('CREATE NEW EXERCISE')],
        [sg.Text('Enter name: '), sg.InputText(key='exName')],
        [sg.Text('Select Equipment:'), sg.Text('', key='equipText_add')],
        [sg.Button('Bodyweight'),sg.Button('Dumbbell'),sg.Button('Barbell'),sg.Button('Kettlebells'),sg.Button('Bench Press'),sg.Button('Cable Machine'),sg.Button('Grip Trainer')],
        [sg.Text('Enter description of exercise:')],
        [sg.Input(size=(80), key="ex_desc")],
        [sg.Text('Select muscles targeted by exercise: ')],
        [sg.Button('Arms'),sg.Button('Back'),sg.Button('Chest'),sg.Button('Core'),sg.Button('Legs')],
        muscleList_add,
        [sg.Button('Clear', visible = False)],
        [sg.Text('Selected muscles: ', key='txt2', visible=False), sg.Text(arrToText(muscles_add), key = 'muscleText_add', visible = False)],
        [sg.Button('ADD EXERCISE!', visible = False)],
        [sg.Text('EXERCISE ADDED!', visible = False, key = 'confirm_add')]
    ]
    return sg.Window('Add New Exercise', layout, location=(400,200), finalize=True)

inputWorkout = ''

result = []
query = Query()
equipmentList = []
equipToAdd = ''

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

def toggleMuscle_add(muscle):
    global muscles_add
    if muscle in muscles_add:
        muscles_add.remove(muscle)
    elif muscle not in muscles_add:
        muscles_add.append(muscle)

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
muscleList = [sg.Listbox(values = [], size=(30,12), key='muscleSelect', enable_events=True, visible = False), sg.Text('These are some \n instructions about \n how to use the \n listbox to the left', visible = False, key='instr')]
muscles = []

muscleList_add = [sg.Listbox(values = [], size=(30,12), key='muscleSelect_add', enable_events=True, visible = False)]
muscles_add = []

searchResults = []
def toggleSearchResults(res):
    global searchResults
    searchResults = []
    for r in res:
        searchResults.append(r[0])

# listbox array from muscles


# band, 
mainLayout = [
        [sg.Text('Search Muscle  '), sg.InputText(key='muscleIn'), sg.Button('Muscle Search')],
        [sg.Text('Search Workout'), sg.InputText(key='workoutIn'), sg.Button('Workout Search')],
        [sg.Text('Add New Workout: '), sg.Button('ADD')],
        [sg.Text('Equipment: '), sg.Text(arrToText(equipmentList), key='equipText')],
        [sg.Button('Bodyweight'),sg.Button('Dumbbell'),sg.Button('Barbell'),sg.Button('Kettlebells'),sg.Button('Bench Press'),sg.Button('Cable Machine'),sg.Button('Grip Trainer')],
        [sg.Text('Pick a muscle group:')],
        [sg.Button('Arms'),sg.Button('Back'),sg.Button('Chest'),sg.Button('Core'),sg.Button('Legs')],
        muscleList,
        [sg.Button('Clear Muscles', visible = False)],
        [sg.Text('Selected muscles: ', key='txt1', visible=False), sg.Text(arrToText(muscles), key = 'muscleText', visible = False)],
        [sg.Button('Search', visible=False)],
        [sg.Text('', key='searchResults')]
    ]

exerciseLayout = [
      
]

# Create the Window
window1, muscleWindow, workoutWindow, addWindow = sg.Window('!! MusclePedia !!', mainLayout, finalize=True, location = (500, 100)), None, None, None
# Event Loop to process "events" and get the "values" of the inputs
while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED: # if user closes window
        window.close()
        if window == muscleWindow:       # if closing win 2, mark as closed
            muscleWindow = None
        elif window == workoutWindow:
            workoutWindow = None
        elif window == addWindow:
            addWindow = None
            muscleList_add = [sg.Listbox(values = [], size=(30,12), key='muscleSelect_add', enable_events=True, visible = False)]
            muscles_add = []
            equipToAdd = ''
        elif window == window1:     # if closing win 1, exit program
            break
    elif event == 'Search':
        res = query.addExerciseWithEquip(equipmentList, muscles)
        toggleSearchResults(res)
        window['searchResults'].update(arrToText(searchResults))
    elif event == 'Bodyweight' or event == 'Dumbbell' or event == 'Barbell' or event == 'Kettlebells' or event == 'Bench Press' or event == 'Cable Machine' or event == 'Grip Trainer':
        if addWindow:
            equipToAdd = event
            window['equipText_add'].update(event)
        else:
            toggleEquipment(event)
            window['equipText'].update(arrToText(equipmentList))
    elif event == 'Muscle Search' and not muscleWindow:
        muscleWindow = makeMuscleWindow(values['muscleIn'])
    elif event == 'Workout Search' and not workoutWindow:
        workoutWindow = makeWorkoutWindow(values['workoutIn'])
        inputWorkout = values['workoutIn']
    elif event == 'ADD' and not addWindow:
        addWindow = makeAddWindow()
    elif event == 'Arms' or event == 'Back' or event == 'Chest' or event == 'Core' or event == 'Legs': ## replace with groupXxxx
        if addWindow:
            window['muscleSelect_add'].update( makeMuscleArray(event), visible = True)
            window['Clear'].update(visible = True)
            window['txt2'].update(visible = True)
            window['muscleText_add'].update(visible = True)
            window['ADD EXERCISE!'].update(visible = True)
        else:
            window['muscleSelect'].update( makeMuscleArray(event), visible = True)
            window['Clear Muscles'].update(visible = True)
            window['txt1'].update(visible = True)
            window['muscleText'].update(visible = True)
            window['Search'].update(visible = True)
            window['instr'].update(visible = True)
    elif event == 'muscleSelect':
        toggleMuscle(values['muscleSelect'][0])
        window['muscleText'].update(arrToText(muscles))
    elif event == 'muscleSelect_add':
        toggleMuscle_add(values['muscleSelect_add'][0])
        window['muscleText_add'].update(arrToText(muscles_add))
    elif event == 'Clear Muscles':
        muscles = []
        window['muscleText'].update(arrToText(muscles))
    elif event == 'Clear':
        muscles_add = []
        window['muscleText_add'].update(arrToText(muscles_add))
    elif event == 'ADD EXERCISE!':
        query.addExercise(values['exName'],equipToAdd, values['ex_desc'], muscles_add)
        window['confirm_add'].update(visible = True)
    elif event == 'DELETE EXERCISE!':
        query.deleteExercise(inputWorkout)
        window['confirm_delete'].update(visible=True)
    print(event)


window.close()

query.kill()