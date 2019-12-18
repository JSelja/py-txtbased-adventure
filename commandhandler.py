# COMMANDHANDLER
# / = Interchangable verbs or arguments.
# | = Respective verbs and arguments.

import json

import roomhandler
import data.roominfo as roominfo

# Parses and interprets player inputs.
def interpretCmd(inputTerms):
    verb = inputTerms[0]
    args = inputTerms[1:]

    # MOVE/GO - Player travels to an adjacent room, and the new room's description is outputted.
    # Formats:
    # 'move/go {direction}'
    # 'move/go in/to/into {room}'
    # 'move/go inside|outside {room: inside|outside}'
    if verb == 'move' or verb == 'go':
        # Set direction based off of inputted argument.
        if 'north' in args or 'forward' in args:
            dr = 0
        elif 'east' in args or 'right' in args:
            dr = 1
        elif 'south' in args or 'back' in args:
            dr = 2
        elif 'west' in args or 'left' in args:
            dr = 3
        elif 'up' in args or 'upward' in args:
            dr = 4
        elif 'down' in args or 'downward' in args:
            dr = 5

        # If none of these were found, the player may have inputted a room identifier.
        else:
            if args[0] in ['in', 'to', 'into', 'inside', 'outside']:
                # See which direction the specified room is from the current room.
                dr = roomhandler.getDirection(args[1:])

                # Room movement will not occur if the room wasn't found, or if the specified room isn't inside or outside when such argument is used.
                if dr == -1 or args[0] == 'inside' and 'inside' not in roominfo.ATTRIBUTES[roomhandler.currentRoom][dr] or args[0] == 'outside' and 'outside' not in roominfo.ATTRIBUTES[roomhandler.currentRoom][dr] :
                    return "You don't see any such place to " + verb + "."

            # In this case, no proper arguments were inputted.
            else:
                return 'Where do you want to ' + verb + '?'

        # Perform movement if successful.
        return roomhandler.move(dr)

    # ENTER/EXIT - Player travels to an adjacent room that is either inside when enterring, or outside when exiting.
    # Format: 'enter|exit {room: inside|outside}'
    elif verb == 'enter' or verb == 'exit':
        # See which direction the specified room is from the current room.
        dr = roomhandler.getDirection(args)

        # Room movement will not occur if the room wasn't found.
        if dr == -1:
            return "You don't see any such place to " + verb + "."

        # Set the attribute to search for based on the command.
        position = 'inside' if verb == 'enter' else 'outside'

        # TODO: Output "You're already outside." if the player tries to exit while outside.

        # If the room is inside, enter it. If the room is outside, exit the current room into it.
        if position in roominfo.ATTRIBUTES[roomhandler.currentRoom][dr]:
            return roomhandler.move(dr)
        # In this case, the new room is not inside if entering or outside if exiting.
        else:
            return "You can't " + verb + " anything that way."

    # CLIMB - Player travels upwards or downwards, or in the direction a ladder heads.
    # Format: 'climb up/down/ladder'
    elif verb == 'climb':
        # Set direction to upwards.
        if 'up' in args or 'upward' in args:
            dr = 4
        # Set direction to downwards.
        elif 'down' in args or 'downward' in args:
            dr = 5
        # Set direction to the ladder's destination.
        elif 'ladder' in args:
            # If there is a ladder in the room, climb in the direction it goes.
            for r in range(2):
                if 'ladder' in roominfo.ATTRIBUTES[roomhandler.currentRoom][4 + r]:
                    dr = 4 + r
        # In this case, no proper arguments were inputted.
        else:
            return "You can't climb that way."

        # Perform movement if successful.
        return roomhandler.move(dr)

    # DEBUG: Stop command exits the game.
    # TODO: Add final exit command that asks for the player's confirmation to exit.
    elif verb == 'stop':
        return "Thanks for playing!"

    # If no defined verb was found, it isn't a known action.
    else:
        return "That isn't something you know how to do."
