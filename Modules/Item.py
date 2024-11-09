# Modules/item.py
import json
from pathlib import Path

class Item:
    def __init__(self, name, description, location):
        self.name = name
        self.description = description
        self.location = location

    def __str__(self):
        return self.name.capitalize()

    def take(self):
        return f"{self.name.capitalize()} is now in your {self.get_location()}!"

    def get_location(self):
        # Decide the default location for specific items
        return "pocket" if self.name in ["keys", "phone"] else "bag"
    
    def inspect(self):
        return self.description

    @staticmethod
    def load_items(filename):
        # Get the path to the Assets folder and load items.json file
        file_path = Path(__file__).parent.parent / 'Assets' / filename
        with open(file_path, 'r') as file:
            data = json.load(file)

        items = {}
        for item_data in data["items"]:
            item = Item(item_data["name"], item_data["description"], item_data["location"])
            items[item_data["name"].lower()] = item  # Store the item instance by name
        return items
