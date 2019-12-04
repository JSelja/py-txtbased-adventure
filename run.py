
   ## py-textbased-adventure ##

# A dynamic text adventure engine by Jakob Selja.
# Project started on 2/12/2019

import commandhandler, roomhandler
import os, sys, time

uInput = ''
output = ''

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    # Clear screen.
    clear()
    # DEBUG: Initial description of current room.
    print()
    print(roomhandler.move(0, roomhandler.currentRoom))

    # Game loop.
    while True:
        print()

        # Get player input.
        uInput = input('  > ').lower()

        if len(uInput) == 0:
            uInput = 'wait'

        # Parse input into array of terms.
        inputTerms = uInput.split()

        # Interpret the user's input.
        output = commandhandler.interpretCmd(inputTerms)

        # Print the output.
        print('\n' + output)
