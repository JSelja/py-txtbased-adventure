# ROOMINFO

# Room directions.
# 0 = Wall
MAP = [
    [0, 0, 0, 0, 0, 0], # ROOM 0
#   [N, E, S, W, U, D]
    [2, 0, 0, 0, 0, 0],
    [2, 2, 1, 2, 0, 0]
]

# Room descriptions, both long and shot variants.
DESCS = [
    ["You are trapped in a tiny grey cell. There is no way in or out.",
    "Looks like a bug caused you to end up here."],
    ["You are in a small blank room. The walls are made of starkly white padded material."
    + " There is a doorway leading north into a darker space.",
    "You are in a white room. A dark doorway leads north."],
    ["You are in a large room. It is completely dark, spare for the "
     + "white light filtering through the southern doorway you just came through.",
     "You are in a dark room. A bright doorway leads south."]
]

# If the room has been visited by the player.
ISVISITED = [False for i in range(len(MAP))]
