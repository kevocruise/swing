import copy
import random


base_item_table = [

    # Potions
    {"type": "potion", "name": "Health Potion", "level": 0, "life_percent": 100},
    {"type": "potion", "name": "Mana Potion", "level": 0, "mana_percent": 100},

    # Swords
    {"type": "sword", "name": "Wood Sword", "level": 0, "damage": [5,6]},
    {"type": "sword", "name": "Rusted Sword", "level": 0, "damage": [8,10]},
    {"type": "sword", "name": "Iron Sword", "level": 0, "damage": [12,17]},
    {"type": "sword", "name": "Broad Sword", "level": 1, "damage": [18,23]},
    {"type": "sword", "name": "Steel Sword", "level": 2, "damage": [19,25]},
    {"type": "sword", "name": "Obsidian Sword", "level": 3, "damage": [30,34]},
    {"type": "sword", "name": "Diamond Sword", "level": 4, "damage": [40,50]},
    {"type": "sword", "name": "Volanic Sword", "level": 5, "damage": [50,60]},
    {"type": "sword", "name": "Mars Sword", "level": 10, "damage": [70]},

    # Shields
    {"type": "shield", "name": "Wood Blocker", "level": 0, "block": [10,12]},
    {"type": "shield", "name": "Small Shield", "level": 0, "block": [12,18]},
    {"type": "shield", "name": "Kite Shield", "level": 1, "block": [20,25]},
    {"type": "shield", "name": "Targe", "level": 2, "block": [25,29]},
    {"type": "shield", "name": "Large Shield", "level": 3, "block": [30,34]},
    {"type": "shield", "name": "Bone Shield", "level": 4, "block": [34,40]},
    {"type": "shield", "name": "Lantern Shield", "level": 5, "block": [40,45]},
    {"type": "shield", "name": "Heater", "level": 5, "block": [45,50]},
    {"type": "shield", "name": "Sacred Shield", "level": 10, "block": [55,60]},

    # Chest Armor
    {"type": "chest", "name": "Leather Armor", "level": 0, "defense": [10,12]},
    {"type": "chest", "name": "Fur Robes", "level": 0, "defense": [20,25]},
    {"type": "chest", "name": "Chain Mail", "level": 1, "defense": [30,34]},
    {"type": "chest", "name": "Steel Plate", "level": 2, "defense": [40,47]},
    {"type": "chest", "name": "Gold Plate", "level": 3, "defense": [50,60]},
    {"type": "chest", "name": "Lizard Scales", "level": 4, "defense": [60,66]},
    {"type": "chest", "name": "Templars Armor", "level": 5, "defense": [70,79]},
    {"type": "chest", "name": "Dragon Scales", "level": 5, "defense": [80,85]},
    {"type": "chest", "name": "Angels Mesh", "level": 10, "defense": [90,100]},
]

unique_item_table = {

    # Swords
    "Wood Sword": {"name": "The Sliver Giver", "damage": [10,12]},
    "Rusted Sword": {"name": "King Tetanus's Shot", "damage": [14,20]},
    "Iron Sword": {"name": "The Blood Spiller", "damage": [20,22]},
    "Broad Sword": {"name": "Knight's Parter", "damage": [23,26]},
    "Steel Sword": {"name": "King Slayer", "damage": [25,30]},
    "Obsidian Sword": {"name": "Widow Maker", "damage": [40,44]},
    "Diamond Sword": {"name": "Matriarch's Instrument", "damage": [60,66]},
    "Volanic Sword": {"name": "The Earth Shaker", "damage": [80,88]},
    "Mars Sword": {"name": "Deimos", "damage": [90,100]},

    # Shields
    "Wood Blocker": {"name": "Wishful Impeder", "block": [15,16]},
    "Small Shield": {"name": "Nobel Defender", "block": [26,28]},
    "Kite Shield": {"name": "The Crumpler", "block": [37,38]},
    "Large Shield": {"name": "The Wall", "block": [50,54]},
    "Target": {"name": "The Peace Keeper", "block": [64,66]},
    "Bone Shield": {"name": "Hell's Door", "block": [79,85]},
    "Mirror Shield": {"name": "Protector's Embrace", "block": [93,99]},
    "Heater": {"name": "Rapture's Riot", "block": [105,110]},
    "Sacred Shield": {"name": "The Iron Sky", "block": [130,140]},

    # Chest Armor
    "Leather Armor": {"name": "Sassy's", "defense": [15,20]},
    "Fur Robes": {"name": "Carcus of the Beast", "defense": [25,35]},
    "Chain Mail": {"name": "Blacksmith's Knit", "defense": [45,50]},
    "Steel Plate": {"name": "Blacksmith's Masterpiece", "defense": [70,72]},
    "Gold Plate": {"name": "Protector of the Bloodline", "defense": [80,86]},
    "Lizard Scales": {"name": "Armor of the Swift", "defense": [90,100]},
    "Templar's Armor": {"name": "Crusader's Choice", "defense": [100,110]},
    "Dragon Scales": {"name": "Breath of Fire", "defense": [120,130]},
    "Angels Mesh": {"name": "Saint's Watch", "defense": [150,160]},

}


def get_roll_item_drop(level, rare_chance_multiplier=1):
    """Get an item at random using the item table and roll its chances of being
    basic, magic, rare, or unique.
    :param level: The maximum item level that can be considered
    :param rare_chance_multiplier: A percent increase of finding rare version of item
    """

    # Max rare chance multiplier is 5
    if rare_chance_multiplier > 5:
        rare_chance_multiplier = 5

    # The roll is determined by a range that a random number
    # falls within. Each rarity has it's own range.
    unique_roll = 100 - (1 * rare_chance_multiplier)
    rare_roll =  100 - (5 * rare_chance_multiplier)
    magic_roll = 100 - (15 * rare_chance_multiplier)

    # Get the item base to be rolled
    base_item = None
    while base_item is None:
        _base_item = copy.deepcopy(random.choice(base_item_table))
        if _base_item["level"] <= level:
            base_item = _base_item

    base_item["rarity"] = "basic"

    # Use a random integer between 0-100 to determine which
    # rarity will be selected.
    roll = random.randint(0, 100)
    if roll >= unique_roll and base_item["name"] in unique_item_table:
        rolled_item = copy.deepcopy(unique_item_table[base_item["name"]])
        rolled_item["rarity"] = "unique"
        return rolled_item

    elif roll >= rare_roll:
        base_item["rarity"] = "rare"
        base_item["name"] = "Rare %s" % base_item["name"]

    elif roll >= magic_roll:
        base_item["rarity"] = "magic"
        base_item["name"] = "Magic %s" % base_item["name"]

    return base_item


def item_drop():
    """
    Get a list of item class instances of dropped items
    :param monster: Monster class instance that helps determine the drops
    """

    MINIMUM_DROP_AMOUNT = 0
    MAXIMUM_DROP_AMOUNT = 6
    MONSTER_LEVEL = 10
    REDUCE_DROP_PERCENT = 70
    CHANCE_MULTIPLIER = 1

    dropped_items = []

    # Calculate the amount of items that will be dropped
    num_items_dropped = random.randint(MINIMUM_DROP_AMOUNT, MAXIMUM_DROP_AMOUNT)

    # Reduce the amount of getting a drop by REDUCE_DROP_PERCENT by default.
    # Don't apply a drop reduction to a special monster.
    if REDUCE_DROP_PERCENT != 0:
        deduct = random.randrange(0, 100)
        if deduct <= REDUCE_DROP_PERCENT:
            num_items_dropped = 0
            print "reduced"

    # Select an item for each item that will drop
    for i in range(0, num_items_dropped):
        dropped_item = get_roll_item_drop(MONSTER_LEVEL, CHANCE_MULTIPLIER)
        dropped_items.append(dropped_item)

    return dropped_items
