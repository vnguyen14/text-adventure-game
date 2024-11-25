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
        """Retrieve all riddles associated with a specific room ID."""
        riddles = cls.load_riddles(file_path)
        return [r for r in riddles if r["room_id"] == room_id]

    @classmethod
    def solve_riddles_sequentially(cls, room_id, file_path=Path("Assets/riddles.json")):
        """Solve riddles in a sequential loop, ensuring no premature exit."""
        riddles = cls.get_riddle_by_room(room_id, file_path)
        if not riddles:
            print("No riddles found for this room.")
            return False

        riddles = sorted(riddles, key=lambda r: r["id"])  # Sort by ID for sequential order
        solved_riddle_ids = set()

        while len(solved_riddle_ids) < len(riddles):  # Loop until all riddles are solved
            for riddle in riddles:
                if riddle["id"] not in solved_riddle_ids:  # Only process unsolved riddles
                    print(f"Riddle: {riddle['riddle']}")
                    answer = input("Your answer: ").strip().lower()
                    if answer in riddle["answers"]:
                        solved_riddle_ids.add(riddle["id"])
                        print(riddle["success_dialogues"][0] if riddle["success_dialogues"] else "Correct!")
                    else:
                        print(riddle["failure_dialogues"][0] if riddle["failure_dialogues"] else "That's not correct. Try again.")
                    break  # Re-check the loop condition after every attempt

        # Once all riddles are solved
        print("Congratulations! You have successfully solved all the riddles and got all the ingredients for the bakery!")
        return True
