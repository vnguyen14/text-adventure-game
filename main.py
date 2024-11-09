from Modules.room import Room
from game_engine import home_logic
from Modules.item import Item  # Import the Item class

# Load rooms and items data from json files
rooms = Room.load_rooms('rooms.json')
items = Item.load_items('items.json')

# Get home room from rooms: next() find the first room where name == 'Home' and stop there
home_room = next(room for room in rooms.values() if room.name == "Home")

# Start the day in the Home room
home_logic.start_home_room(home_room, items)

# Game loop for user's commands/actions in Home
while True:
    command = input("> ")
    if command in ["quit", "exit"]:
        print("Thanks for playing!")
        break
    home_logic.process_home_command(command, home_room, items)
