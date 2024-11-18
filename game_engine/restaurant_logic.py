from Modules.room import Room
from Modules.item import Item

collected_items = []
task_status = False
def start_restaurant(room):
    """Prints the description of the restaurant."""
    # if first time in room => long description
    # if second time => short description
    if room.first_time_in_room:
        room.print_long_description()
        room.change_first_time_status()
    else:
        room.print_short_description()

def talk_to_dina():
    """Dialog with Dina"""
    # should have a global variable to track progress
    # for now, task_status
    if (task_status == False):
        print("I have a culinary crisis! I’ve lost my Nana’s famous lavender pie recipe. It’s been a staple here for years, but I can't seem to locate the original version anywhere! Nana might remember, but I can‘t leave the diner unattended to ask her.\n")
        print("\033[1mWould you help Dina?\033[0m")
        # if already helped dina, switch conversation
    else:
        print("Hi! Today's special is a family recipe: Lavender Pie. Would you like to try?")

def help_dina():
    """Dina's hints for the task"""
    print("Really? You’d do that? You can find her at the retirement home, but I’ve tried talking to her a few times. It’s hard for her to focus these days. They say smell can jog a person’s memory though… Let me know what she says!")

def give_recipe():
    """Give Dina the recipe from Sophia"""
    global task_status
    if "Sophia's Lavender Pie Recipe" in collected_items:
        collected_items.remove("Sophia's Lavender Pie Recipe")
        task_status = True
        print("Wow, I can’t believe you did it! I was worried that the recipe was lost forever.")
    else:
        print("You don't have the recipe to give.")

def restaurant_command(command):
    words = command.lower().split()
    action = words[0]
    item_name = ' '.join(words[1:]) if len(words) > 1 else None

    if action == "talk" and item_name == "dina":
        talk_to_dina()
    elif action == "help" and item_name == "dina":
        help_dina()
    elif action == "give" and item_name == "recipe":
        give_recipe()

    # function for testing
    # elif action == "take" and item_name == "recipe":
    #     take_recipe()
    # function for testing

    else:
        print("I don't understand that command.")

# test
# def take_recipe():
#     items = Item.load_items('items.json')
#     collected_items.append(items["sophia's lavender pie recipe"].name)
#     print("You've added 'Sophia's lavender pie recipe' to your bag.")
#
# def game_loop():
#     """Check if everything is working in the room"""
#     rooms = Room.load_rooms('rooms.json')
#     dina_diner = rooms[4]
#     start_restaurant(dina_diner)
#
#     while True:
#         # Start the restaurant area
#         # Get user input
#         command = input("\nEnter a command: ")
#         if command == "start":
#             start_restaurant(dina_diner)
#         if command.lower() == "q":
#             print("Thanks for playing!")
#             break
#
#         restaurant_command(command)
#
#
# # Run the game
# if __name__ == "__main__":
#     game_loop()