# Modules/item.py
import json
from pathlib import Path

class Item:
    def __init__(self, id, name, description, location, content):
        self.id = id
        self.name = name
        self.description = description
        self.location = location
        self.content = content
        

    def __str__(self):
        return self.name.capitalize()

    # Method to get all items from items.json
    @staticmethod
    def load_items(filename):
        # Get the path to the Assets folder and load items.json file
        file_path = Path(__file__).parent.parent / 'Assets' / filename
        with open(file_path, 'r') as file:
            data = json.load(file)

        items = {}
        for item_data in data["items"]:
            item = Item(item_data["id"], item_data["name"], item_data["description"], item_data["location"], item_data["content"])
            items[item_data["name"].lower()] = item  # Store the item instance by name
        return items
