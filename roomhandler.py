# ROOMHANDLER

import data.roominfo as roominfo
import data.objectinfo as objectinfo

# The room the player is currently in.
currentRoom = 1

# Return the direction a room is from the current room.
def getDirection(args):
    # Join the player's input to account for multi-word room names.
    uInput = ' '.join(args)
    # For each possible direction,
    for r in range(len(roominfo.MAP[currentRoom])):
        if roominfo.MAP[currentRoom][r] != 0:
            # If the room name or an identifier is found, return its direction.
            if roominfo.DESCS[roominfo.MAP[currentRoom][r]][0].lower() in uInput or any(s in uInput for s in roominfo.IDENTIFIERS[currentRoom][r]):
                return r

    return -1

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
        outTxt = "\n" + roominfo.DESCS[currentRoom][0].upper() + "+\n\n"

        # If the room has already been visted, add the large description.
        if roominfo.IS_VISITED[currentRoom]:
            outTxt += roominfo.DESCS[currentRoom][2]
        # Otherwise, add the small description.
        else:
            roominfo.IS_VISITED[currentRoom] = True
            outTxt += roominfo.DESCS[currentRoom][1]

        # Add any object desctriptions.
        for o in objectinfo.objects:
            if o.get("location") == currentRoom:
                outTxt += "\n" + o["description"]

        return outTxt
