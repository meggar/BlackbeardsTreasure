items_db = {
  "map": {
    "info": """
 _.-._._.-._._.-._._.-._._.-._._.-._._.-._._.-._._.-._._.-._._.-._._.-._.-._
(                                                                           )
}                                                                           {
;                                       . (Coral Reef)                      ;
(                                .   .            .                         (
{                  . .        .                    .                        }
;              .       .    .                     .                         ;
)           .            . .                     .                          )
;         .                                    .                            {
(        .                                   .                              ;
{       .                               .  .                                (
;      .                             .                 (Pizza Shop). .      }
)   Start                          .                        .          .    ;
}                          (Parrot Lagoon)                 .            .   )
;                              .                      .  .             .    {
(                              .                   .                 .      ;
{                               .              .                  .         )
;                                 .        .                    .           }
)                                    .   .                    .             ;
}                                                           (X)             (
;                                                                           ;
(_.-._._.-._._.-._._.-._._.-._._.-._._.-._._.-._._.-._._.-._._.-._._.-._.-._)
\n\n""",
    "header": " (X) marks the spot!"
  },
  "scuba": {
    "info": "This is a scuba tank.",
    "header": ""
  },
  "key": {
    "info": "A giant gold key that looks to be about 300 years old.",
    "header": ""
  }
}


scene_db = {

  "initial_scene_id": "Explorer Station",

  "Explorer Station": {
    "info": "\n\nWelcome to the super secret underwater explorer station!\n\n" + 
            "A long time ago, the great pirate BlackBeard hid a bunch of gold " + 
            "nearby by putting it on a ship and then sinking it. then he " + 
            "totally forgot about it.  but luckily he also made a treasure map " + 
            "that may have path to the gold.\n\nType 'help' to see the possible " + 
            "commands at any time.\n",
    "prompt": "> ",
    "unknown_option_response": "invalid input",
    "options": {
      "look": {
        "response": "\nYou look around the explorer station. Above you is a " +
                    "giant glass dome with a bunch of fish swimming in the ocean " + 
                    "above. In front of you is an old wood table with a treasure " + 
                    "map on it.\n"
      },
      "get": {
        "map": {
          "response": "you got the map. type 'show map' to see it.",
          "gamestate": {
            "add_item": "map"
          }
        }        
      },
      "go": {
        "Coral Reef": {
          "gamestate": {
            "change_scene": "Coral Reef"
          }
        }
      },
      "use": {},
    }
  },

  "Coral Reef": {
    "info": "\nWelcome to Coral Reef!\n",
    "prompt": "> ",
    "unknown_option_response": "invalid input",
    "options": {
      "look": {
        "response": "\nYou look around the Coral Reef.  There's a bunch of " + 
                    "coral all over the place.  And some fish too.  And " + 
                    "probably a shark.  There is a wooden sign pointing south " + 
                    "that says 'Parrot Lagoon =>'.\n"
      },
      "get": {},
      "go": {
        "Parrot Lagoon": {
          "gamestate": {
            "change_scene": "Parrot Lagoon"
          }
        }
      },
      "use": {},
    }
  },

  "Parrot Lagoon": {
    "info": "\nWelcome to Parrot Lagoon!\n",
    "prompt": "> ",
    "unknown_option_response": "invalid input",
    "options": {
      "look": {
        "response": "\nYou swim to the surface to have a look around. You see " + 
                    "a beach nearby, with some palm trees. There's a giant " + 
                    "parrot in one of the trees. On the ground near the parrot " + 
                    "you see a shiny gold key. There is a sign on the beach " + 
                    "pointing back at the ocean that says 'Pizza Shop'.\n"
      },
      "get": {
        "key": {
          "response": "you got the key. type 'show key' to see it.",
          "gamestate": {
            "add_item": "key"
          }
        }        
      },
      "go": {
        "Pizza Shop": {
          "gamestate": {
            "change_scene": "Pizza Shop"
          }
        },
        "Coral Reef": {
          "gamestate": {
            "change_scene": "Coral Reef"
          }
        },
      },
      "use": {},
    }
  },

  "Pizza Shop": {
    "info": "\nWelcome to the Underwater Pizza Shop!\n",
    "prompt": "> ",
    "unknown_option_response": "invalid input",
    "options": {
      "look": {
        "response": "\nYou look around the pizza shop. There's a big oven, " + 
                    "and some pizzas in a display case. There is a Wizard " + 
                    "enjoying a slice in the corner because this is a text " + 
                    "game.\n\nThere is a menu above your head.  It reads..." + 
                    "\n\nToday's Menu\n------------------\n1) Pepperoni and " + 
                    "Seaweed Pizza\n2) Submarine Sandwich\n3) Hack the pizza " + 
                    "shop server\n"
      },
      "get": {},
      "go": {
        "Seahorse Cove": {
          "gamestate": {
            "change_scene": "Seahorse Cove"
          }
        },
        "Parrot Lagoon": {
          "gamestate": {
            "change_scene": "Parrot Lagoon"
          }
        }
      },
      "1": { 
         "response": "Good choice!"
      },
      "2": {
         "response": "Also a good choice."
      },
      "3": {
         "response": "Pizza server connection closed.",
         "gamestate": {
           "minigame": "PizzaShopServer"
         }
      },
      "use": {},
    }
  },

  "Seahorse Cove": {
    "info": "\nWelcome to Seahorse Cove!\n",
    "prompt": "> ",
    "unknown_option_response": "invalid input",
    "options": {
      "look": {
        "response": "\nYou look around Seahorse Cove. There's a seahorse " + 
                    "swimming around. And a sloop on the ocean floor. But " + 
                    "the door to the sloop is locked!\n"
      },
      "get": {},
      "go": {
        "Pizza Shop": {
          "gamestate": {
            "change_scene": "Pizza Shop"
          }
        }
      },
      "use": {
        "key": {
           "response": "\n\n    Pirate treasure obtained." + 
                       "\n\n    Congratulations!!" + 
                       "\n\n\n\n    GAME OVER\n\n\n\n\n",
           "validate": {
               "tests": [
                 {"item_exists": "key"},
               ],
               "fail_response": "You don't have a Key. there may have been a " + 
                                "key back at the Parrot Lagoon."
           },
           "gamestate": {
              "game_over": True,
              "change_scene": "Game Over"
           }
        }
      },
    }
  },

  "Game Over": { }
}
