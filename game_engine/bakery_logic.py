# game_engine/bakery_logic.py
from Modules.riddle import Riddle
from Modules.item import Item

# Start the bakery room
def start_bakery(room, items):
    """Handles the setup for entering the bakery."""
    room.print_long_description()  # Print long description the first time
    available_items = Item.get_items_in_room(room.id, items)
    print(f"Items in this room: {[item.name for item in available_items]}")


# Helper function to talk to Jeremy
def talk_to_jeremy(room, game_state):
    """Handles interaction with Jeremy and solving riddles."""
    print("You: Hey Jeremy! I’m not sure I got the right groceries list. It looks like it’s written in… riddle?")
    print("Jeremy: Oh yes! Sorry for the inconvenience, it was supposed to make one of our bakers’ day, but it turned out a bit unfortunate now.")
    print("Jeremy: Here are some riddles to solve.")
    
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
        print("No riddles found for this room.")


# Helper function to solve riddles
def solve_riddles(riddles, game_state):
    """Solve riddles sequentially."""
    for riddle in riddles:
        while True:
            print(f"Riddle: {riddle['riddle']}")
            answer = input("Your answer: ").strip().lower()
            if answer in riddle["answers"]:
                print(riddle["success_dialogues"][0] if riddle["success_dialogues"] else "Correct!")
                game_state.collected_items.append(riddle["answers"][0])  # Add solved riddle items to collected
                break
            else:
                print(riddle["failure_dialogues"][0] if riddle["failure_dialogues"] else "That's not correct. Try again.")

    # Once all riddles are solved
    print("Congratulations! You have successfully solved all the riddles and got all the ingredients for the bakery!")
    game_state.phone_message = "get a fresh bouquet of flowers for your tea date with the Smiths."
    print("Buzz! There’s a reminder on your phone.")


# Helper function to inspect the phone
def inspect_phone(game_state):
    """Display the current phone reminder."""
    if game_state.phone_message:
        print(f"You inspect your phone. There's a new reminder: {game_state.phone_message}")
    else:
        print("Your phone has no new messages.")


# Process commands for bakery room
def process_bakery_command(command, room, items, game_state):
    """Processes commands specific to the bakery room."""
    words = command.lower().split()
    action = words[0]
    item_name = ' '.join(words[1:]) if len(words) > 1 else None

    if action == "talk" and item_name == "to jeremy":
        talk_to_jeremy(room, game_state)
    elif action == "inspect" and item_name == "phone":
        inspect_phone(game_state)
    else:
        print("I don't understand that command.")