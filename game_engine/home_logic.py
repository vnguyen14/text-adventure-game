from Modules.item import Item

#Array to store all collected items from take action
#collected_items = []

# Function to process 'take item' action
def take_item(item_name, room_id, items, game_state):
    available_items = Item.get_items_in_room(room_id, items)
    item_names = {item.name.lower() for item in available_items}  # Access name via item.name

    #Take all needed items: phone, key and wallet
    if item_name.lower() in item_names:
        if item_name.lower() not in game_state.collected_items:
            game_state.collected_items.append(item_name.lower())
            location = "pocket" if item_name.lower() in ["keys", "phone"] else "bag"
            print(f"\n{item_name.capitalize()} is in your {location}!\n")
        else:
            print(f"\nYou already have the {item_name}.\n")
    else:
        print("\nItem not found in this room.\n")

    #If all items are collected/taken, print message to start the day
    if all_items_collected(game_state):
        print("Let's start the day! Buzz! There's a new message on your phone.\n")

# Helper function to check if all items re collected/taken
def all_items_collected(game_state):
    required_items = ["keys", "wallet", "phone"]
    return all(item in game_state.collected_items for item in required_items)


# Function to process 'inspect phone' action
def inspect_phone(game_state):
    if "phone" in game_state.collected_items:
        print("There's a message from Jeremy: \n'I have a favor to ask! One of my workers fell sick. \nCan you pick up some last-minute groceries for me? I need…' \nYou can't make sense of the rest of the message. \nIt's probably best to speak to Jeremy in person.'")
    else:
        print("\nYou don't have your phone yet!\n")


# Function to precess user's commands from the promt/terminal
def process_home_command(command, room, items, game_state):
    words = command.lower().split()
    action = words[0]
    item_name = ' '.join(words[1:]) if len(words) > 1 else None

    if action == "take" and item_name:
        take_item(item_name, room.id, items, game_state)
    #elif action == "inspect" and item_name == "phone":
    #    inspect_phone(game_state)
    #else:
    #    print("I don't understand that command.")