# ROOMINFO

# Room directions.
# 0 = Wall
MAP = [
    [0, 0, 0, 0, 0, 0],
#   [N, E, S, W, U, D]
    [2, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0]
]

# Room descriptions, both long and shot variants.
DESCS = [
    ["", "", ""],
    ["kitchen", "You are in a kitchen. The dining room is north.",
    "uh"],
    ["dining room", "You are in a dining room. The kitchen is south.",
    "um"]
]

# If the room has been visited by the player.
IS_VISITED = [False for i in range(len(MAP))]
