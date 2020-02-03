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

# Attributes all rooms possess:
# title - The capitalised name of the room  displayed when entering.
# desc-large - The main room description returned when first enterring or examining it.
# desc-small - The shortened description returned when entering the room after it has already been entered.
# identifiers - Alternative names the adjacent rooms can be identified by.
# attributes - Special characteristics each direction possesses.
# is-visited - Whether or not the room has already been visited.
rooms = [
    {
        "title": "",
        "desc-large": "",
        "desc-small": "",
        "identifiers": [[], [], [], [], [], []],
        "attributes": [[], [], [], [], [], []],
        "is-visited": False
    }, {
        "title": "Outdoors",
        "desc-large": "You are outside. Inside is north.",
        "desc-small": "",
        "identifiers": [[], [], [], [], [], []],
        "attributes": [['inside'], [], [], [], [], []],
        "is-visited": False
    }, {
        "title": "Indoors",
        "desc-large": "You are inside. Outside is south. Another room is east.",
        "desc-small": "",
        "identifiers": [[], [], [], [], [], []],
        "attributes": [[], ['inside'], ['outside'], [], [], []],
        "is-visited": False
    }, {
        "title": "Another Room",
        "desc-large": "You are in another room. You can go west or down.",
        "desc-small": "",
        "identifiers": [[], [], [], [], [], []],
        "attributes": [[], [], [], ['inside'], [], ['inside', 'ladder']],
        "is-visited": False
    }, {
        "title": "Basement",
        "desc-large": "You are downstairs. You can go up.",
        "desc-small": "",
        "identifiers": [[], [], [], [], [], []],
        "attributes": [[], [], [], [], ['inside', 'ladder'], []],
        "is-visited": False
    }
]
