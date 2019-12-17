# ROOMINFO

# Room directions.
# 0 = Wall
MAP = [
    [0, 0, 0, 0, 0, 0],
#   [N, E, S, W, U, D]
    [2, 0, 0, 0, 0, 0],
    [0, 3, 1, 0, 0, 0],
    [0, 0, 0, 2, 0, 4],
    [0, 0, 0, 0, 3, 0]
]

# Room descriptions, both long and shot variants.
DESCS = [
    ["", "", ""],
    ["Outside Cabin", "You find yourself at the south side of a small wooden cabin.\nA lantern hanging from the southern wall swings in the breeze, illuminating an old oak doorway leading north inside." +
    "\nThe dark woods surround you in all directions, swaying in the swirling winds.", ""],
    ["Living Room", "You are in a cozy living space, bathed in the beautiful warmth of a crackling fireplace.\n" +
    "A sunken leather armchair sits in the center of the room, facing the fire.\nAn open door leads east, and the front door leads outside, south.", ""],
    ["Kitchen", "You are in the cabin's eating area, which has clearly been ransacked. The cupboards are empty and missing their doors." +
    "\nA wooden table is turned on its side in the middle of the room.\nA door leads to the living area west, and a southern ladder travels down an open trap door.", ""],
    ["Cellar", "You are in a small basement, the moldy brick walls lined with empty shelves. A few wooden barrels sit in a corner covered with cobwebs.\nThe ladder leads up out of the cellar.", ""]
]

# Alternative names a room can be identified by.
IDENTIFIERS = [
    [],
    # [N, E, S, W, U, D]
    [['cabin'], [], [], [], [], []],
    [[], [], ['cabin'], [], [], []],
    [[], [], [], [], [], []],
    [[], [], [], [], [], []]
]

# Information regarding what actions can be performed in a certain room.
# 'inside' = Enter command
# 'outside' = Exit command
# 'ladder' = Climb command
ATTRIBUTES = [
    [],
    # [N, E, S, W, U, D]
    [['inside'], [], [], [], [], []],
    [[], ['inside'], ['outside'], [], [], []],
    [[], [], [], ['inside'], [], ['inside', 'ladder']],
    [[], [], [], [], ['inside', 'ladder'], []]
]

# If the room has been visited by the player.
IS_VISITED = [False for i in range(len(MAP))]
