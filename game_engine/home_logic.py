# game_engine/home_logic.py
from Modules.item import Item

# Start the room
def start_home_room(room, items):
    room.print_long_description()  # print long description
    # get and print all items available in this room
    available_items = Item.get_items_in_room(room.id, items)
    print(f"Items in this room: {[item.name for item in available_items]}")


# Function to process 'take item' action
def take_item(item_name, room_id, items, game_state):
    available_items = Item.get_items_in_room(room_id, items)
    item_names = {item.name.lower() for item in available_items}  # Access name via item.name

    # Take all needed items: phone, key, and wallet
    if item_name.lower() in item_names:
        if item_name.lower() not in game_state.collected_items:
            game_state.collected_items.append(item_name.lower())
            location = "pocket" if item_name.lower() in ["keys", "phone"] else "bag"
            print(f"{item_name.capitalize()} is in your {location}!")
        else:
            print(f"You already have the {item_name}.")
    else:
        print("Item not found in this room.")

    # If all items are collected/taken, print message to start the day
    if all_items_collected(game_state):
        game_state.phone_message = ("There's a message from Jeremy: "
                                     "'I have a favor to ask! One of my workers fell sick. "
                                     "Can you pick up some last-minute groceries for me? "
                                     "I need…' It's probably best to speak to Jeremy in person.")
        print("Let's start the day! Buzz! There's a new message on your phone.")


# Helper function to check if all items are collected/taken
def all_items_collected(game_state):
    required_items = ["keys", "wallet", "phone"]
    return all(item in game_state.collected_items for item in required_items)


# Function to process 'inspect phone' action
def inspect_phone(game_state):
    if "phone" in game_state.collected_items:
        if game_state.phone_message:
            print(f"You inspect your phone. {game_state.phone_message}")
        else:
            print("Your phone has no new messages.")
    else:
        print("You don't have your phone yet!")


# Function to process user's commands
def process_home_command(command, room, items, game_state):
    words = command.lower().split()
    action = words[0]
    item_name = ' '.join(words[1:]) if len(words) > 1 else None

    if action == "take" and item_name:
        take_item(item_name, room.id, items, game_state)
    elif action == "inspect" and item_name == "phone":
        inspect_phone(game_state)
    else:
        print("I don't understand that command.")