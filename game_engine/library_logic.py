'''''
TEMPORARY TO MAKE STANDALONE LIBRARY GAME
'''''
#from Modules.item import Item
#from Modules.room import Room

# Define the Room class
class Room:
    def __init__(self, room_id, long_description, short_description):
        self.id = room_id
        self.long_description = long_description
        self.short_description = short_description
        self.visited = False

    # Method to print the room description
    def print_description(self):
        if not self.visited:
            print(self.long_description)
            self.visited = True
        else:
            print(self.short_description)

# Define the Item class
class Item:
    def __init__(self, name, location):
        self.name = name
        self.location = location

# Array to store all collected items from take action
collected_items = []

# Library room setup
library_room = Room(
    room_id=1,
    long_description=(
        "You are in Lore Library. Towering shelves stretch from front to back, "
        "brimming with centuries of knowledge and boundless imagination. The inviting "
        "atmosphere encourages you to explore the countless stories waiting to be discovered. "
        "The quiet ambiance enhances the serenity of the space, making it a perfect haven for "
        "readers and dreamers alike. Near the front door, Mrs. Henderson, the librarian, expertly "
        "assists those seeking a specific title."
    ),
    short_description="You're in Lore Library. Mrs. Henderson, the librarian, skillfully helps visitors find the titles they're looking for."
)

# Items in the library - added random items so that it's not obvious what user should take
library_items = {
    "camera battery": Item(name="Camera Battery", location=[1]),
    "what in carnations? a guide to flowers": Item(name="What in Carnations? A Guide to Flowers", location=[1]),
    "old bookmark": Item(name="Old Bookmark", location=[1]),
    "ink pen": Item(name="Ink Pen", location=[1]),
}

'''''
END TEMPORARY TO MAKE STANDALONE LIBRARY GAME
'''''

#Helper function to get all items in this room
def get_items_in_room(room_id, items):
    return [item for item in items.values() if room_id in item.location] # Only get items with home's roomID

# Helper function to talk to Mrs. Henderson
def talk_to_mrs_henderson():
    print("Let me know if you need any help finding anything—books, supplies, equipment—anything!")

def find_items(keyword=None):
    search_results = [
        item.name for item in library_items.values()
        if keyword.lower() in item.name.lower() or not keyword
    ]
    if search_results:
        print(f"Let me see what I can find! Here you go: {', '.join(search_results)}")
    else:
        print("Sorry dear, I couldn't find anything matching that word.")

# Helper function to process 'take item' action
def take_item(item_name, room_id, items):
    available_items = get_items_in_room(room_id, items)
    item_names = {item.name.lower(): item for item in available_items}  # Map item names to item objects

    if item_name.lower() in item_names:
        collected_items.append(item_name.lower())
        item = item_names[item_name.lower()]
        
        # Special interactions for specific items
        if item_name.lower() == "camera battery":
            if "camera" in collected_items:
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
def process_library_command(command, room, items):
    words = command.lower().split()
    action = words[0]
    item_name_or_keyword = ' '.join(words[1:]) if len(words) > 1 else None

    if action == "talk" and item_name_or_keyword == "mrs. henderson":
        talk_to_mrs_henderson()
    elif action == "find":
        find_items(item_name_or_keyword or "")
    elif action == "take" and item_name_or_keyword:
        take_item(item_name_or_keyword, room.id, items)
    else:
        print("I don't understand that command.")

# Start the room
def start_library_room(room, items):
    room.print_description()
    while True:
        command = input("\n> ").strip()
        if command.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break
        process_library_command(command, room, items)

start_library_room(library_room, library_items)