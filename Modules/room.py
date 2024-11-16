from pathlib import Path
import json

class Room:
    def __init__(self, id, name, longDescription, shortDescription, connections):
        self.id = id
        self.name = name
        self.longDescription = longDescription
        self.shortDescription = shortDescription
        self.connections = connections
        self.first_time_in_room = True  # Track if this is the first time the player enters the room

    # Method to get all rooms from rooms.json
    @staticmethod
    def load_rooms(filename):
        # Use the absolute path to Assets folder
        file_path = Path(__file__).parent.parent / 'Assets' / filename
        with open(file_path, 'r') as file:
            data = json.load(file)
        rooms = {}
        for room_data in data["rooms"]:
            room = Room(
                room_data["id"],
                room_data["name"],
                room_data["longDescription"],
                room_data["shortDescription"],
                room_data["connections"]
            )
            rooms[room.id] = room
        return rooms

    # Method to print long description
    def print_long_description(self):
        print(self.longDescription)

    # Method to print short description
    def print_short_description(self):
        print(self.shortDescription)

    def change_first_time_status(self):
        self.first_time_in_room = False

