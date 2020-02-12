
   ## py-textbased-adventure ##

# A dynamic text adventure engine by Jakob Selja.
# Project started on 2/12/2019

import commandhandler, roomdata
import os, sys, time

uInput = ''
output = ''

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def delay_print(s):
    for c in s:
        if c != '+':
            sys.stdout.write(c)
            sys.stdout.flush()

        if c == ',':
            time.sleep(0.2)
        elif c == '.':
            time.sleep(0.3)
        elif c == '+':
            time.sleep(0.35)
        elif c != '\n':
            #time.sleep(0.05)
            pass

    sys.stdout.write('\n\n')

if __name__ == "__main__":
    # Clear screen.
    clear()
    # DEBUG: Initial description of current room.
    print()
    delay_print(roomdata.rooms["Outside Cabin"].getRoomDescription())

    # Game loop.
    while True:

        # Get player input.
        uInput = input('  > ').lower()

        if len(uInput) <= 0:
            uInput = 'wait'

        # Interpret the user's input.
        output = commandhandler.interpretCmd(uInput)

        # Print the output.
        delay_print('\n' + output)

        # Close if the exit command was inputted.
        if output == "Thanks for playing!":
            time.sleep(1)
            exit()
