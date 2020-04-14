import structs.rooms as r
import structs.items as i
import time

roomdefs = {}

## Room Definitions ##

roomdefs["Outside Cabin"] = {}
roomdefs["Outside Cabin"]["descLarge"] = """You find yourself at the south side of a small wooden cabin.
A lantern hanging from the southern wall swings in the breeze, illuminating an old oak doorway leading north inside.
The dark woods surround you in all directions, swaying in the swirling winds. A small clearing lies further south."""
roomdefs["Outside Cabin"]["descSmall"] = "You are outside, to the south of a cabin. The forest surrounds you in all directions."

roomdefs["Outside Cabin"]["exits"] = [
    {
        "direction": r.Directions.NORTH,
        "location": "Living Room",
        "identifiers": ['cabin'],
        "attributes": ['inside']
    }, {
        "direction": r.Directions.SOUTH,
        "location": "Forest Clearing",
        "identifiers": ['clearing'],
        "attributes": []
    }, {
        "direction": r.Directions.EAST,
        "location": "Forest",
        "identifiers": ['forest', 'woods'],
        "attributes": []
    }, {
        "direction": r.Directions.WEST,
        "location": "Forest",
        "identifiers": [],
        "attributes": []
    }
]

roomdefs["Living Room"] = {}
roomdefs["Living Room"]["descLarge"] = """You are in a cozy living space, bathed in the beautiful warmth of a crackling fireplace.
An open door leads east, and the front door leads outside, south."""
roomdefs["Living Room"]["descSmall"] = "You are in a small, fire-lit living room. The front door is south, and another door leads east."

roomdefs["Living Room"]["exits"] = [
    {
        "direction": r.Directions.SOUTH,
        "location": "Outside Cabin",
        "identifiers": ['front door', 'entrance'],
        "attributes": ['outside']
    }, {
        "direction": r.Directions.EAST,
        "location": "Kitchen",
        "identifiers": ['kitchen'],
        "attributes": ['inside']
    }
]

roomdefs["Kitchen"] = {}
roomdefs["Kitchen"]["descLarge"] = """You are in the cabin's eating area, which is bare and empty.
A door leads to the living area west, and a southern ladder travels down an open trap door."""
roomdefs["Kitchen"]["descSmall"] = "You are in the kitchen. A doorway leads west, and a ladder goes down through a trap door."

roomdefs["Kitchen"]["exits"] = [
    {
        "direction": r.Directions.WEST,
        "location": "Living Room",
        "identifiers": ['living room', 'fireplace'],
        "attributes": ['inside']
    }, {
        "direction": r.Directions.DOWN,
        "location": "Cellar",
        "identifiers": ['cellar', 'basement', 'trap door'],
        "attributes": ['inside', 'ladder']
    }
]

roomdefs["Cellar"] = {}
roomdefs["Cellar"]["descLarge"] = """You are in the cabin's cellar area. A few empty shelves are built into the dirt and brick walls.
Strange vines have sprouted through cracks in the floor. The air smells of damp soil.
A ladder leads up out of the cellar."""
roomdefs["Cellar"]["descSmall"] = "You are in a damp, overgrown basement. A ladder leads up behind you."

roomdefs["Cellar"]["exits"] = [
    {
        "direction": r.Directions.UP,
        "location": "Kitchen",
        "identifiers": ['kitchen'],
        "attributes": ['inside', 'ladder']
    }
]

roomdefs["Cellar"]["items"] = [
    {
        "name": "Coin",
        "identifiers": ['coin', 'bronze'],
        "descriptions": {
            "room": "A small bronze coin covered in dust sits on one of the empty shelves.",
            "look": "The coin is quite small, with elegant, cursive engravings one side. They spell out the initials 'E.V.R'."
        },
        "isCollectable": True,
        "weight": 1,
        "interactions": {
            "get": {
                "text": "You put the small bronze coin in your pocket.",
                "action": None
            }
        }
    }
]

roomdefs["Forest Clearing"] = {}
roomdefs["Forest Clearing"]["descLarge"] = "You are surrounded by trees. There is a dim glow eminating from a cabin not far to the north."
roomdefs["Forest Clearing"]["descSmall"] = "You are in the forest. There is a cabin further north."

roomdefs["Forest Clearing"]["exits"] = [
    {
        "direction": r.Directions.NORTH,
        "location": "Outside Cabin",
        "identifiers": ['cabin'],
        "attributes": []
    }, {
        "direction": r.Directions.EAST,
        "location": "Forest",
        "identifiers": ['forest', 'woods'],
        "attributes": []
    }, {
        "direction": r.Directions.SOUTH,
        "location": "Forest",
        "identifiers": [],
        "attributes": []
    }, {
        "direction": r.Directions.WEST,
        "location": "Forest",
        "identifiers": [],
        "attributes": []
    }
]

roomdefs["Forest"] = {}
roomdefs["Forest"]["descLarge"] = """You are in the forest. Your view is immensely dark and dense with thick trees reaching high above.
The ground here is rugged and uneven. Roots have torn through the moss and earth below your feet.
The darkness and uneven terrain obscures your sense of direction."""
roomdefs["Forest"]["descSmall"] = "You are in the dark depths of the forest. The darkness and uneven terrain obscures your sense of direction."

roomdefs["Forest"]["exits"] = [
    {
        "direction": r.Directions.NORTH,
        "location": "Forest",
        "identifiers": ['forest', 'woods'],
        "attributes": []
    }, {
        "direction": r.Directions.EAST,
        "location": "Forest",
        "identifiers": [],
        "attributes": []
    }, {
        "direction": r.Directions.SOUTH,
        "location": "Forest",
        "identifiers": [],
        "attributes": []
    }, {
        "direction": r.Directions.WEST,
        "location": "Forest Clearing",
        "identifiers": [],
        "attributes": []
    }
]

# Create room items for each defined room.
rooms = {}
for key in roomdefs:
    itemList = {}
    for currentItem in roomdefs[key].get("items", {}):
        itemList[currentItem["name"]] = i.Item(currentItem["name"], currentItem["identifiers"], key, currentItem["descriptions"]["room"], currentItem["descriptions"]["look"], currentItem["isCollectable"], currentItem["weight"], currentItem["interactions"])

    rooms[key] = r.Room(key, roomdefs[key]["descLarge"], roomdefs[key]["descSmall"], roomdefs[key].get("descLook", None), roomdefs[key]["exits"], itemList)
