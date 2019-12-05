# COMMANDHANDLER

import roomhandler
import data.cmdinfo as cmdinfo
import data.roominfo as roominfo

# Parses and interprets player inputs.
def interpretCmd(inputTerms):
    verb = ''
    vIndex = 0
    args = []
    # Identify if the verb is in the list of verbs.
    for i in range(len(cmdinfo.VERBS)):
        if inputTerms[0] in cmdinfo.VERBS[i]:
            verb = cmdinfo.VERBS[i][0]
            vIndex = i

    # If no verb was found, exit this function.
    if verb == '':
        return interpretError('That isn’t something you know how to do.')

    # Identify if all required arguments are found.
    for i in range(len(cmdinfo.REQ_ARGS[vIndex])):
        for term in inputTerms:
            if term != inputTerms[0] and term in cmdinfo.REQ_ARGS[vIndex][i]:
                # Add to the interpreted arguments array.
                args.append(term)
                break
            # If room identifiers are allowed,
            elif cmdinfo.IDEN_ALLOWED[vIndex][i]:
                # Check the name of each room that can be accessed from the current room,
                for r in range(len(roominfo.MAP[roomhandler.currentRoom])):
                    if term != inputTerms[0] and roominfo.MAP[roomhandler.currentRoom][r] > 0 and term != 'room':
                        if term in roominfo.DESCS[roominfo.MAP[roomhandler.currentRoom][r]][0].split() or term in roominfo.IDENTIFIERS[roominfo.MAP[roomhandler.currentRoom][r]]:
                            args.append(r)
                            break

                if len(args) > i:
                    break

        # If nothing was appended to the arguments array, a required argument was not inputted.
        if len(args) <= i:
            return interpretError(cmdinfo.ARG_MISSING_MSG[vIndex][i])

    # Send information to be executed.
    return executeAction(verb, args)

# Print an error message if the expected input was not received.
def interpretError(msg):
    return msg

# Run particular functions based off of interpretted input.
def executeAction(verb, args):
    if verb == 'move':
        # Set direction based off of inputted argument.
        if  args[0] == 'north' or args[0] == 'forward':
            dr = 0
        elif args[0] == 'east' or args[0] == 'right':
            dr = 1
        elif args[0] == 'south' or args[0] == 'back':
            dr = 2
        elif args[0] == 'west' or args[0] == 'left':
            dr = 3
        elif args[0] == 'up':
            dr = 4
        elif args[0] == 'down':
            dr = 5
        # If none of these were found, a room indentifier was inputted.
        else:
            dr = int(args[0])

        return roomhandler.move(dr)

    elif verb == 'examine':
        # Return main description for the current room.
        if 'room' in args[0]:
            return roominfo.DESCS[roomhandler.currentRoom][1]

    elif verb == 'exit':
        return "Thanks for playing!"
