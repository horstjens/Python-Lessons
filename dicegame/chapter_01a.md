# prototype and GUI

To start with programming a Yathzee game, let's define what the program should do:

*  simulate throwing 5 dice
*  let the player keep some dice / throw some dice  (3 throws per game round)
*  keep track of game round and throws
*  ask player to choose an option and keep track of played options
*  show the player which options they can play and how many points they will get. This includes:
    * recognizing if the player throwed a specific option (full house, large straight etc.)
    * calculating the amount of points the player would get for each option
        * include special rules such a joker rule (yathzee can act as a joker under certain conditions)
*  keep track of points, calculate sum of points at the end of the game (13 game rounds)
    * calculate upper score bonus and yathzee bonus

In this tutorial, the prototype will be constructed in python, without any third party libraries.

## GUI 

If the prototype works (all game rules are applied correctly etc.) a Graphical User Interface (GUI) will be created. There exist several options of how to build a GUI, but most of them need a third party library that must be installed. This tutorial will use the PySimpleGUI library.

# step one: throwing 5 dice

To simulate the throwinf of 5 dice, it is necessary to use Python's bulit-in [random](https://docs.python.org/3/library/random.html) module. 

The [random.randint()](https://docs.python.org/3/library/random.html#random.randint) function creates a random integer:

    random.randint(a, b)
    Return a random integer N such that a <= N <= b. 

Because we need 5 random numbers (to simulate the 5 dice) we will store those 5 numbers in a list with the name `dicelist`:
This is done by first creating an empty list and then putting values into this list using the [.append()](https://docs.python.org/3/tutorial/datastructures.html?highlight=append#more-on-lists) method of lists. This is done 5 times inside a [for loop](https://docs.python.org/3/tutorial/controlflow.html?highlight=loops#for-statements), using the [range](https://docs.python.org/3/library/stdtypes.html?highlight=range#range) command:

[dicegame00.py](dicegame00.py)
```python
import random
dicelist = []                            # create an empty list 
for _ in range(5):                       # repeat 5 times
    dicelist.append(random.randint(1,6))  
print(dicelist)                          # example: [4,2,2,1,3]
```

output:

    [6, 1, 6, 1, 4]

things done:

~~simulate throwing 5 dice~~

# step two: keep / throw dice, keep track of throws & game round

The nerdy solution would be to ask the player of the indexes of dicelist of the dice they want to keep. But indexes in Python start with 0, and the indexes as well as the values of the dice are numbers, so this is a bit confusing. 
Better to represent each die with an letter (a-e) and ask the player to enter the letters of the dice they want to keep:

[dicegame01.py](dicegame01.py)
```python
import random

history = []
dicelist = []
for _ in range(5):    
    dicelist.append(random.randint(1,6))  
        
for game_round in range(1,14):   # 13 game rounds 
    for throw in range(1,4):     # 3 throws
        print(f"throw: {throw} of 3, game round: {game_round} of 13")
        print(" a  b  c  d  e")
        print(dicelist)
        if throw == 3:
            text = "" if game_round == 13 else "to start next game round:"
            command = input(f"press ENTER {text} >>>")
            command = ""
            history.append(dicelist[:])  # append a COPY of dicelist to played
        else:
            command = input("Enter letter(s) to keep: >>>").lower() 
        
        if not "a" in command:
            dicelist[0] = random.randint(1,6)
        if not "b" in command:
            dicelist[1] = random.randint(1,6)
        if not "c" in command:
            dicelist[2] = random.randint(1,6)
        if not "d" in command:
            dicelist[3] = random.randint(1,6)
        if not "e" in command:
            dicelist[4] = random.randint(1,6)  
print("Game Over")  
print("game round,  result")
for game_round, result in enumerate(history, 1):
    print(f"{game_round:>5} : {result}" )
```

output:

    ...
    press ENTER to start next game round: >>>
    throw: 1 of 3, game round: 12 of 13
     a  b  c  d  e
    [2, 3, 5, 1, 4]
    Enter letter(s) to keep: >>>abcde
    throw: 2 of 3, game round: 12 of 13
     a  b  c  d  e
    [2, 3, 5, 1, 4]
    Enter letter(s) to keep: >>>abcde
    throw: 3 of 3, game round: 12 of 13
     a  b  c  d  e
    [2, 3, 5, 1, 4]
    press ENTER to start next game round: >>>
    throw: 1 of 3, game round: 13 of 13
     a  b  c  d  e
    [2, 2, 4, 2, 1]
    Enter letter(s) to keep: >>>abd
    throw: 2 of 3, game round: 13 of 13
     a  b  c  d  e
    [2, 2, 3, 2, 3]
    Enter letter(s) to keep: >>>abcde
    throw: 3 of 3, game round: 13 of 13
     a  b  c  d  e
    [2, 2, 3, 2, 3]
    press ENTER  >>>
    Game Over
    game round,  result
        1 : [1, 5, 3, 6, 6]
        2 : [3, 2, 1, 4, 4]
        3 : [6, 1, 4, 3, 3]
        4 : [3, 4, 5, 2, 1]
        5 : [2, 5, 2, 3, 2]
        6 : [5, 4, 6, 4, 5]
        7 : [6, 3, 1, 1, 4]
        8 : [6, 1, 5, 3, 3]
        9 : [2, 2, 3, 6, 2]
       10 : [1, 5, 3, 4, 3]
       11 : [5, 2, 1, 6, 4]
       12 : [2, 3, 5, 1, 4]
       13 : [2, 2, 3, 2, 3]

*  ~~simulate throwing 5 dice~~
*  ~~let the player keep some dice / throw some dice  (3 throws per game round)~~
*  ~~keep track of game round and throws~~

# step three: ask player to choose an option and keep track of played options

To offer the player an option to play at each game round, we need to have all options stored in some kind of data structure, like a list:

```python
options = ["Full House", "Small Straight", "Large Straight", ] # etc. 
```

Because we need to keep track of which option was played and the score of each option, a dictinary is a better data structure. (There exist other possibilities, like using a DataClass). The name of the options serve as the _keys_ of this dictionary. The _values_ of this dictionary are empty dictionaries, so that we have a nested dictionary:

```python
#           keys:            values:
options = {                          # upper section:
           "Ones":            {},
           "Twos":            {},
           "Threes":          {},
           "Fours":           {},
           "Fives":           {},
           "Sixes":           {},
                                     # lower section
           "Three Of A Kind": {},
           "Four Of A Kind":  {},
           "Full House":      {},
           "Small Straight":  {},
           "Large Straight":  {},
           "Yathzee":         {},
           "Chance":          {},
           }
```

The Yathzee simulation must keep track of played options and also about how many points each played option archived. 

Sadly, the number zero can not be used to indicate if an option was played, because in Yathzee it is possible to play an option but get zero points for it. (This happens usually at the end of the game when all easy to reach options are played and the player is forced to "use up" one of the remaining options).

One solution would be to keep track of the score for each option by using Python's special value of `None` to indicate that an option was not yet played, and otherwise write an integer (including zero) to indicate that the option was played.

What key-values pairs to put into the "inner" dictionary that is empty at the moment?

  * a key with the name "played", value is either `True` or `False`
  * a key with the name "scored", value is an integer 
  * a key with the name "possible", value is an integer. <br>The purpose of this is to indicate to the player how much points they would get by choosing this option.
  * a key with the name "maximum", value is an integer. <br>The purpose of this is to indicate to the player how much points they could get in an optimal case for this option. (The optimal case is usually to have a Yathzee).

Let's update the _options_ dictionary:

```python
#           keys:            values:
options = {                          # upper section:
           "Ones":            {"played":False, "scored":0, "possible": 0, "maximum":5},
           "Twos":            {"played":False, "scored":0, "possible": 0, "maximum":10},
           "Threes":          {"played":False, "scored":0, "possible": 0, "maximum":15},
           "Fours":           {"played":False, "scored":0, "possible": 0, "maximum":20},
           "Fives":           {"played":False, "scored":0, "possible": 0, "maximum":25},
           "Sixes":           {"played":False, "scored":0, "possible": 0, "maximum":30},
                                     # lower section
           "Three Of A Kind": {"played":False, "scored":0, "possible": 0, "maximum":30},
           "Four Of A Kind":  {"played":False, "scored":0, "possible": 0, "maximum":30},
           "Full House":      {"played":False, "scored":0, "possible": 0, "maximum":25},
           "Small Straight":  {"played":False, "scored":0, "possible": 0, "maximum":30},
           "Large Straight":  {"played":False, "scored":0, "possible": 0, "maximum":40},
           "Yathzee":         {"played":False, "scored":0, "possible": 0, "maximum":50},
           "Chance":          {"played":False, "scored":0, "possible": 0, "maximum":30},
           }
```

The complete program updates the _options_ dictionary and always gives the maximum score:

[dicegame02.py](dicegame02.py)

```python
import random

history = []
dicelist = []
options = {                          # upper section:
           "Ones":            {"played":False, "scored":0, "possible": 0, "maximum":5},
           "Twos":            {"played":False, "scored":0, "possible": 0, "maximum":10},
           "Threes":          {"played":False, "scored":0, "possible": 0, "maximum":15},
           "Fours":           {"played":False, "scored":0, "possible": 0, "maximum":20},
           "Fives":           {"played":False, "scored":0, "possible": 0, "maximum":25},
           "Sixes":           {"played":False, "scored":0, "possible": 0, "maximum":30},
                                     # lower section
           "Three Of A Kind": {"played":False, "scored":0, "possible": 0, "maximum":30},
           "Four Of A Kind":  {"played":False, "scored":0, "possible": 0, "maximum":30},
           "Full House":      {"played":False, "scored":0, "possible": 0, "maximum":25},
           "Small Straight":  {"played":False, "scored":0, "possible": 0, "maximum":30},
           "Large Straight":  {"played":False, "scored":0, "possible": 0, "maximum":40},
           "Yathzee":         {"played":False, "scored":0, "possible": 0, "maximum":50},
           "Chance":          {"played":False, "scored":0, "possible": 0, "maximum":30},
           }

for _ in range(5):    
    dicelist.append(random.randint(1,6))  

for game_round in range(1,14):   # 13 game rounds 
    for throw in range(1,4):     # 3 throws
        print(f"throw: {throw} of 3, game round: {game_round} of 13")
        print(" a  b  c  d  e")
        print(dicelist)
        if throw == 3:
            text = "" if game_round == 13 else "to start next game round:"
            unplayed = [name for name in options.keys() if not options[name]["played"]]
            print("Your options are:", unplayed)
            while True:    
                command = input(f"type the (exact!) name of option to play {text} >>>")
                if command not in unplayed:
                    if command in options.keys():
                        print("You already used this option, please try again")
                    else:
                        print("Unknow option , please try again") 
                    continue
                break    
            # an option was choosen. Mark as played and give maximum score
            points = options[command]["maximum"]
            print(f"You play {command} and get the maximum number of points: {points}")
            # update dictionary
            options[command]["played"] = True
            options[command]["scored"] = points
            command = ""
            history.append(dicelist[:])  # append a COPY of dicelist to history
        else:
            command = input("Enter letter(s) to keep: >>>").lower() 
        
        if not "a" in command:
            dicelist[0] = random.randint(1,6)
        if not "b" in command:
            dicelist[1] = random.randint(1,6)
        if not "c" in command:
            dicelist[2] = random.randint(1,6)
        if not "d" in command:
            dicelist[3] = random.randint(1,6)
        if not "e" in command:
            dicelist[4] = random.randint(1,6)  
print("Game Over")  
print("game round,  result")
for game_round, result in enumerate(history, 1):
    print(f"{game_round:>5} : {result}" )
```

output:

    throw: 1 of 3, game round: 1 of 13
     a  b  c  d  e
    [5, 4, 6, 5, 6]
    Enter letter(s) to keep: >>>bde
    throw: 2 of 3, game round: 1 of 13
     a  b  c  d  e
    [1, 4, 4, 5, 6]
    Enter letter(s) to keep: >>>bde
    throw: 3 of 3, game round: 1 of 13
     a  b  c  d  e
    [6, 4, 2, 5, 6]
    Your options are: ['Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', 'Three Of A Kind', 'Four Of A Kind', 'Full House', 'Small Straight', 'Large Straight', 'Yathzee', 'Chance']
    type the (exact!) name of option to play to start next game round: >>>Sixes
    You play Sixes and get the maximum number of points: 30
    throw: 1 of 3, game round: 2 of 13
     a  b  c  d  e
    [4, 1, 2, 5, 5]
    Enter letter(s) to keep: >>>de
    throw: 2 of 3, game round: 2 of 13
     a  b  c  d  e
    [3, 6, 5, 5, 5]
    Enter letter(s) to keep: >>>cde
    throw: 3 of 3, game round: 2 of 13
     a  b  c  d  e
    [4, 5, 5, 5, 5]
    Your options are: ['Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Three Of A Kind', 'Four Of A Kind', 'Full House', 'Small Straight', 'Large Straight', 'Yathzee', 'Chance']
    type the (exact!) name of option to play to start next game round: >>>5    
    Unknow option , please try again
    type the (exact!) name of option to play to start next game round: >>>Fives
    You play Fives and get the maximum number of points: 25
    

If you read the output above you will notice the the list of playable options is shrinking after each game round: After the player plays "Sixes", the option "Sixes" does not appear anymore in the list.

Typing in the exact name of the option is not very userfriendly. An menu with letters (like to choose the dice to keep) would be a solution, but this is only a prototype - no time to waste for user comfort! It's the job of GUI (see next chapters) to make the user experience as comfortable as possible.

Let's update the TODO list:

*  ~~simulate throwing 5 dice~~
*  ~~let the player keep some dice / throw some dice  (3 throws per game round)~~
*  ~~keep track of game round and throws~~
*  ~~ask player to choose an option and keep track of played options~~
*  ~~show the player which options they can play~~ and how many points they will get. 

# step four: calculate points for each option

This is by far the most complex step. To calculate how many points each option will give it is first necessary to recoginise if the conditions for an option are met by the numbers inside _dicelist_. A second step is to calculate how many points the option would bring, because only a few options bring a fixed amount of points.

Let's start by defining a few functions to test if dicelist meets the conditions for a certain option. Those functions will return either `True` (if the conditions are met) or `False`. 

It is generally a good idea to prefix names of functions that return an _boolean value_ with an "is": A function to test if dicelist is a a "Full house" should be ideally named: _is_full_house()_. This indicates that the function will return either `True` or `False`.  
By tradition, function names should always be written in lowercase. A space in a function name is not allowed and therefore replaced with an underscore. Names with underscore in it are called _snake_case_ because they resembles a snake on road after a car drove over it. To learn more about naming your functions, read the [Python Style Guide Pep8](https://peps.python.org/pep-0008/).

## function to test for "Three Of A Kind"

To test if dicelist is a "Three of a kind", a function could use the `.count()` functionality of lists:

```python
def is_three_of_a_kind(dicelist):
    for number in dicelist:
        if dicelist.count(number) >= 3:
            return True
    return False
```

Note that "Three of a kind" is also always True for an "Yathzee" and "Four of a kind".


## function to test for "Four Of A Kind"

The `.count()` functionality of lists can also be used to detect "Four of A Kind". Note that "Yathzee" is always automatically a "Four of a Kind" as well.

```python
def is_four_of_a_kind(dicelist):
    for number in dicelist:
        if dicelist.count(number) >= 4:
            return True
    return False
```

## function to test for "Full House"

A full house is defined as dicelist having 2 equal numbers and 3 (different) equal numbers. In other words, only 2 different numbers exist inside dicelist, one of them occuring three times, one of them occuring 2 times.

By creating a [set](https://docs.python.org/3/tutorial/datastructures.html#sets) out of _dicelist_ and putting it into a variable _diceset_, we get a set with all numbers that occur in dicelist. There are no duplicate values in a set. In a _Full House_, only tow different numbers exist at all. By iterating over those numbers, we can _count_ how often they exist in dicelist. If one number of a Full House exsit twice, the ohter number must exist three times - and vice versa.

```python
def is_full_house(dicelist):
    diceset = set(dicelist)
    if len(diceset) == 2:
        for number in diceset:
            if dicelist.count(number) in (2,3):
                return True
    return False
```

## function to test for "Small Straight"

A small straight is defines as dicelist having the those numbers: [1,2,3,4] or [2,3,4,5] or [3,4,5,6]. 


Sets offer functionality to test if one set is a superset or a subset of another set. In other words, it is very easy to test if all numbers inside of a small set also exist in a bigger set.

```python 
def is_small_straight(dicelist):
    diceset = set(dicelist)
    if any((diceset >= {1,2,3,4}, 
            diceset >= {2,3,4,5},
            diceset >= {3,4,5,6})):
        return True
    return False
``` 

## function to test for "Large Straight"

Very similar to the code above:

```python 
def is_large_straight(dicelist):
    diceset = set(dicesetcelist)
    if any((diceset >= {1,2,3,4,5}, 
            diceset >= {2,3,4,5,6})):
        return True
    return False
``` 

## function to test for "Yathzee"

The most simple version is to compare all numbers using the `==` operator:

```python
def is_yathzee(dicelist):
    return dicelist[0] == dicelist[1] == dicelist[2] == dicelist[3] == dicelist[4]
    
```

But it also works using a set. The advantage of using a set in this case is that we will not need to change the code if we change the game rules by (for example) adding a sixth die.


``` python
def is_yathzee(dicelist):
    return len(set(dicelist)) == 1
```

## function to calculate score

Now what is missing is a function to calculate the score for a given dicelist and a given option.

Remember that we already wrote a dictionary with the name _options_ so that we can iterate over all options by using `options.keys()`. The first six options (the "upper section") are very easy to calculate: Just look how often the desired number occurs in dicelist, and multiply the result by that number.

For example, if dicelist contains Two time the number 6 and the player choose to play "Sixes", the calculation is `2 x 6 = 12` points.

The score for the options "Three of a kind", "Four of a kind" and "Chance" is  also very easy to calculate: just take the sum of all dice in dicelist. Python provides a `sum()` functions for lists, so we can code `score = sum(dicelist)`.
We have of course to check first if the dicelist is a "Three Of A Kind" or a "Four Of A Kind".

The scores for "Full House", "Small Straight", "Large Straight" and "Yathzee" are fixed with 25, 30, 40 and 50 points ... if the dicelist is one of those options. 

Finally, there is the joker rule:
If a Yathzee was already played AND scored with 50 points AND another Yathzee is thrown AND this Yathzee can not be played in the corresponding field of the upper section anymore THEN this Yathzee acts as a joker for "Small Straight", "Large Straight" and "Full House", giving 30, 40 or 25 points.




```python
def calculate_score(dicelist, name_of_option):
    # joker rule?
    joker = False
    if all((is_yathzee(dicelist),
            options["Yathzee"]["scored"] == 50,
            options[dicelist[0]-1]["played"] is True)):
        joker = True
    # upper section 
    if name_of_option in list(options.keys())[:6]: # Ones, Tows, ... Sixes
        number = list(options.keys()).index(name_of_option) + 1 # 
        return dicelist.count(number) * number
    # lower section 
    if name_of_option == "Three Of A Kind":
        return sum(dicelist) if  is_three_of_a_kind(dicelist) else 0
    if name_of_option == "Four Of A Kind":
        return sum(dicelist) if is_four_of_a_kind(dicelist) else 0
    if name_of_option == "Full House":
        return 25 if (is_full_house(dicelist) or joker) else 0
    if name_of_option == "Small Straight":
        return 30 if (is_small_straight(dicelist) or joker) else 0
    if name_of_option == "Large Straight":
        return 40 if (is_large_straight(dicelist) or joker) else 0
    if name_of_option == "Yathzee":
        return 50 if is_yathzee(dicelist) else 0
    if name_of_option == "Chance":
        return sum(dicelist)
```

## merging all those functions together

[dicegame03.py](dicegame03.py)

```python
import random


def is_three_of_a_kind(dicelist):
    for number in dicelist:
        if dicelist.count(number) >= 3:
            return True
    return False

def is_four_of_a_kind(dicelist):
    for number in dicelist:
        if dicelist.count(number) >= 4:
            return True
    return False

def is_full_house(dicelist):
    diceset = set(dicelist)
    if len(diceset) == 2:
        for number in diceset:
            if dicelist.count(number) in (2,3):
                return True
    return False

def is_small_straight(dicelist):
    diceset = set(dicelist)
    if any((diceset >= {1,2,3,4}, 
            diceset >= {2,3,4,5},
            diceset >= {3,4,5,6})):
        return True
    return False

def is_large_straight(dicelist):
    diceset = set(dicelist)
    if any((diceset >= {1,2,3,4,5}, 
            diceset >= {2,3,4,5,6})):
        return True
    return False

def is_yathzee(dicelist):
    return len(set(dicelist)) == 1

def calculate_score(dicelist, name_of_option):
    # joker rule?
    joker = False
    upper_name = list(options.keys())[dicelist[0]-1]
    if all((is_yathzee(dicelist),
            options["Yathzee"]["scored"] == 50,
            options[upper_name]["played"] is True)):
        joker = True
    # upper section 
    if name_of_option in list(options.keys())[:6]: # Ones, Tows, ... Sixes
        number = list(options.keys()).index(name_of_option) + 1 # 
        return dicelist.count(number) * number
    # lower section 
    if name_of_option == "Three Of A Kind":
        return sum(dicelist) if  is_three_of_a_kind(dicelist) else 0
    if name_of_option == "Four Of A Kind":
        return sum(dicelist) if is_four_of_a_kind(dicelist) else 0
    if name_of_option == "Full House":
        return 25 if (is_full_house(dicelist) or joker) else 0
    if name_of_option == "Small Straight":
        return 30 if (is_small_straight(dicelist) or joker) else 0
    if name_of_option == "Large Straight":
        return 40 if (is_large_straight(dicelist) or joker) else 0
    if name_of_option == "Yathzee":
        return 50 if is_yathzee(dicelist) else 0
    if name_of_option == "Chance":
        return sum(dicelist)

history = []
dicelist = []
options = {                          # upper section:
           "Ones":            {"played":False, "scored":0, "possible": 0, "maximum":5},
           "Twos":            {"played":False, "scored":0, "possible": 0, "maximum":10},
           "Threes":          {"played":False, "scored":0, "possible": 0, "maximum":15},
           "Fours":           {"played":False, "scored":0, "possible": 0, "maximum":20},
           "Fives":           {"played":False, "scored":0, "possible": 0, "maximum":25},
           "Sixes":           {"played":False, "scored":0, "possible": 0, "maximum":30},
                                     # lower section
           "Three Of A Kind": {"played":False, "scored":0, "possible": 0, "maximum":30},
           "Four Of A Kind":  {"played":False, "scored":0, "possible": 0, "maximum":30},
           "Full House":      {"played":False, "scored":0, "possible": 0, "maximum":25},
           "Small Straight":  {"played":False, "scored":0, "possible": 0, "maximum":30},
           "Large Straight":  {"played":False, "scored":0, "possible": 0, "maximum":40},
           "Yathzee":         {"played":False, "scored":0, "possible": 0, "maximum":50},
           "Chance":          {"played":False, "scored":0, "possible": 0, "maximum":30},
           }

for _ in range(5):    
    dicelist.append(random.randint(1,6))  

for game_round in range(1,14):   # 13 game rounds 
    for throw in range(1,4):     # 3 throws
        print(f"throw: {throw} of 3, game round: {game_round} of 13")
        print(" a  b  c  d  e")
        print(dicelist)
        if throw == 3:
            text = "" if game_round == 13 else "to start next game round:"
            unplayed = [name for name in options.keys() if not options[name]["played"]]
            print("Your options are those:")
            print("option           points")
            for name in unplayed:
                print(f"{name:>15} {calculate_score(dicelist, name):>2}")
                  
            while True:    
                command = input(f"type the (exact!) name of option to play {text} >>>")
                if command not in unplayed:
                    if command in options.keys():
                        print("You already used this option, please try again")
                    else:
                        print("Unknow option , please try again") 
                    continue
                break    
            # an option was choosen. Mark as played and give the correct score
            points = calculate_score(dicelist, command)
            print(f"You play {command} and get {points}.")
            # update dictionary
            options[command]["played"] = True
            options[command]["scored"] = points
            command = ""
            history.append(dicelist[:])  # append a COPY of dicelist to history
        else:
            command = input("Enter letter(s) to keep: >>>").lower() 
        
        if not "a" in command:
            dicelist[0] = random.randint(1,6)
        if not "b" in command:
            dicelist[1] = random.randint(1,6)
        if not "c" in command:
            dicelist[2] = random.randint(1,6)
        if not "d" in command:
            dicelist[3] = random.randint(1,6)
        if not "e" in command:
            dicelist[4] = random.randint(1,6)  
print("Game Over")  
print("game round,  result")
for game_round, result in enumerate(history, 1):
    print(f"{game_round:>5} : {result}" )
print(options)
```

output:

    throw: 3 of 3, game round: 3 of 13
     a  b  c  d  e
    [5, 5, 2, 5, 5]
    Your options are those:
    option           points
               Ones  0
               Twos  2
             Threes  0
              Fours  0
    Three Of A Kind 22
     Four Of A Kind 22
         Full House  0
     Small Straight  0
     Large Straight  0
            Yathzee  0
             Chance 22
    type the (exact!) name of option to play to start next game round: >>>Four Of A Kind
    You play Four Of A Kind and get 22.

updated TODO list:
*  ~~simulate throwing 5 dice~~
*  ~~let the player keep some dice / throw some dice  (3 throws per game round)~~
*  ~~keep track of game round and throws~~
*  ~~ask player to choose an option and keep track of played options~~
*  ~~show the player which options they can play and how many points they will get.~~