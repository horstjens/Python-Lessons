# dicegame2: one button showing a die when clicked

import random
import PySimpleGUI as sg

# unicode for dice faces, see https://en.wikipedia.org/wiki/Miscellaneous_Symbols
codes = {1:"\u2680",
         2:"\u2681",
         3:"\u2682",
         4:"\u2683",
         5:"\u2684",
         6:"\u2685",
         }

layout = [
    [sg.Text("click to play")],
    [sg.Button("?", key="d1", font=("System",64), tooltip="click me")],
    [sg.Button("Cancel")],
]

window = sg.Window("dice game 2", layout)

while True:
    event, values = window.read()
    if event in ("Cancel", sg.WIN_CLOSED):
        break
    if event == "d1":
        throw = random.randint(1,6)
        window["d1"].update(text=f"{codes[throw]}")
window.close()

