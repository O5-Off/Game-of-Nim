'''
Name: Mikhail Ermak
Lesson: Game of Nim
'''

# There are three modules and one file that we should use for a better quality of the Game of Nim:
import random # This module will randomly output the amount of stones making the game more interesting.
import client # This is not a module, yet it is just a file where the user and computer logics are located.
import time # This module will make an affect that computer is thinking before output the amount of stones.
import os # This module will clear the screen for us after every pair of turns ensuring smooth in the game.

# First, the script chooses a random amount of stones before
AmountOfStones = random.randint(22, 32) # starting the game:

# Before starting the game, the script should randomly settle whether who
WhoIsGoingFirst = random.choice(["Computer", "User"]) # is going the first?
CurrentState = "" # We need this variable to determine the player's turn┐
# Moreover, this varible will help us to determine the winner at the end┘

# To optimize our writting, we can put all our needs into one formal paragraph and
def ComputerBlock(amount, removal, state): # then call it as many times as we want:
    amount -= removal # Removes amount of stones that was selected by the computer.

    print("Computer is thinking...") # All of these were done just for originality┐
    time.sleep(1) #───────────────────────────────────────────────────────────────┘

    state = "Computer"
    return amount, state

# To optimize our writting, we can put all our needs into one formal paragraph and
def UserBlock(amount, removal, state): # then call it as many times as we want to:
    amount -= removal # Removes the amount of stones that was elected by the user.

    state = "User"
    return amount, state

# Loop the game until no stones will remain in the game -> means┐
while AmountOfStones > 0: # who will take the last stone -> lose┘

    # This is a universal way to clear the screen after every pair of turns
    os.system("cls" if os.name == "nt" else "clear") # for its portability:

    print("\033[33m===========\033[0m")
    print("\033[33mGame\033[0m of \033[32mNim\033[0m")
    print("\033[32m===========\033[0m")
    print()

    Pebbles = (AmountOfStones * "•") # Prints amount of stones:
    print("Remaining Pebbles:", Pebbles, f"({AmountOfStones})")

    # If computer is going first, then the subsequent moves will
    if WhoIsGoingFirst == "Computer": # follow the same order:
        Removed = client.ComputerStonesTaken(AmountOfStones)
        AmountOfStones, CurrentState = ComputerBlock(AmountOfStones, Removed, CurrentState)
        if AmountOfStones <= 0: # This check-in is required for the moment someone takes the
            break # last stone, the loop ends and the other player never gets an extra turn:

        Pebbles = (AmountOfStones * "•") # Prints stones:
        print("\033[32mPebbles:\033[0m", Pebbles, f"({AmountOfStones})")

        Removed = client.UserStonesTaken(AmountOfStones)
        AmountOfStones, CurrentState = UserBlock(AmountOfStones, Removed, CurrentState)
        if AmountOfStones <= 0: # This check-in is required for the moment someone takes the
            break # last stone, the loop ends and the other player never gets an extra turn:

        Pebbles = (AmountOfStones * "•") # Prints stones:
        print("\033[33mPebbles:\033[0m", Pebbles, f"({AmountOfStones})")

    # If user is going first, then the subsequent moves will
    elif WhoIsGoingFirst == "User": # follow the same order:
        Removed = client.UserStonesTaken(AmountOfStones)
        AmountOfStones, CurrentState = UserBlock(AmountOfStones, Removed, CurrentState)
        if AmountOfStones <= 0: # This check-in is required for the moment someone takes the
            break # last stone, the loop ends and the other player never gets an extra turn:

        Pebbles = (AmountOfStones * "•") # Prints stones:
        print("\033[33mPebbles:\033[0m", Pebbles, f"({AmountOfStones})")

        Removed = client.ComputerStonesTaken(AmountOfStones)
        AmountOfStones, CurrentState = ComputerBlock(AmountOfStones, Removed, CurrentState)
        if AmountOfStones <= 0: # This check-in is required for the moment someone takes the
            break # last stone, the loop ends and the other player never gets an extra turn:

        Pebbles = (AmountOfStones * "•") # Prints stones:
        print("\033[32mPebbles:\033[0m", Pebbles, f"({AmountOfStones})")

    time.sleep(5) # The script will give three seconds to look at your pair of turns.

# Whoever took the last stone went last in
if CurrentState == "Computer": # the game:
    print("Computer took the last stone!")
else:
    print("User took the last stone!")

'''
NOTE: No AI was used while working on the script. The only thing I used
it was to review my Python knowledge, like "What is fString formatting?
NOTE: I did not actually even rewatch the video of how doing this game.
In other words, I just grasped the concept, and things really took off.
'''