from Modules.riddle import Riddle
from Modules.action import Action
from Modules.item import Item

# Store solved riddles
solved_riddles = []

# Start the room
def start_bakery(room, items, actions):
    """Initializes the bakery room, prints the description, and displays riddles."""
    global solved_riddles

    # Display the bakery's long description
    room.print_long_description()

    # Load and display riddles associated with the bakery
    riddles = Riddle.get_riddle_by_room(room.id)
    print("Jeremy hands you a list of riddles to solve to collect ingredients:")
    for riddle in riddles:
        print(f"- {riddle['riddle']}")

    # Display available actions
    available_actions = Action.get_actions_for_room(room.id, actions)
    print(f"Available actions: {[action.name for action in available_actions]}")

# Solve a riddle
def solve_riddle(answer, room):
    """Checks if the player's answer solves a riddle."""
    global solved_riddles

    # Load riddles dynamically
    riddles = Riddle.get_riddle_by_room(room.id)
    riddle = next((r for r in riddles if r['answer'].lower() == answer.lower()), None)

    if riddle:
        if riddle['answer'] in solved_riddles:
            print("You've already solved this riddle!")
        else:
            print(f"Correct! You solved the riddle: {riddle['riddle']}")
            solved_riddles.append(riddle['answer'])
            if len(solved_riddles) == len(riddles):
                print("Congratulations! You've solved all the riddles in the bakery!")
                print("Buzz! There’s a reminder on your phone: Get a fresh bouquet of flowers for your tea date with the Smiths.")
    else:
        print("That's not correct. Try again.")

# Process user commands
def process_bakery_command(command, room, items, actions):
    """Processes commands specific to the bakery room."""
    words = command.lower().split()
    action_name = words[0]
    user_input = ' '.join(words[1:]) if len(words) > 1 else None

    # Fetch the action object
    action = Action.get_action_by_name(action_name, actions)

    if action:
        if action.name == "talk" and user_input == "jeremy":
            print("Hey Jeremy! I’m not sure I got the right groceries list. It looks like it’s written in… riddle?")
            print("Oh yes! Sorry for the inconvenience. Could you try solving it? Let me know if you need any help!")
        elif action.name == "inspect" and user_input == "riddles":
            riddles = Riddle.get_riddle_by_room(room.id)
            for riddle in riddles:
                print(f"Riddle: {riddle['riddle']}")
        elif action.name == "solve" and user_input:
            solve_riddle(user_input, room)
        else:
            print(f"The action '{action_name}' cannot be performed here.")
    else:
        print("I don't understand that command.")
