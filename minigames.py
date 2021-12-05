
"""
A minigame that creates a fake linux command line and file system
so the player can search the file system for clues as part of the
treasure hunt. The clue will be a file that the user can print, if
they can find it. commands include pwd, ls, cd, cat, less, more,
tail, head, exit.

Only available at the Underwater Pizza Shop
"""

def clear_screen():
    print("\033[2J")
    print("\033[0;3H")

class Directory:
    """
    A fake linux Directory
    """
    def __init__(self, name, parent=None):
        self.name = name
        self.files = {}
        self.subdirs = {}
        self.parent_dir = parent
        self.subdirs[".."] = self.parent_dir

    def addSubDir(self, name, subdir):
        self.subdirs[name] = subdir

    def addfile(self, name, new_file):
        self.files[name] = new_file

    def fullpath(self):
        current = self
        parent = current.parent_dir
        path_items = []
        while parent != None:
            parent = current.parent_dir
            path_items.append(current.name)
            current = current.parent_dir
        return "/".join(path_items[::-1])

    def getSubdirectory(self, subdir_path):
        if not subdir_path:
            return self
        path_items = subdir_path.split("/")
        this_dir = self
        for subdir_name in path_items:
            if subdir_name in this_dir.subdirs:
                this_dir = this_dir.subdirs[subdir_name]
            else:
                 return None
        return this_dir

class File:
    """
    A fake linux File
    """
    def __init__(self, name, parent_dir):
        self.parent_dir = parent_dir
        self.name = name
        self.content = "" 


class PizzaShopServer:
    """
    Create a fake linux command line and file structure so the player can hack
    into the Pizza shop's server, and look for clues to find the treasure.
    """

    def __init__(self):
        self.file_structure = {
          "/": {
            "bin": {},
            "lib": {},
            "etc": {
              "pirate_data": {
                 "secret_sunken_treasure_location.txt": """

 To: PirateCrew
 Subject: Treasure Manifest
 CC: BlackBeard


 Arrr!

  On this day, January teh 1st, 1709, we pirates did load the following items of great value onto a sloop, and sunk it into the briny deep!  

  ,====================================,
  | 1,000,000  |  Pieces of 8          |
  |   500,000  |  Pieces of 16         |
  |    60,000  |  Bars of silver       |
  |       500  |  Gold plated cannons  |
  |       500  |  Gold plated swords   |
  |       100  |  Pieces gold flatware |
  `------------------------------------'

 The gold may be found at the bottom of Seahorse Cove.


 BlackBeard
    ~.~
"""
              }
            },
          }
        }
        self.root_dir = Directory("/")
        q = [(self.root_dir, self.file_structure["/"])]
        while q:
            node, json = q.pop(0)
            for k,v in json.items():
                if k != "..":
                    if type(v) == dict:
                        new_dir = Directory(k, node)
                        node.addSubDir(k, new_dir)
                        q.append( (new_dir, v) )
                    elif type(v) == str:
                        new_file = File(k, node)
                        node.addfile(k, new_file)
                        new_file.content = v

    def format_text(self, text, color=None, weight=None):
        """
        Add font and color to command line output
        """
        weights = {"bold": "1",
                   "reset": "0"}

        colors = {"red":   "31",
                  "blue":  "34",
                  "black": "30",
                  "green": "32"}

        prefix = "\033["
        suffix = "\033[0m"

        output = prefix

        if weight:
            output += weights[weight]

        output += ";"

        if color:
            output += colors[color]

        output += "m" + text + suffix

        return output



    def start_session(self):
        """
        Handle command line input like cd, ls, cat, etc..
        """

        clear_screen()
        server_greeting = "Underwater Pizza Shop Server"
        server_log = "Last login: Sat Jan 1, 1709 on ttys001\nuser: BlackBeard5000"
        print(self.format_text(server_greeting, "red", "bold"))
        print(self.format_text(server_log, "black", "bold"))

        current_dir = self.root_dir

        while True:

            cmd = input("% ").strip().split()

            if cmd[0] == "cd":
                if cmd[1] in current_dir.subdirs:
                    current_dir = current_dir.subdirs[cmd[1]] 

            elif cmd[0] == "ls":
                if len(cmd) == 1:
                    print("\t".join([self.format_text(k, "blue", "bold") for k,v in current_dir.subdirs.items()]))
                    print("\t".join([self.format_text(k, "green", "bold") for k,v in current_dir.files.items()]))
                else:
                    subdir_name = cmd[1]

                    subdir = current_dir.getSubdirectory(subdir_name)
                    if subdir:
                        print("\t".join([self.format_text(k, "blue", "bold") for k,v in subdir.subdirs.items()]))
                        print("\t".join([self.format_text(k, "green", "bold") for k,v in subdir.files.items()]))
                    else:
                        print("Path not found")
                    
            elif cmd[0] == "pwd":
                print(current_dir.fullpath())

            elif cmd[0] in ["cat", "less", "more", "tail", "head"]:

                path_items = cmd[1].split("/")
                filename = path_items.pop()

                subdir = current_dir.getSubdirectory('/'.join(path_items))

                if subdir and filename in subdir.files:
                    print(subdir.files[filename].content)
                else:
                    print("File not found.")

            elif cmd[0] == "exit":
                clear_screen()
                return


