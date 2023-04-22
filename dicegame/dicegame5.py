"""
dicegame5: display 5 buttons in a row, showing dice faces
include a "throw dice" button
allows locking/unlocking of each die button 
play three dice throws per game round
play 13 game rounds
hide/display buttons for 'start new game' and 'start next game round'
"""

import random
import PySimpleGUI as sg

game_round = 1
game_rounds = 13
throws_per_round = 3
throw_number = 0  

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
    [sg.Text("starting game round 1 of 13.", key="game_round_counter"),
     sg.Text("throw #1 of 3", key="throw_counter")],
    [sg.Text("Click buttons to toggle lock, click 'throw dice' to play")],
    [sg.Button("?", key="d1", disabled=True, font=("System",64)),
     sg.Button("?", key="d2", disabled=True, font=("System",64)),
     sg.Button("?", key="d3", disabled=True, font=("System",64)),
     sg.Button("?", key="d4", disabled=True, font=("System",64)),
     sg.Button("?", key="d5", disabled=True, font=("System",64)),     
    ],
    [sg.Button("Cancel"),
     sg.Button("start next game round", visible=False),
     sg.Button("start new game", visible=False),
     sg.Button("throw dice")],
]

window = sg.Window("dicegame version 5", layout)

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
    
    if event == "start new game":
        game_round = 1
        throw_number = 0
        window["start new game"].update(visible=False)

    if event in ( "start next game round", "start new game"):
        #throw_number is already set to 0
        for d in locked.keys():
            locked[d] = False
            window[d].update(text="?")
            window[d].update(disabled=True)
            window[d].update(button_color = (color1, color2)) # not locked
        window["start next game round"].update(visible=False)
        window["throw dice"].update(visible=True)
        window["throw_counter"].update( value=f"throw # {throw_number+1} of {throws_per_round}")
        window["game_round_counter"].update(value=f"starting Game round {game_round} of {game_rounds}.")
    
    if event == "throw dice":
        throw_number += 1
        window["throw_counter"].update(value=f"throw # {throw_number} of {throws_per_round}")
        window["game_round_counter"].update(value=f"Game round {game_round} of {game_rounds}.")
        if throw_number == 1:
            for d in locked.keys():
                locked[d] = False
                window[d].update(disabled=False)
                window[d].update(button_color = (color1, color2)) # not locked
        
        # throw all not-locked dice
        for d in locked.keys():
            if locked[d]:
                continue
            throw = random.randint(1,6)
            window[d].update(text=f"{codes[throw]}")

        if throw_number == throws_per_round:
            for d in locked.keys():
                locked[d] = True
                window[d].update(button_color = (color1, color2)) # not locked
                window[d].update(disabled=True)
            throw_number = 0
            game_round += 1
            if game_round > game_rounds:
                window["start new game"].update(visible=True)
                window["start next game round"].update(visible=False)
            else:
                window["start next game round"].update(visible=True)
            window["throw dice"].update(visible=False)

window.close()
sg.PopupOK("Game over")