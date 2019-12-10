# CMDINFO

# List of verbs.
VERBS = [
    ['move', 'go', 'travel'],                           # Movement
    ['examine', 'look', 'inspect', 'investigate'],      # Examine Item
    ['enter'],                                          # Go Inside
    ['end']                                             # End
]

# List of required arguments.
REQ_ARGS = [
    [ ['north', 'south', 'east', 'west', 'forward', 'back', 'left', 'right', 'up', 'down'] ],
    [ ['room'] ],
    [ [] ],
    []
]

# List of messages that appear when a required argument is missing.
ARG_MISSING_MSG = [
    ["Where do you want to move?"],
    ["What do you want to look at?"],
    ["You don't see any such thing to enter."],
    []
]

IDEN_ALLOWED = [
    [True],
    [True],
    [True],
    [False]
]
