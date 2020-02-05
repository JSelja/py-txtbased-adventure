class Directions:
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    UP = 4
    DOWN = 5

class Room:
    """An area the player can occupy."""
    def __init__(self, title, descLarge, descSmall, exits, descLook=None):
        self.title = title
        self.descLarge = descLarge
        self.descSmall = descSmall
        self.descLook = descLook if descLook is not None else descLarge
        self.exits = exits

        self.isVisited = False


    def getRoomDescription(self):
        outTxt = ""

        outTxt += "\n" + self.title.upper() + "+\n\n"

        if self.isVisted:
            outTxt += self.descSmall

        else:
            outTxt += self.descLarge

        # TODO: Add each object description that is present in the room. Taken from array of object instances.

        return outTxt

    def getExitByDirection(self, dirTxt):
        if 'north' in dirTxt or 'forward' in dirTxt:
            dr = Directions.NORTH

        elif 'east' in dirTxt or 'right' in dirTxt:
            dr = Directions.EAST

        elif 'south' in dirTxt or 'back' in dirTxt:
            dr = Directions.SOUTH

        elif 'west' in dirTxt or 'left' in dirTxt:
            dr = Directions.WEST

        elif 'up' in dirTxt or 'upwards' in dirTxt:
            dr = Directions.UP

        elif 'down' in dirTxt or 'downwards' in dirTxt:
            dr = Directions.DOWN

        else:
            dr = -1

        for e in self.exits:
            if dr == e["direction"]:
                return e["location"]

        return None

    def getExitByIdentifier(self, iden):
        for e in self.exits:
            if any(s in iden for s in e["identifiers"]):
                return e["location"]

        return None

    def getExitByAttribute(self, attr):
        for e in self.exits:
            if any(s in attr for s in e["attributes"]):
                return e["location"]

        return None
