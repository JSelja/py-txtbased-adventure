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
    for i in range(len(cmdinfo.REQARGS[vIndex])):
        for term in inputTerms:
            if term != inputTerms[0] and any(s in term for s in cmdinfo.REQARGS[vIndex][i]):
                # Add to the interpreted arguments array.
                args.append(term)
                break

        # If nothing was appended to the arguments array, a required argument was not inputted.

        if len(args) <= i:
            return interpretError(cmdinfo.ARGMISSINGMSG[vIndex][i])

    # Send information to be executed.
    return executeAction(verb, args)

# Print an error message if the expected input was not received.
def interpretError(msg):
    return msg

# Run particular functions based off of interpretted input.
def executeAction(verb, args):
    if verb == 'move':
        if  'north' in args[0] or 'forward' in args[0]:
            dir = 0
        elif 'east' in args[0] or 'right' in args[0]:
            dir = 1
        elif 'south' in args[0] or 'back' in args[0]:
            dir = 2
        elif 'west' in args[0] or 'left' in args[0]:
            dir = 3
        elif 'up' in args[0]:
            dir = 4
        elif 'down' in args[0]:
            dir = 5

        return roomhandler.move(dir)

    elif verb == 'examine':
        # Return main description for the current room.
        if 'room' in args[0]:
            return roominfo.DESCS[roomhandler.currentRoom][0]

    elif verb == 'exit':
        return "Thanks for playing!"
