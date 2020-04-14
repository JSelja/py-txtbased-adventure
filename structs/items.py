class Item:
    """An interactive or usable element of the world."""
    def __init__(self, name, identifiers, location, descRoom, descLook, isCollectable, weight, interactions):
        self.name = name
        self.identifiers = identifiers
        self.location = location
        self.descRoom = descRoom
        self.descLook = descLook
        self.isCollectable = isCollectable
        self.weight = weight
        self.interactions = interactions
