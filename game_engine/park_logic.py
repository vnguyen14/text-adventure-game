from Modules.room import Room
from Modules.item import Item

#collected_items = []

def start_park(room, items):
    if room.first_time_in_room:
        room.print_long_description()
        room.change_first_time_status()
    else:
        room.print_short_description()

def inspect_max():
    print("Poor guy, he must be so scared. I should return him to Mrs. Davis.")

def take_max(game_state):
    if "max" in game_state.collected_items:
        print("Max has already joined your party.")
        return

    if "leash" in game_state.collected_items:
        print("You clip your leash onto Max's collar, ready to guide him back to safety.")
        print("Max has joined your party!")
        print("Let's ask around to see where Mrs. Davis is.")
        game_state.collected_items.append("max")
    else:
        print("You'll need a leash.")

def park_command(command, room, items,game_state):
    words = command.lower().split()
    action = words[0]
    item_name = ' '.join(words[1:]) if len(words) > 1 else None

    #if action == "inspect" and item_name == "max":
    #    inspect_max()
    if action == "take" and item_name == "max":
        print(game_state.collected_items)
        take_max(game_state)
