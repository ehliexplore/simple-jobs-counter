from datetime import date
import PySimpleGUI as sg
from PySimpleGUI import *
from calls_archive import *

file = 'file.txt'
today = date.today()

data_dict = {'october 27': 22,
'november 1': 30,
'november 2': 80,
'november 3': 26}

print(today)

if fileexist(file):
    pass
else:
    createfile(file)

theme('DarkPurple')
headings = ['Date', 'Jobs']

layout = [
    [Text('CALL CENTER SAC JOBS COUNTER')],
    [Text('Hour 1: '), Input(key='hour1')],
    [Text('Hour 2: '), Input(key='hour2')],
    [Text('Hour 3: '), Input(key='hour3')],
    [Text('Hour 4: '), Input(key='hour4')],
    [Text('Hour 5: '), Input(key='hour5')],
    [Text('Hour 6: '), Input(key='hour6')],
    [Button('Save')],
    [Text('Total:', key='show_total')],
    [Button('Show Data')],
    [Text('', key='-SHOW-')]
    ]

screen = sg.Window('CALLS', layout, element_justification='c')

jobs = list()

while True:
    jobs.clear()
    events, values = screen.read()
    if events == sg.WINDOW_CLOSED:
        break
    if events == 'Save':
        jobs.append(int(values['hour1']))
        jobs.append(int(values['hour2']))
        jobs.append(int(values['hour3']))
        jobs.append(int(values['hour4']))
        jobs.append(int(values['hour5']))
        jobs.append(int(values['hour6']))
        total = sum(jobs)
        screen['show_total'].update(f'Total: {total} jobs saved')
        save(file, today, total)
    if events == 'Show Data':
        screen['-SHOW-'].update(data_dict)

screen.close()
