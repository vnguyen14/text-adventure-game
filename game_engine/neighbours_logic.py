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
        print("You have already given flowers to the Smiths.")
        return
    if "hydrangeas" or "roses" not in game_state.collected_items:
        print("You do not have any flowers to give to the Smiths.")
        return
    elif "hydrangeas" in game_state.collected_items:
        game_state.collected_items.remove("hydrangeas")
    elif "roses" in game_state.collected_items:
        game_state.collected_items.remove("roses")
    flowers_delivered = True

    print("The Smiths are very happy to receive them.")

def take_tea():
    global tea_served
    if tea_served:
        print("Mrs. Smith has already served you tea.")
        return
    tea_served = True
    print("Mrs. Smith pours you some tea.")

def talk_to_smiths():
    global box_offered
    if tea_served:
        if not box_offered:
            print("You: This smells lovely. Thank you for your kindness Mrs. Smith.")
            print("Mrs. Smith: Wonderful! I'm glad you like it. Oh and by the way, we cleaned the house\nthe past few days to clear up some of the clutter.\nWe kept some useful stuff in this box for donation.")
            box_offered = True
        else:
            print("Have you taken a look at what's inside the box?")
    else:
        print("How about some tea?")

def take_box(game_state):
    if not tea_served:
        print("Mrs. Smith: Why not sit down for some tea?")
        return
    else:
        if "box" in game_state.collected_items:
            print("You already have the box of old stuff from the Smiths with you.")
        else:
            game_state.collected_items.append("box")
            print("Mrs. Smith hands you a small box filled with odd bits and ends.")

def inspect_box(game_state):
    global box_emptied
    if box_emptied:
        print("You have already taken out the items from the box Mrs. Smith gave to you.")
    else:
        game_state.collected_items.extend(["leash", "camera", "baseball glove", "doll", "scarf"])
        box_emptied = True
        print("You pull out an old leash, a vintage camera, a faded baseball glove, a delicate porcelain doll,\nand a cozy scarf. Each piece surely holds a story waiting to be discovered.")
        print("Leash, Camera, Baseball Glove, Doll, Scarf are in your bag!")

def inspect_camera(game_state):
    if "camera" in game_state.collected_items:
        print("This will surely help in capturing some memories on today's journey! But wait--it's missing a battery.")
    else:
        print("Are you sure you have one yet?")

def capture_camera(game_state):
    if "camera battery" not in game_state.collected_items:
        print("Oh darn! The camera is missing a battery.")
    else:
        print("You took a picture of the scene in front of you.")

# Process commands for neighbour room
def neighbours_command(command, room, items,game_state):
    words = command.lower().split()
    action = words[0]
    item_name = ' '.join(words[1:]) if len(words) > 1 else None


    if action == "talk":
        if item_name == "to smiths":
            talk_to_smiths()
        else:
            print("There's no one else in the room")
    elif action == "take":
        if item_name == "tea":
            take_tea()
        elif item_name == "box":
            take_box(game_state)
        else:
            print("What are you trying to take?")
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
                print(f"Item '{item_name}' is not in your inventory.")
    else:
        print("Invalid action.")

