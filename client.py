'''
Name: Mikhail Ermak
Lesson: Game of Nim
'''

# There is one module that we should use for a better quality of the computer algorithm:
import random # This module will make the computer choose a number from 3 to 1 randomly.

# The Algorithm of the Computer:
def ComputerStonesTaken(amount):
    if amount == 4:
        return 3
    elif amount == 3:
        return 2
    elif amount == 2 or amount == 1:
        return 1
    else:
        return random.randint(1, 3)

# The Algorithm of the User:
def UserStonesTaken(amount):
    StonesTaken = int(input("How many stones would you pick? ").strip())

    if amount == 2:
        while StonesTaken not in [1, 2]:
            print("\033[31mERROR:\033[0m You can borrow only 1 to 2 stones!")
            StonesTaken = int(input("How many stones would you pick? ").strip())

    elif amount == 1:
        while StonesTaken not in [1]:
            print("\033[31mERROR:\033[0m You can borrow only 1 stone!")
            StonesTaken = int(input("How many stones would you pick? ").strip())

    # Continues looping until the user will not enter a
    while StonesTaken not in [1, 2, 3]: # valid number:
        print("\033[31mERROR:\033[0m You can borrow only 1 to 3 stones!")
        StonesTaken = int(input("How many stones would you pick? ").strip())
    else:
        return StonesTaken
