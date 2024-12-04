from Modules.room import Room
from Modules.item import Item

# Array to store all collected items from take action
# collected_items = []

# Check if events have already occurred
tea_served = False
flowers_delivered = False
box_offered = False
box_emptied = False

# Overall order of events = Drink Tea, Receive Box, Inspect box for contents, continue. Talking to Smiths optional


def give_flowers(game_state):
    global flowers_delivered

    if flowers_delivered:
        print("\nYou have already given flowers to the Smiths.\n")
        return
    if "hydrangeas" or "roses" not in game_state.collected_items:
        print("\nYou do not have any flowers to give to the Smiths.\n")
        return
    elif "hydrangeas" in game_state.collected_items:
        game_state.collected_items.remove("hydrangeas")
    elif "roses" in game_state.collected_items:
        game_state.collected_items.remove("roses")
    flowers_delivered = True

    print("\nThe Smiths are very happy to receive them.\n")

def take_tea():
    global tea_served
    if tea_served:
        print("\nMrs. Smith has already served you tea.\n")
        return
    tea_served = True
    print("\nMrs. Smith pours you some tea.\n")

def talk_to_smiths():
    global box_offered
    if tea_served:
        if not box_offered:
            print("\nYou: This smells lovely. Thank you for your kindness Mrs. Smith.")
            print("Mrs. Smith: Wonderful! I'm glad you like it. Oh and by the way, we cleaned the house\nthe past few days to clear up some of the clutter.\nWe kept some useful stuff in this box for donation.\n")
            box_offered = True
        else:
            print("\nHave you taken a look at what's inside the box?\n")
    else:
        print("\nHow about some tea?\n")

def take_box(game_state):
    if not tea_served:
        print("\nMrs. Smith: Why not sit down for some tea?\n")
        return
    else:
        if "box" in game_state.collected_items:
            print("\nYou already have the box of old stuff from the Smiths with you.\n")
        else:
            game_state.collected_items.append("box")
            print("\nMrs. Smith hands you a small box filled with odd bits and ends.\n")

def inspect_box(game_state):
    global box_emptied
    if box_emptied:
        print("\nYou have already taken out the items from the box Mrs. Smith gave to you.\n")
    else:
        game_state.collected_items.extend(["leash", "camera", "baseball glove", "doll", "scarf"])
        box_emptied = True
        print("\nYou pull out an old leash, a vintage camera, a faded baseball glove, a delicate porcelain doll,\nand a cozy scarf. Each piece surely holds a story waiting to be discovered.")
        print("Leash, Camera, Baseball Glove, Doll, Scarf are in your bag!\n")

def inspect_camera(game_state):
    if "camera" in game_state.collected_items:
        print("\nThis will surely help in capturing some memories on today's journey! But wait--it's missing a battery.\n")
    else:
        print("\nAre you sure you have one yet?\n")

def capture_camera(game_state):
    if "camera battery" not in game_state.collected_items:
        print("\nOh darn! The camera is missing a battery.\n")
    else:
        print("\nYou take a picture of the scene in front of you.\n")

# Process commands for neighbour room
def neighbours_command(command, room, items,game_state):
    words = command.lower().split()
    action = words[0]
    item_name = ' '.join(words[1:]) if len(words) > 1 else None


    if action == "talk":
        if item_name == "to smiths":
            talk_to_smiths()
        else:
            print("\nThere's no one else in the room.\n")
    elif action == "take":
        if item_name == "tea":
            take_tea()
        elif item_name == "box":
            take_box(game_state)
        else:
            print("\nWhat are you trying to take?\n")
    elif action == "inspect":
        if item_name == "box":
            inspect_box(game_state)
        elif item_name == "camera":
            inspect_camera(game_state)
        else:
            # Check if the item is in the collected items (case-insensitive)
            if any(collected_item.lower() == item_name for collected_item in game_state.collected_items):
                # Fetch the actual Item object from the items dictionary
                item = next((item for item in items.values() if item.name.lower() == item_name.lower()), None)
                if item:
                    item.get_description()
            else:
                print(f"\nItem '{item_name}' is not in your inventory.\n")
    else:
        print("\nInvalid action.\n")

