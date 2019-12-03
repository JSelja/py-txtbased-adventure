# COMMANDHANDLER

import constants

# The message to be outputted.
outMsg = ''

# Parses and interprets player inputs.
def interpretCmd(inputTerms):
    verb = ''
    vIndex = 0
    args = []
    # Identify if the verb is in the list of verbs.
    for i in range(len(constants.VERBS)):
        if inputTerms[0] in constants.VERBS[i]:
            verb = constants.VERBS[i][0]
            vIndex = i

    # If no verb was found, exit this function.
    if verb == '':
        #outMsg = 'That isn’t something you know how to do.'
        print("That isn't something you know how to do.")
        return

    # Identify if all required arguments are found.
    for i in range(len(constants.REQARGS[vIndex])):
        for term in inputTerms:
            if term != inputTerms[0] and term in constants.REQARGS[vIndex][i]:
                # Add to the interpreted arguments array.
                args.append(term)
                break

        # If nothing was appended to the arguments array, a required argument was not inputted.
        if len(args) <= i:
            #outMsg = constants.ARGMISSINGMSG[i]
            print(constants.ARGMISSINGMSG[vIndex][i])
            return

    # Print the work.
    print(verb + ' ' + ''.join(args))
