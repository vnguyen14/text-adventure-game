from Modules.room import Room
from Modules.item import Item

# collected_items = []
items = Item.load_items('items.json')

task_status = False

def talk_to_sophia():
    """Dialog with Dina"""
    # should have a global variable to track progress
    # for now, task_status
    if (task_status == False):
        print("Oh, dear, I'm sorry, sweetheart. My memory isn't what it used to be. I can't quite recall the recipe anymore–just the way it made everyone smile. But I know it had lavender in it, and love, of course.")

    else:
        print("Hello dear! You have a wonderful day!")

def give_lavender(game_state):
    """Give Sophia the lavender"""
    global task_status
    if items[9] in game_state.collected_items and items[5] not in game_state.collected_items:
        game_state.collected_items.remove(items[9])
        task_status = True
        print("Oh! Lavender! I can almost taste it! I used to steep it in the cream... and there was something about the honey... yes! It's all coming back now! Let me quickly jot it down for you.")   
    else:
        print("You don't have the lavender to give.")


def take_recipe(game_state):
    if items[5] not in game_state.collected_items and task_status == True:
        game_state.collected_items.append(items[5])
        print("You've added 'Sophia's lavender pie recipe' to your bag.") 
    else:
        print("You don't have access to the recipe.")

def process_retirementHome_command(command, game_state):
    words = command.lower().split()
    action = words[0]
    item_name = ' '.join(words[1:]) if len(words) > 1 else None

    if action == "talk to" and item_name == "sophia":
        talk_to_sophia()
    elif action == "give" and item_name == "lavender":
        give_lavender(game_state)
    elif action == "take" and item_name == "recipe":
        take_recipe(game_state)
    else:
        print("I don't understand that command.")

# def game_loop():
#     """Check if everything is working in the room"""
#     rooms = Room.load_rooms('rooms.json')
#     retirementHome = rooms[8]
#     start_restaurant(retirementHome)
#     collected_items.append(items[9])

#     while True:
#         # Start the restaurant area
#         # Get user input
#         command = input("\nEnter a command: ")
#         if command == "start":
#             start_restaurant(retirementHome)
#         elif command.lower() == "q":
#             print("Thanks for playing!")
#             break
#         else:
#             process_retirementHome_command(command)


# # Run the game
# if __name__ == "__main__":
#     game_loop()