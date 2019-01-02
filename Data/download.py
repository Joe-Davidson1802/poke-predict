from google_images_download import google_images_download
import argparse
import math
import os, sys

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--type", required=True,
	help="type of pokemon to download (normal, water, all)")
ap.add_argument("-v", "--verbose", action='store_true',
	help="run verbosely")
args = vars(ap.parse_args())
print(args["verbose"])

response = google_images_download.googleimagesdownload()

def download(_names, _type):
    done = 0
    print("Downloading {} pokemon images".format(_type))
    for name in _names:
        percentage = math.ceil((done / len(_names)) * 100)
        print("[{}] {}% Done ({}/{})".format(("=" * percentage) + ">" + (" " * (100 - percentage)), percentage, done, len(_names)), end="\r")
        with HiddenPrints():
            response.download({ "keywords": name + " pokemon", "output_directory": _type })
        done = done + 1

    print("Done",_type,"type pokemon!")

if args["type"] == "normal" or args["type"] == "all":
    names = ["Rattata","Raticate","Meowth",
        "Persian","Lickitung","Chansey",
        "Kangaskhan","Mega Kangaskhan","Tauros",
        "Ditto","Eevee","Porygon",
        "Snorlax","Sentret","Furret",
        "Aipom","Dunsparce","Teddiursa",
        "Ursaring","Porygon2","Stantler",
        "Smeargle","Miltank","Blissey",
        "Zigzagoon","Linoone","Slakoth",
        "Vigoroth","Slaking","Whismur",
        "Loudred","Exploud","Skitty",
        "Delcatty","Spinda","Zangoose",
        "Castform","Kecleon","Bidoof",
        "Ambipom","Buneary","Lopunny",
        "Glameow","Purugly","Happiny",
        "Munchlax","Lickilicky","Porygon-Z",
        "Regigigas","Arceus","Patrat",
        "Watchog","Lillipup","Herdier",
        "Stoutland","Audino","Minccino",
        "Cinccino","Bouffalant","Bunnelby",
        "Furfrou","Yungoos","Gumshoos",
        "Silvally","Komala"]
    download(names, args["type"])

if args["type"] == "fighting" or args["type"] == "all":
    names = ["Mankey","Primeape","Machop",
        "Machoke","Machamp","Hitmonchan",
        "Tyrogue","Hitmontop","Makuhita",
        "Hariyama","Riolu","Timburr",
        "Gurdurr","Conkeldurr","Throh",
        "Sawk","Mienfoo","Mienshao",
        "Pancham","Crabrawler","Passimian"]
    download(names, args["type"])

if args["type"] == "poison" or args["type"] == "all":
    names = ["Ekans","Arbok","Nidoran♀",
        "Nidorina","Nidoran♂","Nidorino",
        "Grimer","Muk","Koffing",
        "Weezing","Gulpin","Swalot",
        "Seviper","Trubbish","Garbodor",
        "Poipole"]
    download(names, args["type"])