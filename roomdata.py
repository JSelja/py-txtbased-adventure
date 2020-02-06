import structs.rooms as r

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
        "identifiers": [],
        "attributes": []
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
        "identifiers": [],
        "attributes": []
    }, {
        "direction": r.Directions.DOWN,
        "location": "Cellar",
        "identifiers": ['basement'],
        "attributes": ['ladder']
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

# Create room objects for each defined room.
rooms = {}
for key in roomdefs:
    rooms[key] = r.Room(key, roomdefs[key]["descLarge"], roomdefs[key]["descSmall"], roomdefs[key]["exits"])
