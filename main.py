from Modules.room import Room
from game_engine import home_logic, flowerShop_logic, restaurant_logic, library_logic, neighbours_logic, park_logic
from Modules.item import Item
from Modules.action import Action
from game_engine.neighbours_logic import neighbours_command

# Load rooms, actions and items data from json files
rooms = Room.load_rooms('rooms.json')
items = Item.load_items('items.json')
actions = Action.load_actions("actions.json")

# Get current room from rooms: next() find the first room where name == 'Home' and stop there
global current_room
current_room = next(room for room in rooms.values() if room.name == "Home")

# Start the game in the Home room
home_logic.start_home_room(current_room, items)

# Function to move between rooms
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

# Helper function to move rooms: start the room logic once the player enter the room
def enter_room():
    """Displays the appropriate room details and starts room-specific logic."""
    if current_room.name == "Florence's Flower Shop":
        flowerShop_logic.start_flower_shop(current_room, items)
    elif current_room.name == "Dina's Diner":
        restaurant_logic.start_restaurant(current_room)
    elif current_room.name == "Lore Library":
        library_logic.start_library(current_room, items)
    else:
        home_logic.start_home_room(current_room, items)


# Game loop for user's commands/actions
while True:
    command = input("> ").strip().lower()
    if command in ["quit", "exit"]:
        print("Thanks for playing!")
        break
    elif command == "man":
        manual = Action.print_game_manual(actions)
        print(manual) #display manual
    elif command in ["n", "s", "e", "w"]:
        move_player(command)
    elif current_room.name == "Home":
        home_logic.process_home_command(command, current_room, items)
    elif current_room.name == "Florence's Flower Shop":
        flowerShop_logic.process_flower_shop_command(command, current_room, items)
    elif current_room.name == "Lore Library":
        library_logic.process_library_command(command, current_room, items)
    elif current_room.name == "Neighbour's House":
        neighbours_logic.neighbours_command(command, current_room, items)
    elif current_room.name == "The Park":
        park_logic.park_command(command, current_room, items)
    else:
        print("Invalid command.")

