from Modules.room import Room
from Modules.item import Item

# Array to store all collected items from take action
collected_items = []

# Check if events have already occurred
tea_served = False
flowers_delivered = False
box_offered = False
box_emptied = False

# Overall order of events = Drink Tea, Receive Box, Inspect box for contents, continue. Talking to Smiths optional


def give_flowers():
    global flowers_delivered

    if flowers_delivered:
        print("You have already given flowers to the Smiths.")
        return
    if "hydrangeas" or "roses" not in collected_items:
        print("You do not have any flowers to give to the Smiths.")
        return
    elif "hydrangeas" in collected_items:
        collected_items.remove("hydrangeas")
    elif "roses" in collected_items:
        collected_items.remove("roses")
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

def take_box():
    if not tea_served:
        print("Mrs. Smith: Why not sit down for some tea?")
        return
    else:
        if "box" in collected_items:
            print("You already have the box of old stuff from the Smiths with you.")
        else:
            collected_items.append("Box")
            print("Mrs. Smith hands you a small box filled with odd bits and ends.")

def inspect_box():
    global box_emptied
    if box_emptied:
        print("You have already taken out the items from the box Mrs. Smith gave to you.")
    else:
        collected_items.extend(["Leash", "Camera", "Baseball Glove", "Doll", "Scarf"])
        print("You pull out an old leash, a vintage camera, a faded baseball glove, a delicate porcelain doll,\nand a cozy scarf. Each piece surely holds a story waiting to be discovered.")
        print("Leash, Camera, Baseball Glove, Doll, Scarf are in your bag!")

def inspect_camera():
    if "Camera" in collected_items:
        print("This will surely help in capturing some memories on today’s journey! But wait—it's missing a battery.")
    else:
        print("Are you sure you have one yet?")

def capture_camera():
    if "Camera Battery" not in collected_items:
        print("Oh darn! The camera is missing a battery.")
    else:
        print("You took a picture of the scene in front of you.")

def start_neighbours(room, items):
    available_items = Item.get_items_in_room(room.id, items)
    print(f"Items in this room: {[item.name for item in available_items]}")


    if room.first_time_in_room:
        room.print_long_description()
        room.change_first_time_status()
    else:
        room.print_short_description()

# Process commands for neighbour room
def neighbours_command(command, room, items):
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
            take_box()
        else:
            print("What are you trying to take?")
    elif action == "inspect":
        if item_name == "box":
            inspect_box()
        elif item_name == "camera":
            inspect_camera()

