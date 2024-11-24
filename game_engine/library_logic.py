'''
import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
'''

from Modules.room import Room
from Modules.item import Item

# Array to store all collected items from take action
collected_items = []

# Helper function to talk to Mrs. Henderson
def talk_to_mrs_henderson():
    print("'Let me know if you need any help finding anything—books, supplies, equipment—anything!'")

def find_items(keyword=None, available_items=None):
    search_results = [
        item.name for item in available_items
        if keyword.lower() in item.name.lower() or not keyword
    ]
    if search_results:
        print(f"Let me see what I can find! Here you go: {', '.join(search_results)}")
    else:
        print("Sorry dear, I couldn't find anything matching that word.")

# Helper function to process 'take item' action
def take_item(item_name, available_items):
    item_names = {item.name.lower(): item for item in available_items}  # Map item names to item objects

    if item_name.lower() in item_names:
        collected_items.append(item_name.lower())
        item = item_names[item_name.lower()]
        
        # Special interactions for specific items
        if item_name.lower() == "camera battery":
            if "camera" in collected_items:
                print("You carefully slot it into the camera, and with a satisfying click, it powers on! Now, you're ready to capture moments throughout the game.")
            else:
                print(f"'{item.name}' is in your bag! You'll need a camera to use this.")
        elif item_name.lower() == "what in carnations? a guide to flowers":
            print(f"'{item.name}' is in your bag! You can't wait to dive into its colourful pages.")
        else:
            # Default action for other items
            print(f"'{item.name}' is in your bag!")
        # Need a function to update location to 0 in items.json (0 for in user inventory; similarly need code to update location if NPC has item)
    else:
        print("Mrs. Henderson: Sorry dear, I couldn't find that item in the library.")

# Helper function to process user's commands from the prompt/terminal
def process_library_command(command, library, items):
    available_items = Item.get_items_in_room(library.id, items)
    
    words = command.lower().split()
    action = words[0]
    parameter = ' '.join(words[1:]) if len(words) > 1 else None

    if action == "talk" and parameter == "mrs. henderson":
        talk_to_mrs_henderson()
    elif action == "find":
        find_items(parameter or "", available_items)
    elif action == "take" and parameter:
        take_item(parameter, available_items)
    else:
        print("I don't understand that command.")

# Start the room
def start_library(current_room, items):
    # library = rooms[5]
    # Create list of items currently in room
    # available_items = Item.get_items_in_room(current_room.id, items)
    # Print long or short description depending on visited status
    current_room.print_description()

'''
# Test for running isolated room
    while True:
        command = input("\n> ").strip()
        if command.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break
        process_library_command(command, current_room, available_items)

if __name__ == "__main__":
    # Dynamically determine paths to assets
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assets_dir = os.path.join(base_dir, "Assets")

    # Load rooms and items from the Assets directory
    rooms = Room.load_rooms(os.path.join(assets_dir, 'rooms.json'))
    items = Item.load_items(os.path.join(assets_dir, 'items.json'))

    start_library()
'''