import json
from pathlib import Path

class Action:
    def __init__(self, id, name, description, item_id, character_id):
        self.id = id
        self.name = name
        self.description = description
        self.item_id = item_id
        self.character_id = character_id

    @staticmethod
    def load_actions(filename):
        # Get the path to the Assets folder and load actions.json file
        file_path = Path(__file__).parent.parent / 'Assets' / filename
        with open(file_path, 'r') as file:
            data = json.load(file)

        actions = {}
        for action_data in data["actions"]:
            action = Action(
                action_data["id"],
                action_data["name"],
                action_data["description"],
                action_data["item_id"],
                action_data["character_id"]
            )
            actions[action.name] = action  # Store the action instance by name
        return actions

    @staticmethod
    def print_game_manual(actions):
        # Start the manual string
        manual = "=" * 50 + "\n"
        manual += "==================== GAME MANUAL ====================\n\n"
        
        # Movement commands section
        manual += "| MOVEMENT COMMANDS: Navigate between rooms\n"
        manual += "-" * 54 + "\n"
        manual += "    - n: Move North\n"
        manual += "    - e: Move East\n"
        manual += "    - s: Move South\n"
        manual += "    - w: Move West\n\n"
        
        # Action commands section
        manual += "| ACTION COMMANDS: Interact with the game world\n"
        manual += "-" * 54 + "\n"
        for action in actions.values():
            manual += f"    - {action.name}: {action.description}\n"
        
        # Game objectives section
        manual += "\n| GAME OBJECTIVES: Progress and goals\n"
        manual += "-" * 54 + "\n"
        manual += "    - Explore rooms: Discover hidden secrets\n"
        manual += "    - Solve puzzles: Progress through the story\n"
        manual += "    - Assist characters: Complete quests\n\n"

        # Notes section
        manual += "NOTE:\n"
        manual += "-" * 54 + "\n"
        manual += "Commands are not case-sensitive but must be spelled correctly.\n"
        manual += "For arrangements, use flower symbols in uppercase.\n\n"
        
        # Closing statement
        manual += "Enjoy your adventure!\n"
        manual += "=" * 50
        
        return manual
    
    @staticmethod
    def take_item(item_name, available_items, game_state):
        item_names = {item.name.lower(): item for item in available_items}  # Map item names to item objects
        if item_name.lower() in item_names:
            if item_name.lower() in game_state.collected_items:
                print(f"'{item_name}' is in your bag!")
            else:
                game_state.collected_items.append(item_name.lower())
                item = item_names[item_name.lower()]
                
                # Special interactions for specific items
                if item_name.lower() == "camera battery":
                    if "camera" in game_state.collected_items:
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
