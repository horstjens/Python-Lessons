"""
dicegame4: display 5 buttons in a row, showing dice faces
include a "throw all" button
allows locking/unlocking of each die button 
"""

import random
import PySimpleGUI as sg

color1 = sg.theme_button_color_text()
color2 = sg.theme_button_color_background()
color3 = sg.theme_background_color()

codes = {1:"\u2680",
         2:"\u2681",
         3:"\u2682",
         4:"\u2683",
         5:"\u2684",
         6:"\u2685",
         }

locked = {"d1":False,
          "d2":False,
          "d3":False,
          "d4":False,
          "d5":False}

layout = [
    [sg.Text("click buttons to toggle lock, click 'throw dice' to play")],
    [sg.Button("?", key="d1", font=("System",64)),
     sg.Button("?", key="d2", font=("System",64)),
     sg.Button("?", key="d3", font=("System",64)),
     sg.Button("?", key="d4", font=("System",64)),
     sg.Button("?", key="d5", font=("System",64)),     
    ],
    [sg.Button("Cancel"), sg.Button("throw dice")],
]

window = sg.Window("dicegame 4", layout)

while True:
    event, values = window.read()
    if event in ("Cancel", sg.WIN_CLOSED):
        break
    if event in locked.keys():
        # toggle lock
        locked[event] = not locked[event]
        if locked[event]:
            window[event].update(button_color=(color1,color3) )
        else:
            window[event].update(button_color=(color1,color2) )        
    if event == "throw dice":
        # throw all not-locked dice
        for d in locked.keys():
            if locked[d]:
                continue
            throw = random.randint(1,6)
            window[d].update(text=f"{codes[throw]}")
window.close()