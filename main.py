# main.py
from Modules.room import Room
from game_engine import home_logic, flowerShop_logic, bakery_logic, restaurant_logic, library_logic, neighbours_logic, park_logic
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
    print("You can't go that way.")


# Function to handle entering a room and starting its specific logic
def enter_room():
    """Displays the appropriate room details and starts room-specific logic."""
    room_name = current_room.name

    if room_name == "Home":
        home_logic.start_home_room(current_room, items)
    elif room_name == "Jeremy's Bakery":
        bakery_logic.start_bakery(current_room, items)
    elif room_name == "Florence's Flower Shop":
        flowerShop_logic.start_flower_shop(current_room, items)
    else:
        print(f"You've entered an unknown room: {room_name}")


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
        print(manual)
    elif action == "inspect":
        if parameter == "phone":
            home_logic.inspect_phone(game_state)
        else:
            print("Inspect what?")
    elif action in ["n", "s", "e", "w"]:
        move_player(action)
    else:
        if current_room.name == "Home":
            home_logic.process_home_command(command, current_room, items, game_state)
        elif current_room.name == "Jeremy's Bakery":
            bakery_logic.process_bakery_command(command, current_room, items, game_state)
