# COMMANDHANDLER

import roomhandler
import data.roominfo as roominfo

# Parses and interprets player inputs.
def interpretCmd(inputTerms):
    verb = inputTerms[0]
    args = inputTerms[1:]

    if verb == 'move' or verb == 'go':
        # Set direction based off of inputted argument.
        # Format: move {direction}
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
        # If none of these were found, a room indentifier was inputted.
        else:
            # Format: 'move in/to/into {room}' or 'move inside {room: inside}'
            if args[0] in ['in', 'to', 'into', 'inside', 'outside']:
                dr = roomhandler.getDirection(args[1:])

                if dr == -1 or args[0] == 'inside' and 'inside' not in roominfo.ATTRIBUTES[roomhandler.currentRoom][dr] or args[0] == 'outside' and 'outside' not in roominfo.ATTRIBUTES[roomhandler.currentRoom][dr] :
                    return "You don't see any such place to " + verb + "."

            # In this case, no proper arguments were inputted.
            else:
                return 'Where do you want to ' + verb + '?'

        return roomhandler.move(dr)

    elif verb == 'enter' or verb == 'exit':
        dr = roomhandler.getDirection(args)

        if dr == -1:
            return "You don't see any such place to " + verb + "."

        # if the room is inside, enter it. If the room is outside, exit the current room into it.
        if verb == 'enter':
            position = 'inside'
        else:
            position = 'outside'

        if position in roominfo.ATTRIBUTES[roomhandler.currentRoom][dr]:
            return roomhandler.move(dr)
        elif 'inside' in args or 'outside' in args:
            return 'What do you mean?'
        else:
            return "You can't " + verb + " anything that way."

    elif verb == 'climb':
        dr = -1
        if args[0] == 'up':
            dr = 4
        elif args[0] == 'down':
            dr = 5
        elif args[0] == 'ladder':
            # If there is a ladder in the room, climb in the direction it goes.
            for r in range(2):
                if 'ladder' in roominfo.ATTRIBUTES[roomhandler.currentRoom][4 + r]:
                    dr = 4 + r

        if dr == -1:
            return "You can't climb that way."

        return roomhandler.move(dr)

    elif verb == 'stop':
        return "Thanks for playing!"

    else:
        return "That isn't something you know how to do."
