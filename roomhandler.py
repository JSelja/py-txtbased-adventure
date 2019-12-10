# ROOMHANDLER

import data.roominfo as roominfo

# The room the player is currently in.
currentRoom = 1

# Change the player's current room.
# N = 0, E = 1, S = 2, W = 3, U = 4, D = 5
def move(dr, warpLoc=0):
    global currentRoom

    # If not a warp command, move normally.
    if warpLoc == 0:
        # Check the room data for the given direction.
        newRoom = roominfo.MAP[currentRoom][dr]
    # Otherwise, warp to the location.
    else:
        newRoom = warpLoc

    # If it's a wall, you can't move that way.
    if newRoom == 0:
        return "You can't go that way."
    else:
        currentRoom = newRoom

        # Set the outputted text with the new room's title.
        outTxt = roominfo.DESCS[currentRoom][0].upper() + "+\n\n"

        # If the room has already been visted,
        if roominfo.IS_VISITED[currentRoom]:
            outTxt += roominfo.DESCS[currentRoom][2]
        else:
            roominfo.IS_VISITED[currentRoom] = True
            outTxt += roominfo.DESCS[currentRoom][1]

        return outTxt
