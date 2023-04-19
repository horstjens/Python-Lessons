import PySimpleGUI as sg
import random

game_round = 0
while True:
    game_round += 1
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    d4 = random.randint(1,6)
    d5 = random.randint(1,6)
    
    text = f"You throwed the dice and you got:\n {d1} {d2} {d3} {d4} {d5}\n" 
    
    if d1 == d2 == d3 == d4 == d5:
        text += "You throwed Yathzee!\n"
    text += "Do you want to throw the dice again?"
    answer = sg.PopupYesNo(text, title= f"game {game_round}")
    if answer == "No":
        break
sg.PopupOK("thanks for playing")    

