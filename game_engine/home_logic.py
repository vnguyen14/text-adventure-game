from Modules.item import Item

#Array to store all collected items from take action
collected_items = []

# Start the room
def start_home_room(room, items):
    room.print_long_description() # print long description
    # get and print all items available in this room
    available_items = Item.get_items_in_room(room.id, items)
    print(f"Items in this room: {[item.name for item in available_items]}")


# Function to process 'take item' action
def take_item(item_name, room_id, items):
    available_items = Item.get_items_in_room(room_id, items)
    item_names = {item.name.lower() for item in available_items}  # Access name via item.name

    #Take all needed items: phone, key and wallet
    if item_name.lower() in item_names:
        if item_name.lower() not in collected_items:
            collected_items.append(item_name.lower())
            location = "pocket" if item_name.lower() in ["keys", "phone"] else "bag"
            print(f"{item_name.capitalize()} is in your {location}!")
        else:
            print(f"You already have the {item_name}.")
    else:
        print("Item not found in this room.")

    #If all items are collected/taken, print message to start the day
    if all_items_collected():
        print("Let's start the day! Buzz! There's a new message on your phone.")

# Helper function to check if all items re collected/taken
def all_items_collected():
    required_items = ["keys", "wallet", "phone"]
    return all(item in collected_items for item in required_items)


# Function to process 'inspect phone' action
def inspect_phone():
    if "phone" in collected_items:
        print("There's a message from Jeremy: 'I have a favor to ask! One of my workers fell sick. Can you pick up some last-minute groceries for me? I need…” You can't make sense of the rest of the message. It's probably best to speak to Jeremy in person.'")
    else:
        print("You don't have your phone yet!")


# Function to precess user's commands from the promt/terminal
def process_home_command(command, room, items):
    words = command.lower().split()
    action = words[0]
    item_name = ' '.join(words[1:]) if len(words) > 1 else None

    if action == "take" and item_name:
        take_item(item_name, room.id, items)
    elif action == "inspect" and item_name == "phone":
        inspect_phone()
    else:
        print("I don't understand that command.")