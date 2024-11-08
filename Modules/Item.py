class Item:
    def __init__(self, item_id, item_name, item_description):
        self.item_id = item_id
        self.item_name = item_name
        self.item_description = item_description

    def check_item(self, item_id):
        return self.item_id == item_id

    def get_item_details(self):
        return {
            'id': self.item_id,
            'name': self.item_name,
            'description': self.item_description
        }