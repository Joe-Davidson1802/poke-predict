"""
This python module systematically downlads the google images relating to all the pure-type pokemon
"""
import argparse
import math
import os
import sys
from google_images_download import google_images_download

class HiddenPrints:
    """
    Hide prints of functions called
    """
    def __init__(self, v):
        self.verbose = v
        self._original_stdout = sys.stdout
    def __enter__(self):
        if not self.verbose:
            sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.verbose:
            sys.stdout.close()
            sys.stdout = self._original_stdout

# construct the argument parser and parse the arguments
AP = argparse.ArgumentParser()
AP.add_argument("-t", "--type", required=True,
                help="type of pokemon to download (normal, water, all)")
AP.add_argument("-v", "--verbose", action='store_true',
                help="run verbosely")
ARGS = vars(AP.parse_args())

RESPONSE = google_images_download.googleimagesdownload()

def download(_names, _type):
    """
    Download all pokemon of type
    """
    done = 0
    print("Downloading {} pokemon images".format(_type))
    for name in _names:
        percentage = math.ceil((done / len(_names)) * 100)
        print("[{}] {}% Done ({}/{})".format(("=" * percentage) + ">" + (" " * (100 - percentage)),
                                             percentage, done, len(_names)), end="\r")
        with HiddenPrints(ARGS["verbose"]):
            RESPONSE.download({"keywords": name + " pokemon", "output_directory": _type})
        done = done + 1

    print("Done", _type, "type pokemon!")

if ARGS["type"] == "normal" or ARGS["type"] == "all":
    NAMES = ["Rattata", "Raticate", "Meowth",
             "Persian", "Lickitung", "Chansey",
             "Kangaskhan", "Mega Kangaskhan", "Tauros",
             "Ditto", "Eevee", "Porygon",
             "Snorlax", "Sentret", "Furret",
             "Aipom", "Dunsparce", "Teddiursa",
             "Ursaring", "Porygon2", "Stantler",
             "Smeargle", "Miltank", "Blissey",
             "Zigzagoon", "Linoone", "Slakoth",
             "Vigoroth", "Slaking", "Whismur",
             "Loudred", "Exploud", "Skitty",
             "Delcatty", "Spinda", "Zangoose",
             "Castform", "Kecleon", "Bidoof",
             "Ambipom", "Buneary", "Lopunny",
             "Glameow", "Purugly", "Happiny",
             "Munchlax", "Lickilicky", "Porygon-Z",
             "Regigigas", "Arceus", "Patrat",
             "Watchog", "Lillipup", "Herdier",
             "Stoutland", "Audino", "Minccino",
             "Cinccino", "Bouffalant", "Bunnelby",
             "Furfrou", "Yungoos", "Gumshoos",
             "Silvally", "Komala"]
    download(NAMES, "normal")

if ARGS["type"] == "fighting" or ARGS["type"] == "all":
    NAMES = ["Mankey", "Primeape", "Machop",
             "Machoke", "Machamp", "Hitmonchan",
             "Tyrogue", "Hitmontop", "Makuhita",
             "Hariyama", "Riolu", "Timburr",
             "Gurdurr", "Conkeldurr", "Throh",
             "Sawk", "Mienfoo", "Mienshao",
             "Pancham", "Crabrawler", "Passimian"]
    download(NAMES, "fighting")

if ARGS["type"] == "poison" or ARGS["type"] == "all":
    NAMES = ["Ekans", "Arbok", "Nidoran♀",
             "Nidorina", "Nidoran♂", "Nidorino",
             "Grimer", "Muk", "Koffing",
             "Weezing", "Gulpin", "Swalot",
             "Seviper", "Trubbish", "Garbodor",
             "Poipole"]
    download(NAMES, "poison")

if ARGS["type"] == "ground" or ARGS["type"] == "all":
    NAMES = ["Sandshrew", "Sandslash", "Diglett",
             "Dugtrio", "Cubone", "Marowak", "Phanpy",
             "Donphan", "Trapinch", "Groudon", "Hippopotas",
             "Hippowdon", "Drilbur", "Mudbray", "Mudsdale"]
    download(NAMES, "ground")

if ARGS["type"] == "rock" or ARGS["type"] == "all":
    NAMES = ["Sudowoodo", "Nosepass", "Regirock",
             "Cranidos", "Rampardos", "Bonsly",
             "Roggenrola", "Boldore", "Gigalith",
             "rockruff", "lycanroc"]
    download(NAMES, "rock")

if ARGS["type"] == "bug" or ARGS["type"] == "all":
    NAMES = ["Caterpie", "Metapod", "Pinsir",
             "Pineco", "Wurmple", "Silcoon",
             "Cascoon", "Volbeat", "Illumise",
             "Kricketot", "Kricketune", "Burmy",
             "Karrablast", "Shelmet", "Accelgor",
             "Scatterbug", "Spewpa", "Grubbin"]
    download(NAMES, "bug")
