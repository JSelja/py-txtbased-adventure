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
        "title": "Outside Cabin",
        "desc-large": "You find yourself at the south side of a small wooden cabin.\nA lantern hanging from the southern wall swings in the breeze, illuminating an old oak doorway leading north inside." +
        "\nThe dark woods surround you in all directions, swaying in the swirling winds.",
        "desc-small": "",
        "identifiers": [['cabin'], [], [], [], [], []],
        "attributes": [['inside'], [], [], [], [], []],
        "is-visited": False
    }, {
        "title": "Living Room",
        "desc-large": "You are in a cozy living space, bathed in the beautiful warmth of a crackling fireplace.\n An open door leads east, and the front door leads outside, south.",
        "desc-small": "",
        "identifiers": [[], [], ['cabin'], [], [], []],
        "attributes": [[], ['inside'], ['outside'], [], [], []],
        "is-visited": False
    }, {
        "title": "Kitchen",
        "desc-large": "You are in the cabin's eating area, which has clearly been ransacked. The cupboards are empty and missing their doors." +
        "\nA wooden table is turned on its side in the middle of the room.\nA door leads to the living area west, and a southern ladder travels down an open trap door.",
        "desc-small": "",
        "identifiers": [[], [], [], [], [], []],
        "attributes": [[], [], [], ['inside'], [], ['inside', 'ladder']],
        "is-visited": False
    }, {
        "title": "Cellar",
        "desc-large": "You are in a small basement, the moldy brick walls lined with empty shelves. A few wooden barrels sit in a corner covered with cobwebs.\nThe ladder leads up out of the cellar.",
        "desc-small": "",
        "identifiers": [[], [], [], [], [], []],
        "attributes": [[], [], [], [], ['inside', 'ladder'], []],
        "is-visited": False
    }
]
