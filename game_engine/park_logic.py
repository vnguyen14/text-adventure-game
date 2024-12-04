from Modules.room import Room
from Modules.item import Item

def take_max(game_state):
    if "max" in game_state.collected_items:
        print("\nMax has already joined your party.\n")
        return

    if "leash" in game_state.collected_items:
        print("\nYou clip your leash onto Max's collar, ready to guide him back to safety.")
        print("Max has joined your party!")
        print("Let's ask around to see where Mrs. Davis is.\n")
        game_state.collected_items.append("max")
    else:
        print("\nYou'll need a leash.\n")

def process_park_command(command, room, items,game_state):
    words = command.lower().split()
    action = words[0]
    item_name = ' '.join(words[1:]) if len(words) > 1 else None

    #if action == "inspect" and item_name == "max":
    #    inspect_max()
    if action == "take" and item_name == "max":
        #print(game_state.collected_items)
        take_max(game_state)
