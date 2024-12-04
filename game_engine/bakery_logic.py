from Modules.riddle import Riddle
from Modules.item import Item

# Array to store collected items
#collected_items = []

# Helper function to talk to Jeremy
def talk_to_jeremy(room, game_state):
    """Handles interaction with Jeremy and solving riddles."""
    print("\nYou: Hey Jeremy! I'm not sure I got the right groceries list. It looks like it's written in… riddle?")
    print("Jeremy: Oh yes! Sorry for the inconvenience, it was supposed to make one of our bakers' day, but it turned out a bit unfortunate now.")
    print("Jeremy: Here are some riddles to solve.\n")
    
    riddles = Riddle.get_riddle_by_room(room.id)
    if isinstance(riddles, dict):  # If a single riddle is returned as a dictionary
        riddles = [riddles]
    elif not isinstance(riddles, list):  # If it's neither a list nor a dict
        print("Error: Riddles data is not in the expected format.")
        return
    
    if riddles:
        print("Jeremy hands you a list of riddles to solve.")
        solve_riddles(riddles, game_state)
    else:
        print("No riddles found for this room.\n")

# Helper function to solve riddles
def solve_riddles(riddles, game_state):
    """Solve riddles sequentially."""
    global collected_items

    for riddle in riddles:
        while True:
            print(f"\nRiddle: {riddle['riddle']}\n")
            answer = input("Your answer: ").strip().lower()
            if answer in riddle["answers"]:
                print("\n" + riddle["success_dialogues"][0] if riddle["success_dialogues"] else "Correct!" + "\n")
                game_state.collected_items.append(riddle["answers"][0])  # Add solved riddle items to collected
                break
            else:
                print("\n" + riddle["failure_dialogues"][0] if riddle["failure_dialogues"] else "That's not correct. Try again." + "\n")
    
    # Once all riddles are solved
    print("\nCongratulations! You have successfully solved all the riddles and got all the ingredients for the bakery!")
    print("\nBuzz! There's a reminder on your phone.\n")

# Helper function to take items
def take_item(item_name, room, items, game_state):
    """Handles taking an item in the bakery."""
    available_items = Item.get_items_in_room(room.id, items)
    item_names = {item.name.lower() for item in available_items}

    if item_name.lower() in item_names:
        if item_name.lower() not in game_state.collected_items:
            game_state.collected_items.append(item_name.lower())
            print(f"\n{item_name.capitalize()} is now in your bag!\n")
        else:
            print(f"\nYou already have {item_name}.\n")
    else:
        print("\nItem not found in this room.\n")

# Helper function to inspect the phone
def inspect_phone():
    """Display the current phone reminder."""
    print("\nYou inspect your phone. There's a new reminder: get a fresh bouquet of flowers for your tea date with the Smiths.\n")

# Process commands for bakery room
def process_bakery_command(command, room, items, game_state):
    """Processes commands specific to the bakery room."""
    words = command.lower().split()
    action = words[0]
    item_name = ' '.join(words[1:]) if len(words) > 1 else None

    if action == "talk" and item_name == "to jeremy":
        talk_to_jeremy(room, game_state)
    elif action == "inspect" and item_name == "phone":
        inspect_phone()
    elif action == "take" and item_name:
        take_item(item_name, room, items, game_state)
    else:
        print("\nI don't understand that command.\n")
