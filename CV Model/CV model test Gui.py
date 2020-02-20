import PySimpleGUI as sg
import json
import BirdTypes

bird_types = BirdTypes.bird_types

layout = [
    [sg.Text('Choose File path')],
    [sg.Combo(bird_types, key='_bird_chosen_', size=(120, 1), readonly=True)], 
    [sg.Button('GO')]
]

window = sg.Window("Test Bird CV", layout)
while True:
    event, values = window.Read(timeout=0)
    if event in (None, ""):
        break
    elif event == 'GO':
        # do CV thing here
        break