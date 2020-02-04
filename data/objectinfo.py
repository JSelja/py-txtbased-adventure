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
        "desc-room": "A sunken leather armchair sits in the center of the room, facing the fire.",
        "desc-examine": "The armchair is made of an old, faded leather, with many long scratches along the arm rests.\nThe crevices are deep and full of dust, possibly hiding lost items.",
        "location": 2,
        "collectable": False,
        "weight": 0,
        "interactions": {
            "sit": "You sink into the chair. The warmth of the leather against your skin relaxes you.",
            "stand": "You can't relax for too long. You stand back out of the chair.",
            "wait-2": "As you relax in the chair, you wonder how long the fire has been burning for.",
            "search": "The crevices of the chair contain some loose change. You find four silver pieces."
        },

        # How many turns the player is sitting down for.
        "turnsSeated": 0
    },
    {
        "name": "key",
        "alt-names": [""],
        "desc-room": "A small bronze key covered in dust sits on the empty shelf.",
        "desc-examine": "The key is quite small, with slight engravings around the bow. They spell out the initials+ 'E.R'.",
        "location": 4,
        "collectable": True,
        "weight": 2,
        "interactions": {
            "get": "You put the key in your pocket."
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
