"""
dicegame3: display 5 buttons in a row, showing dice faces
include a "throw all" button
"""

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
    [sg.Button("?", key="d1", font=("System",64)),
     sg.Button("?", key="d2", font=("System",64)),
     sg.Button("?", key="d3", font=("System",64)),
     sg.Button("?", key="d4", font=("System",64)),
     sg.Button("?", key="d5", font=("System",64)),     
    ],
    [sg.Button("Cancel"), sg.Button("throw dice")],
]

window = sg.Window("dicegame 3", layout)

while True:
    event, values = window.read()
    if event in ("Cancel", sg.WIN_CLOSED):
        break
    if event in ("d1","d2","d3","d4","d5"):
        throw = random.randint(1,6)
        window[event].update(text=f"{codes[throw]}")
    if event == "throw dice":
        for w in ("d1","d2","d3","d4","d5"):
            throw = random.randint(1,6)
            window[w].update(text=f"{codes[throw]}")
window.close()

