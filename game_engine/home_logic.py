from Modules.Item import Item

collected_items = []

def start_home_room(room, items):
    room.print_long_description()
    available_items = get_items_in_room(room.id, items)
    print(f"Items in this room: {[item.name for item in available_items]}")

def get_items_in_room(room_id, items):
    return [item for item in items.values() if room_id in item.location]

def take_item(item_name, room_id, items):
    available_items = get_items_in_room(room_id, items)
    item_names = {item.name.lower() for item in available_items}  # Access name via item.name

    if item_name.lower() in item_names:
        if item_name.lower() not in collected_items:
            collected_items.append(item_name.lower())
            location = "pocket" if item_name.lower() in ["keys", "phone"] else "bag"
            print(f"{item_name.capitalize()} is in your {location}!")
        else:
            print(f"You already have the {item_name}.")
    else:
        print("Item not found in this room.")

    if all_items_collected():
        print("Let’s start the day! Buzz! There’s a new message on your phone.")

def inspect_phone():
    if "phone" in collected_items:
        print("There’s a message from Jeremy: “I have a favor to ask! One of my workers fell sick. Can you pick up some last-minute groceries for me? I need…” You can’t make sense of the rest of the message. It’s probably best to speak to Jeremy in person.")
    else:
        print("You don't have your phone yet!")

def all_items_collected():
    required_items = ["keys", "wallet", "phone"]
    return all(item in collected_items for item in required_items)

def process_home_command(command, room, items):
    words = command.lower().split()
    action = words[0]
    item_name = ' '.join(words[1:]) if len(words) > 1 else None

    if action == "take" and item_name:
        take_item(item_name, room.id, items)
    elif action == "inspect" and item_name == "phone":
        inspect_phone()
    elif action in ["look", "description"]:
        start_home_room(room, items)
    else:
        print("I don't understand that command.")