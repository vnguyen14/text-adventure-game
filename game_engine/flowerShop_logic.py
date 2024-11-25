from Modules.item import Item
from Modules.riddle import Riddle
from itertools import combinations

collected_items = []
# Track the number of arrangements completed
arrangement_count = 0

# Correct flower arrangements
valid_arrangements = []

riddle_data = {}


# Start the room
def start_flower_shop(room, items):
    """Prints the long description of the flower shop, get riddle data and shows available items."""
    global valid_arrangements
    global riddle_data

    room.print_long_description()
    available_items = Item.get_items_in_room(room.id, items)
    riddle_data = Riddle.get_riddle_by_room(room.id)
    valid_arrangements = generate_valid_arrangements(room, available_items)
    print(f"Items in this room: {[item.name for item in available_items]}")


# Helper function to generate valid flowers combinations
def generate_valid_arrangements(room, items):
    valid_arrangements = []
    # Get flowers object from items.json
    flowers = next((item.content for item in items if item.id == 4), None)
    
    # Generate all unique combinations of three different flowers
    for combo in combinations(flowers.keys(), 3):
        f1, f2, f3 = flowers[combo[0]], flowers[combo[1]], flowers[combo[2]]
        
        # Apply Florence's bouquet rules
        if (f1['color'] == "Red" and f2['color'] in ["Yellow", "Purple", "White"] and f3['color'] in ["Yellow", "Purple", "White"]) or \
           (f1['color'] == "Yellow" and f2['color'] in ["Red", "White"] and f3['color'] in ["Red", "White"]) or \
           (f1['color'] == "Purple" and f2['color'] in ["Red", "Blue", "White"] and f3['color'] in ["Red", "Blue", "White"]) or \
           (f1['color'] == "White" and f2['color'] != "White" and f3['color'] != "White"):
            # Check the size rule (at least two different sizes)
            if len(set([f1['size'], f2['size'], f3['size']])) >= 2:
                # Check the scented flower rule (no more than one strongly scented flower)
                if len([f for f in [f1, f2, f3] if f['scent'] == "Strong"]) <= 1:
                    arrangement = ''.join(combo)
                    valid_arrangements.append(arrangement)
    
    return valid_arrangements


# Function for solving puzzle logic
def solve_arrangement(arrangement):
    print(valid_arrangements)
    """Checks if the player's arrangement matches Florence's criteria."""
    global arrangement_count

    # Check if the entered arrangement is correct
    if arrangement in valid_arrangements:
        arrangement_count += 1
        if arrangement_count < len(valid_arrangements):
            print(f"Nice! I need {len(valid_arrangements) - arrangement_count} more!")
            valid_arrangements.remove(arrangement)
        else:
            print("Perfect! We might just pull this off for the festival!")
            print("Thanks for all your help. Let me treat you to lunch. I have to finish these bouquets but head over to Dina's Diner. I’ll let Dina know the bill is on me!")
            print("Oh and of course, here are some of today’s most blooming flowers. I hope they make your day!")
            collected_items.extend(["roses", "lavender", "hydrangeas"])
            print("\033[1mRoses, Lavender, and Hydrangeas are in your bag!\033[0m")
    else:
        print("Sorry, that doesn’t work!")


# Helper function to talk to Florence
def talk_to_florence():
    """Handles dialog with Florence."""
    if "lavender" not in collected_items:
        print("A big festival is coming and I want everything to be perfect, but I can’t assemble all these elaborate bouquets!\n")
        print("\033[1mWould you help Florence?\033[0m")


# Helper function to help Florence
def help_florence():
    """Florence shares her bouquet requirements."""
    print("Thank you so much! Let me share some instructions with you.")
    
    # Handle riddle_data as a list
    if isinstance(riddle_data, list) and riddle_data:
        # Assuming Florence's bouquet riddle is the first in the list
        relevant_riddle = riddle_data[0]  # Use the first riddle
        print(f"\033[1m{relevant_riddle['riddle']}\033[0m")  # Print the riddle text
    else:
        print("No riddle data found for this room.")
    
    print("I keep a book of all the flowers we have in store, it's called 'What in Carnations? A guide to flowers', please feel free to take a look at it. Let me know if you found any good arrangement by saying the flowers' symbols, I'll let you know right away if the arrangement works!")



# Helper function to display information from the flower guide book 
def inspect_book(items):
    """Displays information from the flower guide book in a table format."""

    book_name = "What in Carnations? A Guide to Flowers"
    # Use case-insensitive search for the item name in the items dictionary
    book = next((item for item in items.values() if book_name.lower() in item.name.lower()), None)

    if book:
        print(book.description)  # Print the book's description
    else:
        print("The book is not available in this room.")


# Function to precess user's commands from the promt/terminal
def process_flower_shop_command(command, room, items):
    """Processes commands specific to the flower shop room."""
    words = command.lower().split()
    action = words[0]
    item_name = ' '.join(words[1:]) if len(words) > 1 else None

    if action == "talk" and item_name == "florence":
        talk_to_florence()
    elif action == "help" and item_name == "florence":
        help_florence()
    elif action == "inspect" and item_name == "what in carnations? a guide to flowers book":
        inspect_book(items)
    elif action == "arrange":
        # Only use the input after "arrange" as the arrangement string
        arrangement = ''.join(words[1:]).upper()
        solve_arrangement(arrangement)
    else:
        print("I don't understand that command.")