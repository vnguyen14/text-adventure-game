from Modules.item import Item
from Modules.riddle import Riddle

collected_items = []
solved_riddles = 0
required_riddles = 4  # Number of riddles to solve

riddle_data = {}

# Start the bakery room
def start_bakery(room, items):
    """Prints the long description of the bakery and shows available items."""
    global riddle_data

    room.print_long_description()
    available_items = Item.get_items_in_room(room.id, items)
    riddle_data = Riddle.get_riddle_by_room(room.id)
    print(f"Items in this room: {[item.name for item in available_items]}")
    print("\033[1mTalk to Jeremy to learn more about the task.\033[0m")


# Function to solve a riddle
def solve_riddle(answer):
    """Checks if the player's answer solves the current riddle."""
    global solved_riddles

    if answer.lower() in [ans.lower() for ans in riddle_data["answers"]]:
        solved_riddles += 1
        print("\033[1mCorrect! Keep going!\033[0m")
        if solved_riddles == required_riddles:
            print("Congratulations! You’ve solved all the riddles and collected the ingredients!")
            print("Buzz! There’s a reminder on your phone: \033[1m'Get a fresh bouquet of flowers for your tea date with the Smiths.'\033[0m")
            collected_items.extend(riddle_data["rewards"])
            print("\033[1mCollected items: Butter, Yeast, Chocolate Chips, Sugar.\033[0m")
        else:
            print(f"\033[1mYou still have {required_riddles - solved_riddles} riddles to solve.\033[0m")
    else:
        print("\033[1mSorry, that’s not the correct answer. Try again!\033[0m")


# Helper function to talk to Jeremy
def talk_to_jeremy():
    """Handles dialogue with Jeremy."""
    if solved_riddles < required_riddles:
        print("Hey there! Thanks for stopping by. I need your help solving some riddles to get the ingredients for a big order!")
        print("\033[1mWould you like to help Jeremy?\033[0m")


# Helper function to help Jeremy
def help_jeremy():
    """Jeremy shares his riddle challenge."""
    if solved_riddles < required_riddles:
        print("Thank you so much! Here’s the first riddle:")
        print(f"\033[1m{riddle_data['riddles'][solved_riddles]}\033[0m")
    else:
        print("You’ve already helped me solve all the riddles. Thank you!")


# Function to process user's commands from the prompt/terminal
def process_bakery_command(command, room, items):
    """Processes commands specific to the bakery room."""
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