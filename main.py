from Modules.room import Room
from game_engine import home_logic, flowerShop_logic, bakery_logic, restaurant_logic, library_logic, neighbours_logic, park_logic, retirementHome_logic
from Modules.item import Item
from Modules.action import Action
from Modules.game_state import GameState

# Load rooms, actions, and items data from JSON files
rooms = Room.load_rooms('rooms.json')
items = Item.load_items('items.json')
actions = Action.load_actions("actions.json")
game_state = GameState()

# Get the initial room (Home)
global current_room
current_room = next(room for room in rooms.values() if room.name == "Home")
current_phone_message = None  # Global phone message

# Room-specific logic handlers
room_inspect_handlers = {
    "Jeremy's Bakery": bakery_logic.process_bakery_command,
    "Neighbour's House": neighbours_logic.neighbours_command,
}

room_command_handlers = {
    "Home": home_logic.process_home_command,
    "Jeremy's Bakery": bakery_logic.process_bakery_command,
    "Florence's Flower Shop": flowerShop_logic.process_flower_shop_command,
    "Lore Library": library_logic.process_library_command,
    "Neighbour's House": neighbours_logic.neighbours_command,
    "The Park": park_logic.process_park_command,
    "Dina's Diner": restaurant_logic.process_restaurant_command,
    "Retirement Home": retirementHome_logic.process_retirementHome_command,
}

# Function to handle movement between rooms
def move_player(direction):
    """Moves the player in the specified direction if a connection exists."""
    global current_room
    for connection in current_room.connections:
        if connection["direction"] == direction:
            new_room_id = connection["roomID"]
            current_room = rooms[new_room_id]
            enter_room()
            return
    print("\nYou can't go that way.\n")


# Function to handle entering a room and starting its specific logic
def enter_room():
    """Displays the appropriate room details and starts room-specific logic."""
    room_name = current_room.name

    # Match the room to its specific logic module
    if room_name in ("Home", "Jeremy's Bakery", "Neighbour's House"):
        Room.start_room(current_room, items)
    elif room_name == "Florence's Flower Shop":
        flowerShop_logic.start_flower_shop(current_room, items, game_state.collected_items)
    else:
        Room.start_room(current_room)

def inspect_item(parameter):
    """Handles the 'inspect' command."""
    item = next((item for item in items.values() if item.name.lower() == parameter.lower()), None)
    if parameter in game_state.collected_items:
        item.get_description()
    else:
        print(f"\nItem '{parameter}' is not in your inventory.\n")

# Start the game in the Home room
enter_room()

# Game loop for handling user commands
while True:
    command = input("> ").strip().lower()
    words = command.split()
    action = words[0]
    parameter = ' '.join(words[1:]) if len(words) > 1 else None

    if action in ["quit", "exit"]:
        print("Thanks for playing!")
        break
    elif action == "man":
        manual = Action.print_game_manual(actions)
        print(manual)  # Display the manual
    elif action == "inventory":
        print("\nHere's what you have:\n- " + "\n- ".join(sorted(game_state.collected_items)) + "\n")
    elif action == "inspect":
        # Check if the room has a custom command for 'inspect'
        if current_room.name in room_inspect_handlers:
            room_inspect_handlers[current_room.name](command, current_room, items, game_state)
        else:
            inspect_item(parameter)
    elif action in ["n", "s", "e", "w", "se"]:
        move_player(action)
    else:
        handler = room_command_handlers.get(current_room.name)
        if handler:
            handler(command, current_room, items, game_state)
        else:
            print("Invalid command.")
