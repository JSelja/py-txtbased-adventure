# MAP

import constants

# The room the player is currently in.
currentRoom = 1

# Change the player's current room.
# N = 0, E = 1, S = 2, W = 3, U = 4, D = 5
def move(dir):
    global currentRoom
    # Check the room data for the given direction.
    newRoom = constants.ROOMDATA[currentRoom][dir]

    # If it's a wall, you can't move that way.
    if newRoom == 0:
        return "You can't go that way."
    else:
        currentRoom = newRoom
        return 'You went to room ' + str(currentRoom)
