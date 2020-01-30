# COMMANDHANDLER
# Brackets denote a command is usable by Player (P), or Object (O).
# a/b = Interchangable verbs or arguments.
# a|b = Respective verbs and arguments.

import roomhandler
import data.roominfo as roominfo
import data.objectinfo as objectinfo
import data.playerinfo as player

# Parses and interprets player inputs.
def interpretCmd(inputTerms):
    user = inputTerms[0]
    verb = inputTerms[1]
    args = inputTerms[2:]

    # MOVE/GO (P,O) - Player travels to an adjacent room, and the new room's description is outputted.
    # Format:
    # 'move/go {direction}'
    # 'move/go in/to/into {room}'
    # 'move/go inside|outside {room: inside|outside}'
    if verb == 'move' or verb == 'go':
        # Don't allow movement if the player is seated.
        if player.isSeated:
            return "You can't " + verb + " anywhere while sitting down."

        # Set direction based off of inputted argument.
        if 'north' in args or 'forward' in args:
            dr = 0
        elif 'east' in args or 'right' in args:
            dr = 1
        elif 'south' in args or 'back' in args:
            dr = 2
        elif 'west' in args or 'left' in args:
            dr = 3
        elif 'up' in args or 'upwards' in args:
            dr = 4
        elif 'down' in args or 'downwards' in args:
            dr = 5

        # If none of these were found, the player may have inputted a room identifier.
        else:
            if args[0] in ['in', 'to', 'into', 'inside', 'outside']:
                # See which direction the specified room is from the current room.
                dr = roomhandler.getDirection(args[1:])

                # Room movement will not occur if the room wasn't found, or if the specified room isn't inside or outside when such argument is used.
                if dr == -1 or args[0] == 'inside' and 'inside' not in roominfo.rooms[roomhandler.currentRoom]["attributes"][dr] or args[0] == 'outside' and 'outside' not in roominfo.rooms[roomhandler.currentRoom]["attributes"][dr] :
                    return "You don't see any such place to " + verb + "."

            # In this case, no proper arguments were inputted.
            else:
                return 'Where do you want to ' + verb + '?'

        # Perform movement if successful.
        return roomhandler.move(dr)

    # ENTER/EXIT (P) - Player travels to an adjacent room that is either inside when enterring, or outside when exiting.
    # Format: 'enter|exit {room: inside|outside}'
    if verb == 'enter' or verb == 'exit':
        # See which direction the specified room is from the current room.
        dr = roomhandler.getDirection(args)

        # Room movement will not occur if the room wasn't found.
        if dr == -1:
            return "You don't see any such place to " + verb + "."

        # Set the attribute to search for based on the command.
        position = 'inside' if verb == 'enter' else 'outside'

        # TODO: Output "You're already outside." if the player tries to exit while outside.

        # If the room is inside, enter it. If the room is outside, exit the current room into it.
        if position in roominfo.rooms[roomhandler.currentRoom]["attributes"][dr]:
            return roomhandler.move(dr)
        # In this case, the new room is not inside if entering or outside if exiting.
        else:
            return "You can't " + verb + " anything that way."
    
    # CLIMB (P) - Player travels upwards or downwards, or in the direction a ladder heads.
    # Format: 'climb up/down/ladder'
    if verb == 'climb':
        # Set direction to upwards.
        if 'up' in args or 'upwards' in args:
            dr = 4
        # Set direction to downwards.
        elif 'down' in args or 'downwards' in args:
            dr = 5
        # Set direction to the ladder's destination.
        elif 'ladder' in args:
            # If there is a ladder in the room, climb in the direction it goes.
            for r in range(2):
                if 'ladder' in roominfo.rooms[roomhandler.currentRoom]["attributes"][4 + r]:
                    dr = 4 + r
        # In this case, no proper arguments were inputted.
        else:
            return "You can't climb that way."

        # Perform movement if successful.
        return roomhandler.move(dr)

    # EXAMINE (P) - Display full description of a room or object as requested by the player.
    # Format:
    # 'Examine room'
    # 'Examine {object}'
    if verb == 'examine':
        # If looking at the room, return the current room's large description.
        if 'room' in args:
            return roominfo.rooms[roomhandler.currentRoom]["desc-large"]
        # Otherwise, an object name may have been inputted.
        else:
            for o in objectinfo.objects:
                # If the object is referenced, and it is in the current room,
                if o.get("name") in args or any(s in args for s in o.get("alt-names")):
                    if o.get("location") == roomhandler.currentRoom:
                        # Print the object description.
                        return o["desc-examine"]

            # In this case, no proper arguments were inputted.
            return "You don't see any such thing to examine."

    # SIT (P) - If there is something in the room to sit in, the player will sit down.
    # Format:
    # 'Sit down'
    # 'Sit in {object}'
    if verb == 'sit':
        # Check for an object in the current room that the player can sit in.
        for o in objectinfo.objects:
            # If the player inputs the name of the object,
            if 'down' in args or o.get("name") in args or any(s in args for s in o.get("alt-names")):
                # If the object has the ability to sit in and is in the room, and the player isn't already sitting,
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
            # Find the object the player is currently interacting with (the chair).
            for o in objectinfo.objects:
                if o.get("name") == player.currentObj:
                    # Reset the object.
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
            # Find the object the player is currently interacting with (the chair).
            for o in objectinfo.objects:
                if o.get("name") == player.currentObj:
                    # Advance the counter.
                    o["turnsSeated"] += 1

                    # If the turn equals the value denoted in the key of the 'wait' interaction, output the text.
                    for k in o.get("interactions").keys():
                        if k == "wait" + str(o.get("turnsSeated")):
                            outTxt += '\n' + o["interactions"][k]

        return outTxt

    # DEBUG: Stop command exits the game.
    # TODO: Add final exit command that asks for the player's confirmation to exit.
    if verb == 'stop':
        return "Thanks for playing!"

    # If no defined verb was found, it isn't a known action.
    return "That isn't something you know how to do."
