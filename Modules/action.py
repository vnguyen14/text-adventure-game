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
        manual += "    - w: Move West\n"
        manual += "    - s: Move South\n\n"
        
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
