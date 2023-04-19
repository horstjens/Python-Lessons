"""
dicegame1: one button displaying a random number if clicked
"""

import random
import PySimpleGUI as sg

# d1 ... dice number one

layout = [
    [sg.Text("click to play")],
    [sg.Button("?", key="d1", font=("System",64))],
    [sg.Button("Cancel")],
]

window = sg.Window("dice game 1", layout)

while True:
    event, values = window.read()
    if event in ("Cancel", sg.WIN_CLOSED):
        break
    if event == "d1":
        throw = random.randint(1,6)
        window["d1"].update(text=f"{throw}")
window.close()