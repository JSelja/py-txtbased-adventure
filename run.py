
   ## py-textbased-adventure ##

# A dynamic text adventure engine by Jakob Selja.
# Project started on 2/12/2019

import os

uInput = ''

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    clear()
    print()

    uInput = input('  > ')

    if uInput == 'hello':
        print("Message recieved.")
