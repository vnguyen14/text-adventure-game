# from Modules.room import Room
# from game_engine import home_logic

# # Load rooms and items
# rooms = Room.load_rooms('rooms.json')
# items = home_logic.load_items('items.json')

# # Start in the Home room
# home_room = next(room for room in rooms.values() if room.name == "Home")

# # Start the day in the Home room
# home_logic.start_home_room(home_room, items)

# # Game loop for commands
# while True:
#     command = input("> ")
#     if command in ["quit", "exit"]:
#         print("Thanks for playing!")
#         break
#     home_logic.process_home_command(command, home_room, items)

# main.py
from Modules.room import Room
from game_engine import home_logic
from Modules.Item import Item  # Import the Item class

# Load rooms and items
rooms = Room.load_rooms('rooms.json')
items = Item.load_items('items.json')  # Use Item's load_items method

# Start in the Home room
home_room = next(room for room in rooms.values() if room.name == "Home")

# Start the day in the Home room
home_logic.start_home_room(home_room, items)

# Game loop for commands
while True:
    command = input("> ")
    if command in ["quit", "exit"]:
        print("Thanks for playing!")
        break
    home_logic.process_home_command(command, home_room, items)
