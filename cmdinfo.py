# CMDINFO

# List of verbs.
VERBS = [
    ['move', 'go', 'travel', 'head'],                   # Movement
    ['examine', 'look', 'inspect', 'investigate'],      # Examine Item
    ['exit']                                            # Exit
]

# List of required arguments.
REQARGS = [
    [ ['north', 'south', 'east', 'west', 'forward', 'back', 'left', 'right', 'up', 'down'] ],   # Movement
    [ ['room'] ],
    []
]

# List of messages that appear when a required argument is missing.
ARGMISSINGMSG = [
    ["Where do you want to move?"], # Movement
    ["What do you want to look at?"],
    []
]
