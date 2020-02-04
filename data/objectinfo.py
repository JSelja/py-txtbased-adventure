# OBJECTINFO

# Attributes all objects possess:
# name - A unique name for identifying the object.
# alt-names - A list of other identifiers for the object. Doesn't neccessarily have to be unique.
# desc-room - Text to be returned when entering or examining the room.
# desc-examine - Text to be returned when examining the object.
# location - Which room the object initially resides in. Can be changed.
# collectable - Whether or not the object can be placed in the player's inventory. Collectable items require a 'get' interaction.
# weight - How many inventory slots the object takes up. Uncollectable item's weight does not matter.
# interactions - A dictionary of actions and their resulting text output.

# Any other attributes are custom to the object and will have a corresponding comment.

objects = [
    {
        "name": "chair",
        "alt-names": ["armchair"],
        "desc-room": "There is a chair in this room.",
        "desc-examine": "Chair description",
        "location": 2,
        "collectable": False,
        "weight": 0,
        "interactions": {
            "sit": "You sit down.",
            "stand": "You stand back out of the chair.",
            "wait-2": "You have waited in the chair."
        },

        # How many turns the player is sitting down for.
        "turnsSeated": 0
    },
    {
        "name": "key",
        "alt-names": [""],
        "desc-room": "There is a key here.",
        "desc-examine": "Key description",
        "location": 4,
        "collectable": True,
        "weight": 2,
        "interactions": {
            "get": "You get the key."
        }
    },
    {
        "name": "clover",
        "alt-names": ["clovers"],
        "desc-room": "There is a patch of clovers here.",
        "desc-examine": "One clover stands twice as high as the others. It has four leaves on it.",
        "location": 7,
        "collectable": True,
        "weight": 1,
        "interactions": {
            "get": "You pluck the clover out of the ground and carefully slide it into your front pocket."
        }
    }
]
