from Modules.room import Room
from Modules.item import Item

# Helper function to talk to Mrs. Henderson
def talk_to_mrs_henderson():
    print("\nLet me know if you need any help finding anything—books, supplies, equipment—anything!\n")

def find_items(keyword=None, available_items=None):
    search_results = [
        item.name for item in available_items
        if keyword.lower() in item.name.lower() or not keyword
    ]
    if search_results:
        sorted_results = sorted(search_results)  # Sort the list alphabetically
        print("\nLet me see what I can find! Here you go:\n- " + "\n- ".join(sorted_results) + "\n")
    else:
        print("\nSorry dear, I couldn't find anything matching that word.\n")

# Helper function to process 'take item' action
def take_item(item_name, available_items, game_state):
    item_names = {item.name.lower(): item for item in available_items}  # Map item names to item objects
    if item_name.lower() in item_names:
        if item_name.lower() in game_state.collected_items:
            print(f"\n'{item_name}' is in your bag!\n")
        else:
            game_state.collected_items.append(item_name.lower())
            item = item_names[item_name.lower()]
            
            # Special interactions for specific items
            if item_name.lower() == "camera battery":
                if "camera" in game_state.collected_items:
                    print("\nYou carefully slot it into the camera, and with a satisfying click, it powers on! Now, you're ready to capture moments throughout the game.\n")
                else:
                    print(f"\n'{item.name}' is in your bag! You'll need a camera to use this.\n")
            elif item_name.lower() == "what in carnations? a guide to flowers":
                print(f"\n'{item.name}' is in your bag! You can't wait to dive into its colourful pages.\n")
            else:
                # Default action for other items
                print(f"\n'{item.name}' is in your bag!\n")
    else:
        print("\nSorry dear, I couldn't find that item in the library.\n")

# Helper function to process user's commands from the prompt/terminal
def process_library_command(command, room, items, game_state):
    available_items = Item.get_items_in_room(room.id, items)
    
    words = command.lower().split()
    action = words[0]
    parameter = ' '.join(words[1:]) if len(words) > 1 else None

    if action == "talk" and parameter == "to mrs. henderson":
        talk_to_mrs_henderson()
    elif action == "find":
        find_items(parameter or "", available_items)
    elif action == "take" and parameter:
        take_item(parameter, available_items, game_state)
    else:
        print("\nI don't understand that command.\n")