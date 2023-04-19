import PySimpleGUI as sg
import random

game_round = 0
d1 = random.randint(1,6)
d2 = random.randint(1,6)
d3 = random.randint(1,6)
d4 = random.randint(1,6)
d5 = random.randint(1,6)

while True:
    game_round += 1
    text = "You throwed the dice and you got:\n"
    text += f" a: {d1}\n b: {d2}\n c: {d3}\n d: {d4}\n e: {d5}\n" 
    if d1 == d2 == d3 == d4 == d5:
        text += "You throwed Yathzee!\n"
    text += "Please enter letters of the dice you want to throw again:"     
    answer = sg.popup_get_text(text, f"game {game_round}")
    answer = answer.lower()
    if "a" in answer:
        d1 = random.randint(1,6)
    if "b" in answer:
        d2 = random.randint(1,6)
    if "c" in answer:
        d3 = random.randint(1,6)
    if "d" in answer:
        d4 = random.randint(1,6)
    if "e" in answer:
        d5 = random.randint(1,6)
    if answer == "quit":
        break

sg.PopupOK("thanks for playing")

   

