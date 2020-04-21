# a/b = Interchangable verbs or arguments.
# a|b = Respective verbs and arguments.

# Current defined commands:
# MOVE / GO, ENTER, CLIMB, GET
# EXAMINE, SIT, STAND, WAIT, EXIT
import gamedata as data

# DEBUG: Placeholder current room, will be in player class.
currentRoom = data.rooms["Cellar"]

# Parses and interprets player inputs.
def interpretCmd(uInput):
    global currentRoom

    inputTerms = uInput.split()
    verb = inputTerms[0]
    args = inputTerms[1:]

    # MOVE/GO - Player travels to an adjacent room, and the new room's description is outputted.
    # Format:
    # 'move/go {direction}'
    # 'move/go in/to/into {room}'
    # 'move/go inside|outside {room: inside|outside}'
    if verb == 'move' or verb == 'go':
        # Don't allow movement if the player is seated.
        #if player.isSeated:
        #    return "You can't " + verb + " anywhere while sitting down."

        # Set direction based off of inputted argument.
        newRoom = currentRoom.getExitByDirection(uInput)

        # If none of these were found, the player may have inputted a room identifier.
        if newRoom == None:
            if args[0] in ['in', 'to', 'into', 'inside', 'outside']:
                newRoom = currentRoom.getExitByIdentifier(uInput)

                # If the statement 'move/go inside/outside' was used, state a name is required.
                if newRoom == None and len(args) == 1:
                    return "Where exactly do you want to " + verb + " " + args[0] + "?"

                # Room movement will not occur if the room wasn't found, or if the specified room isn't inside or outside when such argument is used.
                if newRoom == None or args[0] == 'inside' and currentRoom.exitHasAttribute(newRoom, 'inside') == False or args[0] == 'outside' and currentRoom.exitHasAttribute(newRoom, 'outside') == False:
                    return "You don't see any such place to " + verb + "."

            # In this case, no proper arguments were inputted.
            else:
                return 'Where do you want to ' + verb + '?'

        # Perform movement if successful.
        currentRoom = data.rooms[newRoom]
        return currentRoom.getRoomDescription()


    # ENTER - Player travels to an adjacent room that is inside.
    # Format: 'enter {room: inside}'
    if verb == 'enter':
        # See which direction the specified room is from the current room.
        newRoom = currentRoom.getExitByIdentifier(uInput)

        # Room movement will not occur if the room wasn't found.
        if newRoom == None:
            return "You don't see any such place to enter."

        # If the room is inside, enter it. If the room is outside, exit the current room into it.
        if currentRoom.exitHasAttribute(newRoom, 'inside'):
            currentRoom = data.rooms[newRoom]
            return currentRoom.getRoomDescription()
        # In this case, the new room is not inside if entering or outside if exiting.
        else:
            return "You can't enter anything that way."


    # CLIMB - Player travels upwards or downwards, or in the direction a ladder heads.
    # Format: 'climb up/down/ladder'
    if verb == 'climb':
        newRoom = None
        # Set direction to upwards.
        if 'up' in uInput or 'down' in uInput:
            newRoom = currentRoom.getExitByDirection(uInput)
        # Set direction to the ladder's destination.
        elif 'ladder' in args:
            newRoom = currentRoom.getExitByAttribute('ladder')

        # In this case, no proper arguments were inputted.
        if newRoom == None:
            return "You can't climb that way."

        # Perform movement if successful.
        currentRoom = data.rooms[newRoom]
        return currentRoom.getRoomDescription()

    """
    # GET (P,O) - Adds an item to the player's inventory.
    # Format: 'get {item}'
    if verb == 'get':
        for i in iteminfo.items:

            # If the item is referenced, and it is in the current room,
            if i.get("name") in args or any(s in args for s in i.get("alt-names")):
                if i.get("location") == roomhandler.currentRoom:

                    # And the item is collectable,
                    if i.get("collectable"):

                        # And there is room in the player's inventory,
                        if player.currentInvWeight + i.get("weight") <= player.maxInvWeight:
                            # Add the item and its weight to the player's inventory.
                            player.inventory.append(i.get("name"))
                            player.currentInvWeight += i.get("weight")

                            i["location"] = 0

                            return i["interactions"]["get"]

                        # There isn't enough room in the player's inventory.
                        else:
                            return "You're carrying too much."

                    # The item is not collectable.
                    else:
                        return "You can't get that."

        # The item is not in the current room, or no correct item names were inputted.
        return "You don't see any such thing to get."


    # EXAMINE (P) - Display full description of a room or item as requested by the player.
    # Format:
    # 'Examine room'
    # 'Examine {item}'
    if verb == 'examine' or verb == 'look':
        # If looking at the room, return the current room's large description.
        if 'room' in args or verb == 'look' and len(args) == 0:
            return roominfo.rooms[roomhandler.currentRoom]["desc-large"]
        # If the wrong grammar is used, tell the player.
        elif verb == 'look' and args[0] != 'at':
            return "What do you want to look at?"
        # Otherwise, an item name may have been inputted.
        else:
            for o in iteminfo.items:
                # If the item is referenced, and it is in the current room or in the player's inventory,
                if o.get("name") in args or any(s in args for s in o.get("alt-names")):
                    if o.get("location") == roomhandler.currentRoom or o.get("name") in player.inventory:
                        # Print the item description.
                        return o["desc-examine"]

            # In this case, no proper arguments were inputted.
            return "You don't see any such thing to examine."

    # SIT (P) - If there is something in the room to sit in, the player will sit down.
    # Format:
    # 'Sit down'
    # 'Sit in {item}'
    if verb == 'sit':
        # Check for an item in the current room that the player can sit in.
        for o in iteminfo.items:
            # If the player inputs the name of the item,
            if 'down' in args or o.get("name") in args or any(s in args for s in o.get("alt-names")):
                # If the item has the ability to sit in and is in the room, and the player isn't already sitting,
                if "sit" in o.get("interactions").keys() and o.get("location") == roomhandler.currentRoom:
                    if player.isSeated:
                        return "You're already sitting down."
                    else:
                        # Sit the player down, and return the sitting interaction message.
                        player.isSeated = True
                        player.currentObj = o.get("name")
                        return o["interactions"]["sit"]

        return "You don't see anywhere comfortable to sit."


    # STAND (P) - If the player is sitting, they will stand up.
    if verb == 'stand':
        #If the player is sitting,
        if player.isSeated:
            # They will stand up.
            player.isSeated = False
            # Find the item the player is currently interacting with (the chair).
            for o in iteminfo.items:
                if o.get("name") == player.currentObj:
                    # Reset the item.
                    player.currentObj = 0
                    o["turnsSeated"] = 0
                    # Return the stand message from the seat.
                    return o["interactions"]["stand"]
        else:
            return "You're already standing up."

    # WAIT (P) - No action is performed.
    # Format:
    # '' (No input)
    # 'Wait'
    if verb == 'wait':
        outTxt = "..."
        # If the player is sitting down, advance the turns seated counter.
        if player.isSeated:
            # Find the item the player is currently interacting with (the chair).
            for o in iteminfo.items:
                if o.get("name") == player.currentObj:
                    # Advance the counter.
                    o["turnsSeated"] += 1

                    # If the turn equals the value denoted in the key of the 'wait' interaction, output the text.
                    for k in o.get("interactions").keys():
                        if k == "wait-" + str(o.get("turnsSeated")):
                            outTxt += '\n' + o["interactions"][k]

        return outTxt

    """
    # DEBUG: Stop command exits the game.
    # TODO: Add final exit command that asks for the player's confirmation to exit.
    if verb == 'exit':
        return "Thanks for playing!"

    # If no defined verb was found, it isn't a known action.
    return "That isn't something you know how to do."
