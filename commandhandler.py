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
            if term != inputTerms[0] and term in cmdinfo.REQARGS[vIndex][i]:
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
        if args[0] == 'north' or args[0] == 'forward':
            dir = 0
        elif args[0] == 'east' or args[0] == 'right':
            dir = 1
        elif args[0] == 'south' or args[0] == 'back':
            dir = 2
        elif args[0] == 'west' or args[0] == 'left':
            dir = 3
        elif args[0] == 'up':
            dir = 4
        elif args[0] == 'down':
            dir = 5

        return roomhandler.move(dir)

    elif verb == 'examine':
        # Return main description for the current room.
        if args[0] == 'room':
            return roominfo.DESCS[roomhandler.currentRoom][0]

    elif verb == 'exit':
        print("\nThanks for playing!")
        exit()
