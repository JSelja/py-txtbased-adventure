# CMDINFO

# List of verbs.
VERBS = [
    ['move', 'go', 'travel', 'head', 'enter'],          # Movement
    ['examine', 'look', 'inspect', 'investigate'],      # Examine Item
    ['end']                                             # End
]

# List of required arguments.
REQ_ARGS = [
    [ ['north', 'south', 'east', 'west', 'forward', 'back', 'left', 'right', 'up', 'down'] ],   # Movement
    [ ['room'] ],
    []
]

# List of messages that appear when a required argument is missing.
ARG_MISSING_MSG = [
    ["Where do you want to move?"], # Movement
    ["What do you want to look at?"],
    []
]

IDEN_ALLOWED = [
    [True],
    [True],
    [False]
]
