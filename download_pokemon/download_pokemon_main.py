"""
This python module systematically downlads the google images relating to all the pokemon by type and also primary type if multi
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

def download(output, t="all", verbose=False):
    RESPONSE = google_images_download.googleimagesdownload()

    OUTPUT = os.path.dirname(output)

    def download(_names, _type):
        """
        Download all pokemon of type
        """
        done = 0
        total = 0
        print("Downloading {} pokemon images".format(_type))
        for name in _names:
            percentage = math.ceil((done / len(_names)) * 100)
            end = "\r"
            if done == len(_names):
                end = "\n"
            print("[{}] {}% Downloaded ({}/{})".format(("=" * percentage) + ">" + (" " * (100 - percentage)),
                                                percentage, done, len(_names)), end=end)
            with HiddenPrints(verbose):
                found = RESPONSE.download({"keywords": name + " pokemon", "output_directory": os.path.join(OUTPUT, _type), "image_directory": name, "limit": 25})[name + " pokemon"]
            done = done + 1
            total = total + len(found)

            count = 1
            for filename in found:
                percentage = math.ceil((count / len(found)) * 100)
                end = "\r"
                if count == len(found):
                    end = "\n"
                print("[{}] {}% Processed ({}/{})".format(("=" * percentage) + ">" + (" " * (100 - percentage)),
                                                    percentage, count, len(found)), end=end)
                extension = os.path.splitext(filename)[1]
                new_file_name = "{}_{}".format(name, count)
                new_file_name_with_ext = new_file_name+extension
                os.rename(os.path.join(OUTPUT,filename),os.path.join(OUTPUT,new_file_name_with_ext))
                count = count + 1

        print("Found {} images of {} different {} pokemon!".format(total, len(_names), _type))

    if t == "normal" or t == "all":
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

    if t == "fighting" or t == "all":
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

    if t == "flying" or t == "all":
        NAMES = ["Tornadus", "Noibat", "Noivern"]
        download(NAMES, "flying")

    if t == "poison" or t == "all":
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

    if t == "ground" or t == "all":
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

    if t == "rock" or t == "all":
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

    if t == "bug" or t == "all":
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

    if t == "ghost" or t == "all":
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

    if t == "steel" or t == "all":
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

    if t == "fire" or t == "all":
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

    if t == "water" or t == "all":
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

    if t == "grass" or t == "all":
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

    if t == "electric" or t == "all":
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

    if t == "psychic" or t == "all":
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

    if t == "ice" or t == "all":
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

    if t == "dragon" or t == "all":
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

    if t == "dark" or t == "all":
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

    if t == "fairy" or t == "all":
        NAMES = ["Clefairy", "Clefable", "Cleffa",
                "Togepi", "Snubbull", "Granbull",
                "Flabébé", "Floette", "Florges",
                "Spritzee", "Aromatisse", "Swirlix",
                "Slurpuff", "Sylveon", "Xerneas",
                "Comfey", "Togetic", "Togekiss"]
        download(NAMES, "fairy")
