from pathlib import Path
import json

class Riddle:
    @staticmethod
    def load_riddles(file_path=Path("Assets/riddles.json")):
        """Load riddles from a JSON file."""
        if file_path.exists():
            with file_path.open("r") as f:
                data = json.load(f)
            return data.get("riddles", [])
        else:
            print("Riddle file not found.")
            return []

    @classmethod
    def get_riddle_by_room(cls, room_id, file_path=Path("Assets/riddles.json")):
        """Retrieve riddle associated with a specific room ID."""
        riddles = cls.load_riddles(file_path)
        return next((r for r in riddles if r["room_id"] == room_id), None)
