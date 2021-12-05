# Author: Mike Eggar
# Date: 12/5/21

from game_db import scene_db, items_db
from minigames import PizzaShopServer
from models import Item, Scene


class GameState:
    """
    The state of the game.
    """

    def __init__(self, scene_db):
        self.current_scene_id = scene_db["initial_scene_id"]
        self.game_over = False
        self.loot = { "scuba": Item("scuba", items_db) }

    def addItemByName(self, item_name):
        self.loot[item_name] = Item(item_name, items_db)

    def removeItemByName(self, item_name):
        self.loot.pop(item_name)

    def printAllItems(self):
        print("\nYour items\n==========")
        for k,v in self.loot.items():
            print(k)



class GameFunctions:
    """
    Commands that are available during the whole game. Can be overridden
    in a Scene by using the same cmd name in SceneFunctions.
    """

    # list of valid function names
    options = set(["show", "drop", "exit", "help"])

    def processCommand(gamestate, cmd, param):
        success = True

        if cmd == "show":
            if param:
                if param in gamestate.loot: 
                    gamestate.loot[param].printInfo()
                else:
                    print("You don't have an item by that name")
            else:
                gamestate. printAllItems()

        elif cmd == "drop":
            gamestate.removeItemByName(param)

        elif cmd == "help":
            print("\n".join([
               "\nYou can use the following commands:",
               "-----------------------------------",
               "Look:\t\t check out your surroundings when you get to a new place. there may be items to Get.",
               "Show:\t\t list all your items.",
               "Show myItem:\t get information on myItem.",
               "Go Coral Reef:\t you can use Go to go to another place on the map. You can only follow the path on the map.",
               "Get map:\t use Get to get an item if you see one, like this map.",
               "Drop map:\t to get rid of an item, like this map.",
               "Use item:\t Use can be used to use an item.",
               "Help:\t\t To see this menu at any time.",
               "Exit:\t\t And you can exit the game at any time."
             ]))
                   

        elif cmd == "exit":
            exit()
            

class SceneFunctions:
    """
    Commands that are available during a Scene, as described in db.
    """

    def processCommand(gamestate, cmd_dict):
        for k,v in cmd_dict.items():

            if k == "item_exists":
                return v in gamestate.loot

            elif k == "add_item":
                gamestate.addItemByName(v)

            elif k == "game_over":
                gamestate.game_over = True

            elif k == "change_scene":
                if v in scene_db:
                    gamestate.current_scene_id = v
                else:
                    print("Invalid scene id")

            elif k == "minigame":
                if v == "PizzaShopServer":
                    server = PizzaShopServer()
                    server.start_session()



# ============================The Game Loop ============================ #

gamestate = GameState(scene_db)

while not gamestate.game_over:

    # load a new scene
    scene = Scene(gamestate.current_scene_id, scene_db)
    current_scene_id = scene.scene_id
    gamestate.current_scene_id = current_scene_id

    print(scene.info)

    # run the Scene loop
    while gamestate.current_scene_id == current_scene_id and not gamestate.game_over:

        user_input = input(scene.prompt).strip().split()
        cmd = user_input[0]
        cmd = cmd.lower()
        param = ' '.join(user_input[1:])

        # first see if the user input can be handled by a SceneFunction
        if cmd in scene.options:

            if param and param not in scene.options[cmd]:
                print(scene.unknown_option_response)

            else:
                option = scene.options[cmd] if not param else scene.options[cmd][param]

                validated = True

                if "validate" in option:
                    validated = all(SceneFunctions.processCommand(gamestate, test) for test in option["validate"]["tests"])
                    if not validated:
                        print(option["validate"]["fail_response"])

                if validated and "gamestate" in option:
                    for item in option["gamestate"]:
                        SceneFunctions.processCommand(gamestate, option["gamestate"])
                        
                if validated and "response" in option:
                    print(option["response"])


        # if no SceneFunction can handle the user input, see if a GameFunction can
        elif cmd in GameFunctions.options:
            GameFunctions.processCommand(gamestate, cmd, param)

        # if not, print error and continue taking user input
        else:
            print(scene.unknown_option_response)

