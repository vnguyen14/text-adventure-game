from Modules.item import Item
from Modules.riddle import Riddle

collected_items = []
solved_riddles = 0
required_riddles = 4  # Number of riddles to solve

riddle_data = {}


# Start the bakery room
def start_bakery(room, items):
    """Initializes the bakery room and shows available items."""
    global riddle_data

    # Print the room's long description
    room.print_long_description()
    
    # Load available items and riddles for this room
    available_items = Item.get_items_in_room(room.id, items)
    riddle_data = Riddle.get_riddle_by_room(room.id)

    # Display items in the room and prompt the player to talk to Jeremy
    print(f"Items in this room: {[item.name for item in available_items]}")
    print("Talk to Jeremy to learn more about the task.")


# Function to solve a riddle
def solve_riddle(answer):
    """Verifies if the player's answer solves the current riddle."""
    global solved_riddles

    # Match the player's answer with the correct answer for the current riddle
    if answer.lower() in [ans.lower() for ans in riddle_data["answers"]]:
        solved_riddles += 1
        print("Correct! Keep going!")

        if solved_riddles == required_riddles:
            # Reward the player upon solving all riddles
            print("Congratulations! You’ve solved all the riddles and collected the ingredients!")
            print("Buzz! There’s a reminder on your phone: 'Get a fresh bouquet of flowers for your tea date with the Smiths.'")
            collected_items.extend(riddle_data["rewards"])
            print("Collected items: Butter, Yeast, Chocolate Chips, Sugar.")
        else:
            # Inform the player about remaining riddles
            print(f"You still have {required_riddles - solved_riddles} riddles to solve.")
    else:
        print("Sorry, that’s not the correct answer. Try again!")


# Helper function to talk to Jeremy
def talk_to_jeremy():
    """Handles dialogue with Jeremy."""
    if solved_riddles < required_riddles:
        print("Hey there! Thanks for stopping by. I need your help solving some riddles to get the ingredients for a big order!")
        print("Would you like to help Jeremy?")


# Helper function to help Jeremy
def help_jeremy():
    """Jeremy provides the next riddle."""
    if solved_riddles < required_riddles:
        print("Thank you so much! Here’s the next riddle:")
        print(riddle_data["riddles"][solved_riddles])
    else:
        print("You’ve already helped me solve all the riddles. Thank you!")


# Process player commands
def process_bakery_command(command, room, items):
    """Handles player commands in the bakery."""
    words = command.lower().split()
    action = words[0]
    input_data = ' '.join(words[1:]) if len(words) > 1 else None

    if action == "talk" and input_data == "jeremy":
        talk_to_jeremy()
    elif action == "help" and input_data == "jeremy":
        help_jeremy()
    elif action == "answer":
        if input_data:
            solve_riddle(input_data)
        else:
            print("You need to provide an answer after 'answer'.")
    else:
        print("I don't understand that command.")