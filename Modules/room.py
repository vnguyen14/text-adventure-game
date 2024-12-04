from pathlib import Path
import json
from Modules.item import Item

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

    # Method to print description
    def print_description(self):
        if self.first_time_in_room:
            print("\n" + self.longDescription + "\n")
            self.first_time_in_room = False
        else:
            print("\n" + self.shortDescription + "\n")

    # Generic handler for starting any room.
    def start_room(self, items=None):
        self.print_description()  # Print long description
        
        # If items passed, then want to show items in room. Otherwise, hide items in room.
        if items:
            available_items = Item.get_items_in_room(self.id, items)
            print(f"Items in this room: {[item.name for item in available_items]}\n")

