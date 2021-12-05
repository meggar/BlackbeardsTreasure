"""
Data models for object database layer. 
"""

class Item:
    """
    Examples: Scuba, Gold key, Treasure map
    """
    def __init__(self, item_name, items_db):
        self.item_name = item_name
        self.item_description = items_db[item_name]
    def printInfo(self):
        print("\n", self.item_name)
        print(self.item_description["header"], self.item_description["info"], "\n")

class Scene:
    """
    Example: Parrot Lagoon
    """
    def __init__(self, scene_id, scene_db):
        scene_data = scene_db[scene_id]
        self.scene_id = scene_id
        self.info = scene_data["info"]
        self.prompt = scene_data["prompt"]
        self.unknown_option_response = scene_data["unknown_option_response"]
        self.options = scene_data["options"]
