# ROOMHANDLER

import data.roominfo as roominfo

# The room the player is currently in.
currentRoom = 1

# Change the player's current room.
# N = 0, E = 1, S = 2, W = 3, U = 4, D = 5
def move(dir, warpLoc=0):
    global currentRoom

    # If not a warp command, move normally.
    if warpLoc == 0:
        # Check the room data for the given direction.
        newRoom = roominfo.MAP[currentRoom][dir]
    # Otherwise, warp to the location.
    else:
        newRoom = warpLoc

    # If it's a wall, you can't move that way.
    if newRoom == 0:
        return "You can't go that way."
    else:
        currentRoom = newRoom
        # If the room has already been visted,
        if roominfo.ISVISITED[currentRoom]:
            return roominfo.DESCS[currentRoom][1]
        else:
            roominfo.ISVISITED[currentRoom] = True
            return roominfo.DESCS[currentRoom][0]
