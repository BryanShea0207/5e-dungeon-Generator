import random

from PIL import Image

NUMBER_MASKS = [Image.open("Room Numbers/one.png"), Image.open("Room Numbers/two.png"),
                Image.open("Room Numbers/three.png"), Image.open("Room Numbers/four.png"),
                Image.open("Room Numbers/five.png"), Image.open("Room Numbers/six.png"),
                Image.open("Room Numbers/seven.png"), Image.open("Room Numbers/eight.png"),
                Image.open("Room Numbers/nine.png"), Image.open("Room Numbers/ten.png")]


class Encounter:
    def __init__(self, amount, monsters):
        self.monsters = monsters
        self.amount = amount

    def __str__(self):
        return str("This encounter contains " + str(int(self.amount)) + " " + self.monsters.name)


class Monster:
    def __init__(self, name, book, pageNum, cr, boolSel):
        self.name = name
        self.book = book
        self.pageNum = pageNum
        self.cr = cr
        self.boolSel = boolSel

    def __str__(self):
        return str(self.name + " has a CR of " + str(self.cr) + " and can be found on page " + str(
            self.pageNum) + " of " + self.book)


class Floor:
    condition = ""

    def __init__(self, im, sides, boolMon):
        self.layout = Image.open(im)
        self.sides = sides
        self.top = sides[0]
        self.right = sides[1]
        self.bottom = sides[2]
        self.left = sides[3]
        self.boolMon = boolMon

    def setCondition(self, conStr):
        self.condition = conStr


class Room:
    condition = ""

    def __init__(self, floor, loc, roomNum):
        self.floor = floor
        self.floorImg = floor.layout.copy()
        self.floorImg.paste(NUMBER_MASKS[roomNum], (0, 0), NUMBER_MASKS[roomNum])
        self.top = floor.top
        self.right = floor.right
        self.bottom = floor.bottom
        self.left = floor.left
        self.loc = loc
        self.boolMon = floor.boolMon
        self.condition = floor.condition

    def changeSide(self, side):
        if side == 't':
            self.top = '0'
        elif side == 'r':
            self.right = '0'
        elif side == 'b':
            self.bottom = '0'
        elif side == 'l':
            self.left = '0'

    def __str__(self):
        return str("this room at " + str(self.loc[0]) + ", " + str(self.loc[1]))


ENEMIES = [
    Monster("Aarakocra", "Monster Manual", 12, .25, False),
    Monster("Aboleth", "Monster Manual", 13, 10, False),
    Monster("Deva", "Monster Manual", 16, 10, False),
    Monster("Planetar", "Monster Manual", 17, 16, False),
    Monster("Solar", "Monster Manual", 18, 21, False),
    Monster("Animated Armor", "Monster Manual", 19, 1, False),
    Monster("Flying Sword", "Monster Manual", 20, .25, False),
    Monster("Rug of Smothering", "Monster Manual", 20, 2, False),
    Monster("Ankheg", "Monster Manual", 21, 2, False),
    Monster("Azer", "Monster Manual", 22, 2, False),
    Monster("Banshee", "Monster Manual", 23, 4, False),
    Monster("Basilisk", "Monster Manual", 24, 3, False),
    Monster("Behir", "Monster Manual", 25, 11, False),
    Monster("Beholder", "Monster Manual", 28, 13, False),
    Monster("Death Tyrant", "Monster Manual", 29, 14, False),
    Monster("Spectator", "Monster Manual", 30, 3, False),
    Monster("Needle Blight", "Monster Manual", 32, .25, False),
    Monster("Twig Blight", "Monster Manual", 32, .125, False),
    Monster("Vine Blight", "Monster Manual", 32, .5, False),
    Monster("Bugbear", "Monster Manual", 33, 1, False),
    Monster("Bugbear Chief", "Monster Manual", 33, 3, False),
    Monster("Bulette", "Monster Manual", 34, 5, False),
    Monster("Bullywug", "Monster Manual", 35, .25, False),
    Monster("Cambion", "Monster Manual", 36, 5, False),
    Monster("Carrion Crawler", "Monster Manual", 37, 2, False),
    Monster("Centaur", "Monster Manual", 38, 2, False),
    Monster("Chimera", "Monster Manual", 39, 6, False),
    Monster("Chuul", "Monster Manual", 40, 4, False),
    Monster("Cloaker", "Monster Manual", 41, 8, False),
    Monster("Cockatrice", "Monster Manual", 42, .5, False),
    Monster("Couatl", "Monster Manual", 43, 4, False),
    Monster("Cyclops", "Monster Manual", 45, 6, False),
    Monster("Darkmantle", "Monster Manual", 46, .5, False),
    Monster("Death Knight", "Monster Manual", 47, 17, False),
    Monster("Demilich", "Monster Manual", 48, 18, False),
    Monster("Balor", "Monster Manual", 55, 19, False),
    Monster("Barlgura", "Monster Manual", 56, 5, False),
    Monster("Chasme", "Monster Manual", 57, 6, False),
    Monster("Dretch", "Monster Manual", 57, .25, False),
    Monster("Glsbrezu", "Monster Manual", 58, 9, False),
    Monster("Goristro", "Monster Manual", 59, 17, False),
    Monster("Hezrou", "Monster Manual", 60, 8, False),
    Monster("Manes", "Monster Manual", 60, .125, False),
    Monster("Marilith", "Monster Manual", 61, 16, False),
    Monster("Nalfshnee", "Monster Manual", 62, 13, False),
    Monster("Quasit", "Monster Manual", 63, 1, False),
    Monster("Shadow Demon", "Monster Manual", 64, 4, False),
    Monster("Vrock", "Monster Manual", 64, 6, False),
    Monster("Yochlol", "Monster Manual", 65, 10, False),
    Monster("Barbed Devil", "Monster Manual", 70, 5, False),
    Monster("Bearded Devil", "Monster Manual", 70, 3, False),
    Monster("Bone Devil", "Monster Manual", 71, 9, False),
    Monster("Chain Devil", "Monster Manual", 72, 8, False),
    Monster("Erinyes", "Monster Manual", 73, 12, False),
    Monster("Horned Devil", "Monster Manual", 74, 11, False),
    Monster("Ice Devil", "Monster Manual", 75, 14, False),
    Monster("Imp", "Monster Manual", 76, 1, False),
    Monster("Pit Fiend", "Monster Manual", 77, 20, False),
    Monster("Spined Devil", "Monster Manual", 78, 2, False),
    Monster("Allosaurus", "Monster Manual", 79, 2, False),
    Monster("Ankylosaurus", "Monster Manual", 79, 3, False),
    Monster("Plesiosaurus", "Monster Manual", 80, 2, False),
    Monster("Pteranodon", "Monster Manual", 80, .25, False),
    Monster("Triceratops", "Monster Manual", 80, 5, False),
    Monster("Tyrannosaurus Rex", "Monster Manual", 80, 8, False),
    Monster("Displacer Beast", "Monster Manual", 81, 3, False),
    Monster("Doppelganger", "Monster Manual", 8, 1, False),
    Monster("Dracolich", "Monster Manual", 84, 17, True),
    Monster("Shadow Dragon", "Monster Manual", 84, 13, True),
    Monster("Dragon", "Monster Manual", 88, 7, True),
    Monster("Dragon Turtle", "Monster Manual", 119, 17, False),
    Monster("Drider", "Monster Manual", 120, 6, False),
    Monster("Dryad", "Monster Manual", 121, 1, False),
    Monster("Duergar", "Monster Manual", 122, 1, False),
    Monster("Air Elemental", "Monster Manual", 124, 5, False),
    Monster("Earth Elemental", "Monster Manual", 124, 5, False),
    Monster("Fire Elemental", "Monster Manual", 125, 5, False),
    Monster("Water Elemental", "Monster Manual", 125, 5, False),
    Monster("Drow", "Monster Manual", 128, .25, False),
    Monster("Drow Elite Warrior", "Monster Manual", 128, 5, False),
    Monster("Drow Mage", "Monster Manual", 129, 7, False),
    Monster("Drow Priestess of Lolth", "Monster Manual", 129, 8, False),
    Monster("Empyrean", "Monster Manual", 130, 23, False),
    Monster("Ettercap", "Monster Manual", 131, 2, False),
    Monster("Ettin", "Monster Manual", 132, 4, False),
    Monster("Faerie Dragon", "Monster Manual", 133, 1, True),
    Monster("Flameskull", "Monster Manual", 134, 4, False),
    Monster("Flumph", "Monster Manual", 135, .125, False),
    Monster("Fomorian", "Monster Manual", 136, 8, False),
    Monster("Gas Spore", "Monster Manual", 138, .5, False),
    Monster("Violet Fungus", "Monster Manual", 138, .25, False),
    Monster("Galeb Duhr", "Monster Manual", 139, 6, False),
    Monster("Gargoyle", "Monster Manual", 140, 2, False),
    Monster("Dao", "Monster Manual", 143, 11, False),
    Monster("Djinni", "Monster Manual", 144, 11, False),
    Monster("Efreeti", "Monster Manual", 145, 11, False),
    Monster("Marid", "Monster Manual", 146, 11, False),
    Monster("Ghost", "Monster Manual", 147, 4, False),
    Monster("Ghast", "Monster Manual", 148, 2, False),
    Monster("Ghoul", "Monster Manual", 148, 1, False),
    Monster("Giant", "Monster Manual", 154, 5, True),
    Monster("Gibbering Mouther", "Monster Manual", 157, 2, False),
    Monster("Githyanki Warrior", "Monster Manual", 160, 3, False),
    Monster("Githyanki Knight", "Monster Manual", 160, 8, False),
    Monster("Githzerai Monk", "Monster Manual", 161, 2, False),
    Monster("Githzerai Zerth", "Monster Manual", 161, 6, False),
    Monster("Gnoll", "Monster Manual", 163, .5, False),
    Monster("Gnoll Pack Lord", "Monster Manual", 163, 2, False),
    Monster("Gnoll Fang od Yeenoghu", "Monster Manual", 163, 4, False),
    Monster("Depp Gnome", "Monster Manual", 164, .5, False),
    Monster("Goblin", "Monster Manual", 166, .25, False),
    Monster("Goblin Boss", "Monster Manual", 166, 1, False),
    Monster("Clay Golem", "Monster Manual", 168, 9, False),
    Monster("Flesh Golem", "Monster Manual", 169, 5, False),
    Monster("Iron Golem", "Monster Manual", 170, 16, False),
    Monster("Stone Golem", "Monster Manual", 170, 10, False),
    Monster("Gorgon", "Monster Manual", 171, 5, False),
    Monster("Grell", "Monster Manual", 172, 3, False),
    Monster("Grick", "Monster Manual", 173, 2, False),
    Monster("Grick Alpha", "Monster Manual", 173, 7, False),
    Monster("Griffon", "Monster Manual", 174, 2, False),
    Monster("Grimlock", "Monster Manual", 175, .25, False),
    Monster("Green Hag", "Monster Manual", 177, 5, False),
    Monster("Night Hag", "Monster Manual", 178, 7, False),
    Monster("Sea Hag", "Monster Manual", 179, 4, False),
    Monster("Harpy", "Monster Manual", 181, 1, False),
    Monster("Hell Hound", "Monster Manual", 182, 3, False),
    Monster("Helmed Horror", "Monster Manual", 183, 4, False),
    Monster("Hippogriff", "Monster Manual", 184, 1, False),
    Monster("Hobgoblin", "Monster Manual", 186, 0.5, False),
    Monster("Hobgobolin Captain", "Monster Manual", 186, 3, False),
    Monster("Hobgoblin Warlord", "Monster Manual", 187, 6, False),
    Monster("Hook Horror", "Monster Manual", 189, 3, False),
    Monster("Hydra", "Monster Manual", 190, 8, False),
    Monster("Intellect Devourer", "Monster Manual", 191, 2, False),
    Monster("Invisible Stalker", "Monster Manual", 192, 6, False),
    Monster("Jackalwere", "Monster Manual", 193, 0.5, False),
    Monster("Kenku", "Monster Manual", 194, 0.25, False),
    Monster("Kobold", "Monster Manual", 195, 0.125, False),
    Monster("Winged Kobold", "Monster Manual", 195, 0.25, False),
    Monster("Kraken", "Monster Manual", 197, 23, False),
    Monster("Kuo-Toa", "Monster Manual", 199, 0.25, False),
    Monster("Kuo-Toa Archpriest", "Monster Manual", 200, 6, False),
    Monster("Kuo-Toa Whip", "Monster Manual", 200, 1, False),
    Monster("Lamia", "Monster Manual", 201, 4, False),
    Monster("Lich", "Monster Manual", 202, 21, False),
    Monster("Lizardfolk", "Monster Manual", 204, 0.5, False),
    Monster("Lizardfolk Shaman", "Monster Manual", 205, 2, False),
    Monster("Lizardfolk Monarch", "Monster Manual", 205, 4, False),
    Monster("Werebear", "Monster Manual", 208, 5, False),
    Monster("Wereboar", "Monster Manual", 209, 4, False),
    Monster("Wererat", "Monster Manual", 209, 2, False),
    Monster("Weretiger", "Monster Manual", 210, 4, False),
    Monster("Werewolf", "Monster Manual", 211, 3, False),
    Monster("Magmin", "Monster Manual", 212, 0.5, False),
    Monster("Manticore", "Monster Manual", 213, 3, False),
    Monster("Medusa", "Monster Manual", 214, 6, False),
    Monster("Mephits", "Monster Manual", 215, .25, True),
    Monster("Merfolk", "Monster Manual", 218, 0.125, False),
    Monster("Merrow", "Monster Manual", 219, 2, False),
    Monster("Mimic", "Monster Manual", 220, 2, False),
    Monster("Mind Flayer", "Monster Manual", 222, 7, False),
    Monster("Minotaur", "Monster Manual", 223, 3, False),
    Monster("Mummy", "Monster Manual", 228, 3, False),
    Monster("Mummy Lord", "Monster Manual", 229, 15, False),
    Monster("Myconid Adult", "Monster Manual", 232, 0.5, False),
    Monster("Myconid Sovereign", "Monster Manual", 232, 2, False),
    Monster("Bone Naga", "Monster Manual", 233, 4, False),
    Monster("Spirit Naga", "Monster Manual", 234, 8, False),
    Monster("Guardian Naga", "Monster Manual", 234, 10, False),
    Monster("Nightmare", "Monster Manual", 235, 3, False),
    Monster("Nothic", "Monster Manual", 236, 2, False),
    Monster("Ogre", "Monster Manual", 237, 2, False),
    Monster("Oni", "Monster Manual", 239, 7, False),
    Monster("Black Pudding", "Monster Manual", 241, 4, False),
    Monster("Gelatinous Cube", "Monster Manual", 242, 2, False),
    Monster("Gray Ooze", "Monster Manual", 243, 0.5, False),
    Monster("Ochre Jelly", "Monster Manual", 243, 2, False),
    Monster("Orc", "Monster Manual", 246, 0.5, False),
    Monster("Orc War Chief", "Monster Manual", 246, 4, False),
    Monster("Orc Eye of Gruumsh", "Monster Manual", 247, 2, False),
    Monster("Orog", "Monster Manual", 247, 2, False),
    Monster("Otyugh", "Monster Manual", 248, 5, False),
    Monster("Owlbear", "Monster Manual", 249, 3, False),
    Monster("Pegasus", "Monster Manual", 250, 2, False),
    Monster("Peryton", "Monster Manual", 251, 2, False),
    Monster("Piercer", "Monster Manual", 252, 0.5, False),
    Monster("Pixie", "Monster Manual", 253, 0.25, False),
    Monster("Pseudodragon", "Monster Manual", 254, 0.25, False),
    Monster("Purple Worm", "Monster Manual", 255, 15, False),
    Monster("Quaggoth", "Monster Manual", 256, 2, False),
    Monster("Rakshasa", "Monster Manual", 257, 13, False),
    Monster("Young Remorhaz", "Monster Manual", 258, 5, False),
    Monster("Remorhaze", "Monster Manual", 258, 11, False),
    Monster("Revenant", "Monster Manual", 259, 5, False),
    Monster("Roc", "Monster Manual", 260, 11, False),
    Monster("Roper", "Monster Manual", 261, 5, False),
    Monster("Rust Monster", "Monster Manual", 262, 0.25, False),
    Monster("Sahuagin", "Monster Manual", 263, 0.5, False),
    Monster("Sahuagin Priestess", "Monster Manual", 264, 2, False),
    Monster("Sahuagin Baron", "Monster Manual", 264, 5, False),
    Monster("Fire Snake", "Monster Manual", 265, 1, False),
    Monster("Salamander", "Monster Manual", 266, 5, False),
    Monster("Satyr", "Monster Manual", 267, 0.5, False),
    Monster("Scarecrow", "Monster Manual", 268, 1, False),
    Monster("Shadow", "Monster Manual", 269, 0.5, False),
    Monster("Shambling Mound", "Monster Manual", 270, 5, False),
    Monster("Shield Guardian", "Monster Manual", 271, 7, False),
    Monster("Skeleton", "Monster Manual", 272, 0.25, False),
    Monster("Minotaur Skeleton", "Monster Manual", 273, 2, False),
    Monster("Warhorse Skeleton", "Monster Manual", 273, 0.5, False),
    Monster("Slaad", "Monster Manual", 276, 0.125, True),  # Needs select, Falseor
    Monster("Specter", "Monster Manual", 279, 1, False),
    Monster("Poltergeist", "Monster Manual", 279, 2, False),
    Monster("Androsphinx", "Monster Manual", 281, 17, False),
    Monster("Gynosphinx", "Monster Manual", 282, 11, False),
    Monster("Sprite", "Monster Manual", 283, 0.25, False),
    Monster("Stirge", "Monster Manual", 284, .125, False),
    Monster("Succubus/Incubus", "Monster Manual", 285, 4, False),
    Monster("Tarrasque", "Monster Manual", 286, 30, False),
    Monster("Thri-Kreen", "Monster Manual", 288, 1, False),
    Monster("Treant", "Monster Manual", 289, 9, False),
    Monster("Troglodyte", "Monster Manual", 290, 0.25, False),
    Monster("Troll", "Monster Manual", 291, 5, False),
    Monster("Umber Hulk", "Monster Manual", 292, 5, False),
    Monster("Unicorn", "Monster Manual", 294, 5, False),
    Monster("Vampire", "Monster Manual", 297, 13, False),
    Monster("Vampire Spawn", "Monster Manual", 298, 5, False),
    Monster("Water Weird", "Monster Manual", 299, 3, False),
    Monster("Wight", "Monster Manual", 300, 3, False),
    Monster("Will-O'-Wisp", "Monster Manual", 301, 2, False),
    Monster("Wraith", "Monster Manual", 302, 5, False),
    Monster("Wyvern", "Monster Manual", 303, 6, False),
    Monster("Xorn", "Monster Manual", 304, 5, False),
    Monster("Yeti", "Monster Manual", 305, 3, False),
    Monster("Abominable Yeti", "Monster Manual", 306, 9, False),
    Monster("Yuan-Ti Abomination", "Monster Manual", 308, 7, False),
    Monster("Yuan-Ti Malison", "Monster Manual", 309, 3, False),
    Monster("Yuan-Ti Pureblood", "Monster Manual", 310, 1, False),
    Monster("Arcanaloth", "Monster Manual", 313, 12, False),
    Monster("Mezzoloth", "Monster Manual", 313, 5, False),
    Monster("Nycaloth", "Monster Manual", 314, 9, False),
    Monster("Ultroloth", "Monster Manual", 314, 13, False),
    Monster("Zombie", "Monster Manual", 316, 0.25, False),
    Monster("Beholder Zombie", "Monster Manual", 316, 5, False),
    Monster("Ogre Zombie", "Monster Manual", 316, 2, False),
    Monster("Ape", "Monster Manual", 317, 0.5, False),
    Monster("Axe Beak", "Monster Manual", 317, 0.25, False),
    Monster("Black Bear", "Monster Manual", 318, 0.5, False),
    Monster("Blink Dog", "Monster Manual", 318, 0.25, False),
    Monster("Blood Hawk", "Monster Manual", 319, 0.125, False),
    Monster("Boar", "Monster Manual", 319, 0.25, False),
    Monster("Brown Bear", "Monster Manual", 319, 1, False),
    Monster("Camel", "Monster Manual", 320, 0.125, False),
    Monster("Constrictor Snake", "Monster Manual", 320, 0.25, False),
    Monster("Crocodile", "Monster Manual", 320, 0.5, False),
    Monster("Death Dog", "Monster Manual", 321, 1, False),
    Monster("Dire Wolf", "Monster Manual", 321, 1, False),
    Monster("Draft Horse", "Monster Manual", 321, 0.25, False),
    Monster("Elephant", "Monster Manual", 322, 4, False),
    Monster("Elk", "Monster Manual", 322, 0.25, False),
    Monster("Flying Snake", "Monster Manual", 322, 0.125, False),
    Monster("Giant Ape", "Monster Manual", 323, 7, False),
    Monster("Giant Badger", "Monster Manual", 323, 0.25, False),
    Monster("Giant Bat", "Monster Manual", 323, 0.25, False),
    Monster("Giant Boar", "Monster Manual", 323, 2, False),
    Monster("Giant Centipede", "Monster Manual", 323, 0.25, False),
    Monster("Giant Constrictor Snake", "Monster Manual", 324, 2, False),
    Monster("Giant Crab", "Monster Manual", 324, 0.125, False),
    Monster("Giant Crocodile", "Monster Manual", 324, 5, False),
    Monster("Giant Eagle", "Monster Manual", 324, 1, False),
    Monster("Giant Elk", "Monster Manual", 325, 2, False),
    Monster("Giant Frog", "Monster Manual", 325, 0.25, False),
    Monster("Giant Goat", "Monster Manual", 326, 0.5, False),
    Monster("Giant Hyena", "Monster Manual", 326, 1, False),
    Monster("Giant Lizard", "Monster Manual", 326, 0.25, False),
    Monster("Giant Octopus", "Monster Manual", 326, 1, False),
    Monster("Giant Owl", "Monster Manual", 327, 0.25, False),
    Monster("Giant Poisonous Snake", "Monster Manual", 327, 0.25, False),
    Monster("Giant Rat", "Monster Manual", 327, 0.125, False),
    Monster("Giant Scorpion", "Monster Manual", 327, 3, False),
    Monster("Giant Spider", "Monster Manual", 328, 1, False),
    Monster("Giant Toad", "Monster Manual", 329, 1, False),
    Monster("Giant Vulture", "Monster Manual", 329, 1, False),
    Monster("Giant Wasp", "Monster Manual", 329, 0.5, False),
    Monster("Giant Weasel", "Monster Manual", 329, 0.125, False),
    Monster("Giant Wolf Spider", "Monster Manual", 330, 0.25, False),
    Monster("Lion", "Monster Manual", 331, 1, False),
    Monster("Mammoth", "Monster Manual", 332, 6, False),
    Monster("Mastiff", "Monster Manual", 332, 0.125, False),
    Monster("Mule", "Monster Manual", 333, 0.125, False),
    Monster("Panther", "Monster Manual", 333, 0.25, False),
    Monster("Phase Spider", "Monster Manual", 334, 3, False),
    Monster("Poisonous Snake", "Monster Manual", 334, 0.125, False),
    Monster("Polar Bear", "Monster Manual", 334, 2, False),
    Monster("Pony", "Monster Manual", 335, 0.125, False),
    Monster("Rhinoceros", "Monster Manual", 336, 2, False),
    Monster("Saber-Toothed Tiger", "Monster Manual", 336, 2, False),
    Monster("Tiger", "Monster Manual", 339, 1, False),
    Monster("Warhorse", "Monster Manual", 340, 0.5, False),
    Monster("Winter Wolf", "Monster Manual", 340, 3, False),
    Monster("Wolf", "Monster Manual", 341, 0.25, False),
    Monster("Worg", "Monster Manual", 341, 0.5, False),
    Monster("Acolyte", "Monster Manual", 342, 0.25, False),
    Monster("Archmage", "Monster Manual", 342, 12, False),
    Monster("Assassin", "Monster Manual", 343, 8, False),
    Monster("Bandit", "Monster Manual", 343, 0.125, False),
    Monster("Bandit Captian", "Monster Manual", 344, 2, False),
    Monster("Berserker", "Monster Manual", 344, 2, False),
    Monster("Cultist", "Monster Manual", 345, 0.125, False),
    Monster("Cult Fanatic", "Monster Manual", 345, 2, False),
    Monster("Druid", "Monster Manual", 346, 2, False),
    Monster("Gladiator", "Monster Manual", 346, 5, False),
    Monster("Guard", "Monster Manual", 347, 0.125, False),
    Monster("Knight", "Monster Manual", 347, 3, False),
    Monster("Mage", "Monster Manual", 347, 6, False),
    Monster("Noble", "Monster Manual", 348, 0.125, False),
    Monster("Priest", "Monster Manual", 348, 2, False),
    Monster("Scout", "Monster Manual", 349, 0.5, False),
    Monster("Spy", "Monster Manual", 349, 1, False),
    Monster("Thug", "Monster Manual", 350, 0.5, False),
    Monster("Tribal Warrior", "Monster Manual", 350, 0.125, False),
    Monster("Veteran", "Monster Manual", 350, 3, False),
]

# (player,monsters,cr)
CHALLENGE = [
    # CR : 1/8 , 1/4, 1/2, 1, 2, 3, ...
    [(1, 2, .125), (1, 1, .25), (3, 1, .5), (5, 1, 1)],  # level 1
    [(1, 3, .125), (1, 2, .25), (1, 1, .5), (3, 1, 1), (6, 1, 2)],  # level 2
    [(1, 5, .125), (1, 2, .25), (1, 1, .5), (2, 1, 1), (4, 1, 2), (6, 1, 3)],  # Level 3
    [(1, 4, .25), (1, 2, .5), (1, 1, 1), (2, 1, 2), (4, 1, 3), (6, 1, 4)],  # Level 4
    [(1, 4, .5), (1, 2, 1), (1, 1, 2), (2, 1, 3), (3, 1, 4), (5, 1, 5), (6, 1, 6)],  # Level 5
    [(1, 5, .5), (1, 2, 1), (1, 1, 2), (2, 1, 3), (2, 1, 4), (4, 1, 5), (5, 1, 6), (6, 1, 7)],  # Level 6
    [(1, 6, .5), (1, 3, 1), (1, 1, 2), (1, 1, 3), (2, 1, 4), (3, 1, 5), (4, 1, 6), (5, 1, 7)],  # Level 7
    [(1, 7, .5), (1, 4, 1), (1, 2, 2), (1, 1, 3), (2, 1, 4), (3, 1, 5), (3, 1, 6), (4, 1, 7), (6, 1, 8)],  # Level 8
    [(1, 4, 1), (1, 2, 2), (1, 1, 3), (1, 1, 4), (2, 1, 5), (3, 1, 6), (4, 1, 7), (5, 1, 8), (6, 1, 9)],  # Level 9
    [(1, 5, 1), (1, 2, 2), (1, 1, 3), (1, 1, 4), (2, 1, 5), (2, 1, 6), (3, 1, 7), (4, 1, 8), (5, 1, 9), (6, 1, 10)],
    # Level 10
    [(1, 6, 1), (1, 3, 2), (1, 2, 3), (1, 1, 4), (2, 1, 5), (2, 1, 6), (2, 1, 7), (3, 1, 8), (4, 1, 9), (5, 1, 10),
     (6, 1, 11)],  # Level 11
    [(1, 3, 2), (1, 2, 3), (1, 1, 4), (1, 1, 5), (2, 1, 6), (2, 1, 7), (3, 1, 8), (3, 1, 9), (4, 1, 10), (5, 1, 11),
     (6, 1, 12)],  # Level 12
    [(1, 4, 2), (1, 2, 3), (1, 2, 4), (1, 1, 5), (1, 1, 6), (2, 1, 7), (2, 1, 8), (3, 1, 9), (3, 1, 10), (4, 1, 11),
     (5, 1, 12), (6, 1, 13)],  # Level 13
    [(1, 4, 2), (1, 3, 3), (1, 2, 4), (1, 1, 5), (1, 1, 6), (2, 1, 7), (2, 1, 8), (3, 1, 9), (3, 1, 10), (4, 1, 11),
     (4, 1, 12), (5, 1, 13), (6, 1, 14)],  # Level 14
    [(1, 5, 2), (1, 3, 3), (1, 2, 4), (1, 1, 5), (1, 1, 6), (1, 1, 7), (2, 1, 8), (2, 1, 9), (3, 1, 10), (3, 1, 11),
     (4, 1, 12), (5, 1, 13), (5, 1, 14), (6, 1, 15)],  # Level 15
    [(1, 5, 2), (1, 3, 3), (1, 2, 4), (1, 1, 5), (1, 1, 6), (1, 1, 7), (2, 1, 8), (2, 1, 9), (2, 1, 10), (3, 1, 11),
     (4, 1, 12), (4, 1, 13), (5, 1, 14), (5, 1, 15), (6, 1, 16)],  # Level 16
    [(1, 7, 2), (1, 4, 3), (1, 3, 4), (1, 2, 5), (1, 1, 6), (1, 1, 7), (1, 1, 8), (2, 1, 9), (2, 1, 10), (2, 1, 11),
     (3, 1, 12), (3, 1, 13), (4, 1, 14), (4, 1, 15), (5, 1, 16), (6, 1, 17)],  # Level 17
    [(1, 7, 2), (1, 5, 3), (1, 3, 4), (1, 2, 5), (1, 1, 6), (1, 1, 7), (1, 1, 8), (2, 1, 9), (2, 1, 10), (2, 1, 11),
     (3, 1, 12), (3, 1, 13), (4, 1, 14), (4, 1, 15), (5, 1, 16), (6, 1, 17), (6, 1, 18)],  # Level 18
    [(1, 5, 3), (1, 3, 4), (1, 2, 5), (1, 2, 6), (1, 1, 7), (1, 1, 8), (1, 1, 9), (2, 1, 10), (2, 1, 11), (2, 1, 12),
     (3, 1, 13), (3, 1, 14), (4, 1, 15), (4, 1, 16), (5, 1, 17), (6, 1, 18), (6, 1, 19)],  # Level 19
    [(1, 6, 3), (1, 4, 4), (1, 2, 5), (1, 2, 6), (1, 1, 7), (1, 1, 8), (1, 1, 9), (1, 1, 10), (2, 1, 11), (2, 1, 12),
     (2, 1, 13), (3, 1, 14), (3, 1, 15), (4, 1, 16), (4, 1, 17), (5, 1, 18), (5, 1, 19), (6, 1, 20)],  # Level 20
]

REWARDS = [
    (1,24,("Str","Dex","Con","Wis","Int","Cha","Choice")),
    (25,48,("1st","2nd","3rd","4th","5th","6th","7th","8th","9th")),
    (49,72,("cp","sp","gp")),
    (73,96,("Sword")),
    (97,100,"Nothing")
]

newName = ""


def Selector(mon):
    global newName

    # For Dragons
    colors = ["Black", "Blue", "Green", "Red", "White", "Brass", "Bronze", "Copper", "Gold", "Silver"]
    ages = ["Wyrmling", "Young", "Adult", "Ancient"]
    combinations = []
    crs = [2, 7, 14, 21, 3, 9, 16, 23, 2, 8, 15, 22, 4, 10, 17, 24, 2, 6, 13, 20, 1, 6, 13, 20, 2, 8, 15, 22, 1, 7, 14,
           21, 3, 10, 17, 24, 2, 9, 16, 23]
    index = 0

    for c in colors:
        for a in ages:
            combinations.append(a + " " + c)
            index += 1

    if mon.name == "Dracolich":
        mon.name = str(random.choice(colors) + " " + mon.name)
        mon.cr += 1
    else:
        combo = random.choice(combinations)
        newName = str(combo + " " + mon.name)
        mon.cr = crs[combinations.index(combo)]
        if mon.name.__contains__("Shadow"):
            mon.cr += 2

    if mon.name.__contains__("Faerie Dragon"):
        colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
        newColor = random.choice(colors)

        if colors.index(newColor) >= 3:
            mon.cr = 2
        else:
            mon.cr = 1

        newName = str(newColor + " " + "Faerie Dragon")

    if mon.name.__contains__("Giant"):
        options = [("Cloud", 9), ("Fire", 9), ("Frost", 8), ("Hill", 5), ("Stone", 7), ("Storm", 13)]
        type = random.choice(options)
        newName = str(type[0] + " " + "Giant")
        mon.cr = type[1]

    if mon.name.__contains__("Mephit"):
        materials = ["Dust", "Ice", "Magma", "Mud", "Smoke", "Steam"]
        type = random.choice(materials)
        if materials.index(type) <= 2:
            mon.cr = 0.5
        else:
            mon.cr = 0.25
        newName = str(type + " " + "Mephit")


def createMatch(level, players):
    global newName
    cr = 100
    ratio = 0
    while True:
        mon = ENEMIES[random.randrange(len(ENEMIES))]
        if mon.boolSel:
            Selector(mon)

        for i in range(len(CHALLENGE[level - 1])):
            if CHALLENGE[level - 1][i][2] == mon.cr:
                if CHALLENGE[level - 1][i][0] == 1:
                    ratio = CHALLENGE[level - 1][i]
                    break
                elif players % CHALLENGE[level - 1][i][0] == 0:
                    ratio = CHALLENGE[level - 1][i]
                    if newName != "":
                        mon.name = newName
                        newName = ""
                    break
        if ratio != 0:
            if newName != "":
                mon.name = newName
            break

    if ratio[0] == 1:
        num = ratio[1] * players

    else:
        num = players / ratio[0]

    if num > 8:
        return createMatch(level, players)

    if mon.name.__contains__("Hag") and num != 3:
        num = 3

    return Encounter(num, mon)


def findBoss(level, players):
    mon = random.choice(ENEMIES)
    boss = False
    if players == 1:
        if mon.cr <= level / 2:
            boss = True
    if players <= 4:
        if mon.cr == level or mon.cr == level + 1:
            boss = True
    if players > 4:
        if level + 1 <= mon.cr <= (level + (players - 4)):
            boss = True
    if boss:
        return Encounter(1, mon)
    else:
        return findBoss(level, players)
