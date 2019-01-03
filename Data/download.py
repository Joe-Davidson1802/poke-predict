"""
This python module systematically downlads the google images relating to all the pokemon by type and also primary type if multi
"""
import argparse
import math
import os
import sys
from google_images_download import google_images_download

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
sys.path.append(dir_path)

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

AP = argparse.ArgumentParser()
AP.add_argument("-t", "--type", required=True,
                help="type of pokemon to download (normal, water, all)")
AP.add_argument("-v", "--verbose", action='store_true',
                help="run verbosely")
AP.add_argument("-o", "--output", required=True,
                help="output_folder")
ARGS = vars(AP.parse_args())

RESPONSE = google_images_download.googleimagesdownload()

OUTPUT = os.path.dirname(ARGS["output"])

def download(_names, _type):
    """
    Download all pokemon of type
    """
    done = 0
    total = 0
    print("Downloading {} pokemon images".format(_type))
    for name in _names:
        percentage = math.ceil((done / len(_names)) * 100)
        print("[{}] {}% Done ({}/{})".format(("=" * percentage) + ">" + (" " * (100 - percentage)),
                                             percentage, done, len(_names)), end="\r")
        with HiddenPrints(ARGS["verbose"]):
            found = RESPONSE.download({"keywords": name + " pokemon", "output_directory": os.path.join(OUTPUT, _type), "image_directory": name, "limit": 25})[name + " pokemon"]
        done = done + 1
        total = total + len(found)

    print("Found {} images of {} different {} pokemon!".format(total, len(_names), _type))

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
             "Silvally", "Komala", "Farfetch'd",
             "Pidgey", "Pidgeotto", "Pidgeot",
             "Spearow", "Fearow", "Jigglypuff",
             "Wigglytuff", "Doduo", "Dodrio",
             "Hoothoot", "Noctowl", "Igglybuff",
             "Girafarig", "Taillow", "Swellow",
             "Azurill", "Swablu", "Starly",
             "Staravia", "Staraptor", "Bibarel",
             "Lopunny", "Chatot", "Pidove",
             "Tranquill", "Unfezant", "Audino",
             "Deerling", "Sawsbuck", "Rufflet",
             "Braviary", "Meloetta", "Diggersby",
             "Fletchling", "Pikipek", "Trumbeak",
             "Toucannon", "Stufful", "Bewear",
             "Oranguru", "Drampa"]
    download(NAMES, "normal")

if ARGS["type"] == "fighting" or ARGS["type"] == "all":
    NAMES = ["Mankey", "Primeape", "Machop",
             "Machoke", "Machamp", "Hitmonchan",
             "Tyrogue", "Hitmontop", "Makuhita",
             "Hariyama", "Riolu", "Timburr",
             "Gurdurr", "Conkeldurr", "Throh",
             "Sawk", "Mienfoo", "Mienshao",
             "Pancham", "Crabrawler", "Passimian",
             "Meditite", "Medicham", "Lucario",
             "Pangoro", "Hawlucha", "Crabominable",
             "Marshadow"]
    download(NAMES, "fighting")

if ARGS["type"] == "flying" or ARGS["type"] == "all":
    NAMES = ["Tornadus", "Noibat", "Noivern"]
    download(NAMES, "flying")

if ARGS["type"] == "poison" or ARGS["type"] == "all":
    NAMES = ["Ekans", "Arbok", "Nidoran♀",
             "Nidorina", "Nidoran♂", "Nidorino",
             "Grimer", "Muk", "Koffing",
             "Weezing", "Gulpin", "Swalot",
             "Seviper", "Trubbish", "Garbodor",
             "Poipole", "Nidoqueen", "Nidoking",
             "Zubat", "Golbat", "Grimer",
             "Muk", "Crobat", "Stunky",
             "Skuntank", "Skorupi", "Drapion",
             "Croagunk", "Toxicroak", "Skrelp",
             "Dragalge", "Mareanie", "Toxapex",
             "Salandit", "Salazzle", "Naganadel"]
    download(NAMES, "poison")

if ARGS["type"] == "ground" or ARGS["type"] == "all":
    NAMES = ["Sandshrew", "Sandslash", "Diglett",
             "Dugtrio", "Cubone", "Marowak",
             "Phanpy", "Donphan", "Trapinch",
             "Groudon", "Hippopotas", "Hippowdon",
             "Drilbur", "Mudbray", "Mudsdale",
             "Diglett", "Dugtrio", "Rhyhorn",
             "Rhydon", "Gligar", "Vibrava",
             "Flygon", "Baltoy", "Claydol",
             "Groudon", "Rhyperior", "Gliscor",
             "Excadrill", "Sandile", "Krokorok",
             "Krookodile", "Stunfisk", "Golett",
             "Golurk", "Landorus"
             ]
    download(NAMES, "ground")

if ARGS["type"] == "rock" or ARGS["type"] == "all":
    NAMES = ["Sudowoodo", "Nosepass", "Regirock",
             "Cranidos", "Rampardos", "Bonsly",
             "Roggenrola", "Boldore", "Gigalith",
             "rockruff", "lycanroc", "Geodude",
             "Graveler", "Golem", "Onix",
             "Omanyte", "Omastar", "Kabuto",
             "Kabutops", "Aerodactyl", "Larvitar",
             "Pupitar", "Tyranitar", "Lunatone",
             "Solrock", "Lileep", "Cradily",
             "Anorith", "Armaldo", "Shieldon",
             "Bastiodon", "Probopass", "Archen",
             "Archeops", "Terrakion", "Binacle",
             "Barbaracle", "Tyrunt", "Tyrantrum",
             "Amaura", "Aurorus", "Carbink",
             "Diancie", "Minior", "Nihilego",
             "Stakataka"]
    download(NAMES, "rock")

if ARGS["type"] == "bug" or ARGS["type"] == "all":
    NAMES = ["Caterpie", "Metapod", "Pinsir",
             "Pineco", "Wurmple", "Silcoon",
             "Cascoon", "Volbeat", "Illumise",
             "Kricketot", "Kricketune", "Burmy",
             "Karrablast", "Shelmet", "Accelgor",
             "Scatterbug", "Spewpa", "Grubbin",
             "Butterfree", "Weedle", "Kakuna",
             "Beedrill", "Paras", "Parasect",
             "Venonat", "Venomoth", "Scyther",
             "Pinsir", "Ledyba", "Ledian",
             "Spinarak", "Ariados", "Yanma",
             "Forretress", "Scizor", "Shuckle",
             "Heracross", "Beautifly", "Dustox",
             "Surskit", "Masquerain", "Nincada",
             "Ninjask", "Shedinja", "Wormadam",
             "Mothim", "Combee", "Vespiquen",
             "Yanmega", "Sewaddle", "Swadloon",
             "Leavanny", "Venipede", "Whirlipede",
             "Scolipede", "Dwebble", "Crustle",
             "Escavalier", "Joltik", "Galvantula",
             "Durant", "Larvesta", "Volcarona",
             "Genesect", "Vivillon", "Charjabug",
             "Vikavolt", "Cutiefly", "Ribombee",
             "Wimpod", "Golisopod", "Buzzwole",
             "Pheromosa"]
    download(NAMES, "bug")

if ARGS["type"] == "ghost" or ARGS["type"] == "all":
    NAMES = ["Misdreavus", "Shuppet", "Banette",
             "Duskull", "Dusclops", "Mismagius",
             "Dusknoir", "Yamask", "Cofagrigus",
             "Gastly", "Haunter", "Gengar",
             "Drifloon", "Drifblim", "Spiritomb",
             "Giratina", "Litwick", "Lampent",
             "Chandelure", "Phantump", "Trevenant",
             "Pumpkaboo", "Gourgeist", "Oricorio",
             "Sandygast", "Palossand", "Mimikyu",
             "Dhelmise"]
    download(NAMES, "ghost")

if ARGS["type"] == "steel" or ARGS["type"] == "all":
    NAMES = ["Aggron", "Registeel", "Klink",
             "Klang", "Klinklang", "Meltan",
             "Melmetal", "Jirachi", "Bronzor",
             "Bronzong", "Dialga", "Cobalion",
             "Honedge", "Doublade", "Aegislash",
             "Klefki", "Celesteela", "Magearna",
             "Metagross", "Aron", "Lairon",
             "Aggron", "Beldum", "Metang",
             "Mawile", "Skarmory", "Steelix"]
    download(NAMES, "steel")

if ARGS["type"] == "fire" or ARGS["type"] == "all":
    NAMES = ["Charmander", "Charmeleon", "Vulpix",
             "Ninetales", "Growlithe", "Arcanine",
             "Ponyta", "Rapidash", "Magmar",
             "Flareon", "Cyndaquil", "Quilava",
             "Typhlosion", "Slugma", "Magby",
             "Entei", "Torchic", "Torkoal",
             "Castform", "Chimchar", "Magmortar",
             "Tepig", "Pansear", "Simisear",
             "Darumaka", "Darmanitan", "Heatmor",
             "Fennekin", "Braixen", "Litten",
             "Torracat", "Ho-Oh", "Charizard",
             "Marowak", "Moltres", "Magcargo",
             "Combusken", "Blaziken", "Numel",
             "Camerupt", "Monferno", "Infernape",
             "Heatran", "Pignite", "Emboar",
             "Darmanitan", "Mode", "Delphox",
             "Fletchinder", "Talonflame", "Litleo",
             "Pyroar", "Volcanion", "Incineroar",
             "Oricorio", "Turtonator", "Blacephalon"
             ]
    download(NAMES, "fire")

if ARGS["type"] == "water" or ARGS["type"] == "all":
    NAMES = ["Squirtle", "Wartortle", "Blastoise",
             "Psyduck", "Golduck", "Poliwag",
             "Poliwhirl", "Seel", "Shellder",
             "Krabby", "Kingler", "Horsea",
             "Seadra", "Goldeen", "Seaking",
             "Staryu", "Magikarp", "Vaporeon",
             "Totodile", "Croconaw", "Feraligatr",
             "Politoed", "Remoraid", "Octillery",
             "Suicune", "Mudkip", "Wailmer",
             "Wailord", "Corphish", "Feebas",
             "Milotic", "Castform", "Clamperl",
             "Huntail", "Gorebyss", "Luvdisc",
             "Kyogre", "Piplup", "Prinplup",
             "Buizel", "Floatzel", "Shellos",
             "Finneon", "Lumineon", "Phione",
             "Manaphy", "Oshawott", "Dewott",
             "Samurott", "Panpour", "Simipour",
             "Tympole", "Basculin", "Alomomola",
             "Froakie", "Frogadier", "Clauncher",
             "Clawitzer", "Popplio", "Brionne",
             "Wishiwashi", "Pyukumuku""Poliwrath",
             "Tentacool", "Tentacruel", "Slowpoke",
             "Slowbro", "Dewgong", "Cloyster",
             "Starmie", "Gyarados", "Lapras",
             "Chinchou", "Lanturn", "Marill",
             "Azumarill", "Wooper", "Quagsire",
             "Slowking", "Qwilfish", "Corsola",
             "Mantine", "Kingdra", "Marshtomp",
             "Swampert", "Lotad", "Lombre",
             "Ludicolo", "Wingull", "Pelipper",
             "Carvanha", "Sharpedo", "Barboach",
             "Whiscash", "Crawdaunt", "Relicanth",
             "Empoleon", "Gastrodon", "Mantyke",
             "Palkia", "Palpitoad", "Seismitoad",
             "Tirtouga", "Carracosta", "Ducklett",
             "Swanna", "Frillish", "Jellicent",
             "Keldeo", "Greninja", "Primarina",
             "Dewpider", "Araquanid", "Bruxish",
             "Tapu Fini"]
    download(NAMES, "water")

if ARGS["type"] == "grass" or ARGS["type"] == "all":
    NAMES = ["Tangela", "Chikorita", "Bayleef",
             "Meganium", "Bellossom", "Sunkern",
             "Sunflora", "Treecko", "Grovyle",
             "Sceptile", "Seedot", "Shroomish",
             "Cacnea", "Turtwig", "Grotle",
             "Cherubi", "Cherrim", "Carnivine",
             "Tangrowth", "Leafeon", "Shaymin",
             "Snivy", "Servine", "Serperior",
             "Pansage", "Simisage", "Petilil",
             "Lilligant", "Maractus", "Chespin",
             "Quilladin", "Skiddo", "Gogoat",
             "Fomantis", "Lurantis", "Bounsweet",
             "Steenee", "Tsareena", "Bulbasaur",
             "Ivysaur", "Venusaur", "Oddish",
             "Gloom", "Vileplume", "Bellsprout",
             "Weepinbell", "Victreebel", "Exeggcute",
             "Exeggutor", "Hoppip", "Skiploom",
             "Jumpluff", "Sceptile", "Nuzleaf",
             "Shiftry", "Breloom", "Roselia",
             "Cacturne", "Tropius", "Torterra",
             "Budew", "Roserade", "Snover",
             "Abomasnow", "Shaymin", "Cottonee",
             "Whimsicott", "Foongus", "Amoonguss",
             "Ferroseed", "Ferrothorn", "Virizion",
             "Chesnaught", "Rowlet", "Dartrix",
             "Decidueye", "Morelull", "Shiinotic",
             "Kartana", "Tapu Bulu"]
    download(NAMES, "grass")

if ARGS["type"] == "electric" or ARGS["type"] == "all":
    NAMES = ["Pikachu", "Raichu", "Voltorb",
             "Electrode", "Electabuzz", "Jolteon",
             "Pichu", "Mareep", "Flaaffy",
             "Ampharos", "Elekid", "Raikou",
             "Electrike", "Manectric", "Plusle",
             "Minun", "Shinx", "Luxio",
             "Luxray", "Pachirisu", "Electivire",
             "Blitzle", "Zebstrika", "Tynamo",
             "Eelektrik", "Eelektross", "Xurkitree",
             "Zeraora", "Raichu", "Magnemite",
             "Magneton", "Zapdos", "Ampharos",
             "Magnezone", "Rotom", "Emolga",
             "Thundurus", "Helioptile", "Heliolisk",
             "Dedenne", "Oricorio", "Togedemaru",
             "Tapu Koko"
             ]
    download(NAMES, "electric")

if ARGS["type"] == "psychic" or ARGS["type"] == "all":
    NAMES = ["Abra", "Kadabra", "Alakazam",
             "Drowzee", "Hypno", "Mewtwo",
             "Mew", "Espeon", "Unown",
             "Wobbuffet", "Spoink", "Grumpig",
             "Chimecho", "Wynaut", "Deoxys",
             "Chingling", "Uxie", "Mesprit",
             "Azelf", "Cresselia", "Munna",
             "Musharna", "Gothita", "Gothorita",
             "Gothitelle", "Solosis", "Duosion",
             "Reuniclus", "Elgyem", "Beheeyem",
             "Espurr", "Meowstic", "Cosmog",
             "Cosmoem", "Necrozma", "Mr. Mime",
             "Mime Jr.", "Mewtwo", "Natu",
             "Xatu", "Lugia", "Celebi",
             "Ralts", "Kirlia", "Gardevoir",
             "Gallade", "Victini", "Woobat",
             "Swoobat", "Sigilyph", "Hoopa",
             "Oricorio", "Tapu", "Solgaleo",
             "Lunala", "Necrozma", "Mime Jr.",
             "Tapu Lele", "Mr. Mime", "Mewtwo",
             "Natu", "Xatu", "Lugia",
             "Celebi", "Ralts", "Kirlia",
             "Gardevoir", "Gallade", "Victini",
             "Woobat", "Swoobat", "Sigilyph",
             "Hoopa", "Oricorio", "Solgaleo",
             "Lunala", "Necrozma"
             ]
    download(NAMES, "psychic")

if ARGS["type"] == "ice" or ARGS["type"] == "all":
    NAMES = ["Vulpix", "Castform", "Snorunt",
             "Glalie", "Regice", "Glaceon",
             "Vanillite", "Vanillish", "Vanilluxe",
             "Cubchoo", "Beartic", "Cryogonal",
             "Bergmite", "Avalugg", "Sandshrew",
             "Sandslash", "Ninetales", "Jynx",
             "Articuno", "Swinub", "Piloswine",
             "Delibird", "Smoochum", "Spheal",
             "Sealeo", "Walrein", "Mamoswine",
             "Froslass"]
    download(NAMES, "ice")

if ARGS["type"] == "dragon" or ARGS["type"] == "all":
    NAMES = ["Dratini", "Dragonair", "Bagon",
             "Shelgon", "Axew", "Fraxure",
             "Haxorus", "Druddigon", "Goomy",
             "Sliggoo", "Goodra", "Jangmo-o",
             "Dragonite", "Altaria", "Salamence",
             "Latias", "Latios", "Rayquaza",
             "Gible", "Gabite", "Garchomp",
             "Reshiram", "Zekrom", "Kyurem",
             "Zygarde", "Forme", "Forme",
             "Hakamo-o", "Kommo-o"]
    download(NAMES, "dragon")

if ARGS["type"] == "dark" or ARGS["type"] == "all":
    NAMES = ["Meowth", "Persian", "Umbreon",
             "Poochyena", "Mightyena", "Absol",
             "Darkrai", "Purrloin", "Liepard",
             "Zorua", "Zoroark", "Rattata",
             "Raticate", "Murkrow", "Sneasel",
             "Houndour", "Houndoom", "Sableye",
             "Honchkrow", "Weavile", "Scraggy",
             "Scrafty", "Pawniard", "Bisharp",
             "Vullaby", "Mandibuzz", "Deino",
             "Zweilous", "Hydreigon", "Inkay",
             "Malamar", "Yveltal", "Guzzlord"]
    download(NAMES, "dark")

if ARGS["type"] == "fairy" or ARGS["type"] == "all":
    NAMES = ["Clefairy", "Clefable", "Cleffa",
             "Togepi", "Snubbull", "Granbull",
             "Flabébé", "Floette", "Florges",
             "Spritzee", "Aromatisse", "Swirlix",
             "Slurpuff", "Sylveon", "Xerneas",
             "Comfey", "Togetic", "Togekiss"]
    download(NAMES, "fairy")

