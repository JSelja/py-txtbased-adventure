# OBJECTINFO

# Attributes all objects possess:
# name - A unique name for identifying the object.
# alt-names - A list of other identifiers for the object. Doesn't neccessarily have to be unique.
# description - Text to be returned when inspecting the object.
# location - Which room the object initially resides in. Can be changed.
# interactions - A dictionary of actions and their resulting text output.

# Any other attributes are custom to the object and will have a corresponding comment.

objects = [
    {
        "name": "chair",
        "alt-names": ["armchair"],
        "description": "A sunken leather armchair sits in the center of the room, facing the fire.",
        "location": 2,
        "collectable": False,
        "interactions": {
            "sit": "You sink into the chair. The warmth of the leather against your skin relaxes you.",
            "stand": "You can't relax for too long. You stand back out of the chair.",
            "wait2": "As you relax in the chair, you wonder how long the fire has been burning for."
        },

        # How many turns the player is sitting down for.
        "turnsSeated": 0
    }
]
