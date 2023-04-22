"""
dicegame6: display 5 buttons in a row, showing dice faces
include a "throw dice" button
allows locking/unlocking of each die button 
play three dice throws per game round
play 13 game rounds
hide/display buttons for 'start new game' and 'start next game round'
show and update score table
player must choose one option after each game round
give maximum points for each option
"""

import random
import PySimpleGUI as sg

def play_option(selected_option):
    '''function to update score_table
       returns the maximum value of a selected option
    '''
    for i, line in enumerate(score_table):
        # column index:
        # 0     1       2        3
        name, score, possible, maximum = line 
        if name != selected_option:
            continue  # go back to start of the for loop
        # update column score so that it has the value of maximum score
        score = maximum
        score_table[i][1] = score
        # update column possible with an empty string
        score_table[i][2] = ""
        # update total score in last row
        score_table[-1][1] += score
        return score # return the value of 'score' 
    return 0 # return 0 in case selected_option was not found

game_round = 1
game_rounds = 13
throws_per_round = 3
throw_number = 0 
game_score = 0

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

# a list of list to display name of option, achived score, possible score, maximum score
score_table = [
    ["Ones",0,0,5],
    ["Twos",0,0,10],
    ["Threes",0,0,15],
    ["Fours",0,0,20],
    ["Fives",0,0,25],
    ["Sixes",0,0,30],
    ["          sum upper section",0,"",105],
    ["          upper sectoin bonus",0,"",35],
    ["Three Of A Kind",0,0,30],
    ["Four Of A Kind",0,0,30],
    ["Full House",0,0,25],
    ["Small Straight",0,0,30],
    ["Large Straight",0,0,40],
    ["Yahtzee",0,0,50],
    ["Chance",0,0,30],
    ["          sum lower section",0,"",235],
    ["          Yahtzee bonus",0,"","100 x 12"],
    ["          Score",0,"",""],
    ]


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
    [sg.Table(score_table, headings=["option","score","possible","maximum"],
            select_mode = sg.TABLE_SELECT_MODE_BROWSE,
            cols_justification=["l","r","r","r"],
            alternating_row_color = "#888888",
            #enable_events = True,
            key="table1", num_rows=18)],
    #[sg.Button("Ones"),sg.Button("Twos"),sg.Button("Threes"),sg.Button("Fours"),
    # sg.Button("Fives"),sg.Button("Sixes")],
    #[sg.Button("Three Of A Kind"), sg.Button("Four of a Kind"), sg.Button("Full House")],
    #[ sg.Button("Small Straight"), sg.Button("Large Straight"), sg.Button("Yahtzee"),
    # sg.Button("Chance")],
    [sg.Button("Select", disabled=True), sg.Text("Click a row in the table above with an number in the column 'possible',  then click 'Select'")],
    [sg.Button("Cancel"),
     sg.Button("start next game round", visible=False),
     sg.Button("start new game", visible=False),
     sg.Button("throw dice")],
]

window = sg.Window("dicegame version 6", layout)

while True:
    event, values = window.read()
    if event in ("Cancel", sg.WIN_CLOSED):
        break
    #print(event, values)
    
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
    
    if event == "Select":
        # check if a row was selected in table1
        if values["table1"] == []:
            sg.PopupError("You must select a row in the table")
            continue
        # check if the selected row is illegal (has empty string in the field possible)
        row = values["table1"][0]
        if score_table[row][2] == "":
            sg.PopupError("You must select a row in the table where the field possible has a number")
            continue        
        # give maximum score and put empty stirng into field possible:
        line = score_table[row]  # selected line in score table
        play_option(line[0])     # line[0] is the name of the played option
        # update table1 widget with the new score_table
        window["table1"].update(score_table)
        # prepare GUI for next game / game round
        window["start new game"].update(disabled=False)
        window["start next game round"].update(disabled=False)
        window["Select"].update(disabled=True)

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
            # disable buttons until Select is clicked
            window["start new game"].update(disabled=True)
            window["start next game round"].update(disabled=True)
            window["Select"].update(disabled=False)

window.close()
sg.PopupOK("Game over")
