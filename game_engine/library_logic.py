'''
import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
'''

from Modules.room import Room
from Modules.item import Item

# Array to store all collected items from take action
# collected_items = []

# Helper function to talk to Mrs. Henderson
def talk_to_mrs_henderson():
    print("'Let me know if you need any help finding anything—books, supplies, equipment—anything!'")

def find_items(keyword=None, available_items=None):
    search_results = [
        item.name for item in available_items
        if keyword.lower() in item.name.lower() or not keyword
    ]
    if search_results:
        sorted_results = sorted(search_results)  # Sort the list alphabetically
        print("Let me see what I can find! Here you go:\n- " + "\n- ".join(sorted_results))
    else:
        print("Sorry dear, I couldn't find anything matching that word.")

# Helper function to process 'take item' action
def take_item(item_name, available_items, game_state):
    item_names = {item.name.lower(): item for item in available_items}  # Map item names to item objects
    if item_name.lower() in item_names:
        if item_name.lower() in game_state.collected_items:
            print(f"'{item_name}' is in your bag!")
        else:
            game_state.collected_items.append(item_name.lower())
            item = item_names[item_name.lower()]
            
            # Special interactions for specific items
            if item_name.lower() == "camera battery":
                if "camera" in game_state.collected_items:
                    print("You carefully slot it into the camera, and with a satisfying click, it powers on! Now, you're ready to capture moments throughout the game.")
                else:
                    print(f"'{item.name}' is in your bag! You'll need a camera to use this.")
            elif item_name.lower() == "what in carnations? a guide to flowers":
                print(f"'{item.name}' is in your bag! You can't wait to dive into its colourful pages.")
            else:
                # Default action for other items
                print(f"'{item.name}' is in your bag!")
    else:
        print("Mrs. Henderson: Sorry dear, I couldn't find that item in the library.")

# Helper function to process user's commands from the prompt/terminal
def process_library_command(command, library, items, game_state):
    available_items = Item.get_items_in_room(library.id, items)
    
    words = command.lower().split()
    action = words[0]
    parameter = ' '.join(words[1:]) if len(words) > 1 else None

    if action == "talk" and parameter == "mrs. henderson":
        talk_to_mrs_henderson()
    elif action == "find":
        find_items(parameter or "", available_items)
    elif action == "take" and parameter:
        take_item(parameter, available_items, game_state)
    else:
        print("I don't understand that command.")