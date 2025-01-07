#config.py

#Set product era using abbreviation
product_era_abbr= "sv"
#set Scarlet & Violet product expansion
tcg_expansion_abbr = "sv1"

#Mapping for Pokémon TCG eras
era_map = {
    "sv": "Scarlet & Violet"
    "swsh" "Sword & Shield"
}

#Mapping for Pokémon TCG expansions
expansion_map = {
    "swsh1": "Base",
    "swsh2": "Rebel Clash",
    "swsh3": "Darkness Ablaze",
    "swsh3.5": "Champions Path",
    "swsh4": "Vivid Voltage",
    "swsh4.5": "Shining Fates",
    "swsh5": "Battle Styles",
    "swsh6": "Chilling Reign",
    "swsh7": "Evolving Skies",
    "swsh7.5": "Celebrations",
    "swsh8": "Fusion Strike",
    "swsh9": "Brilliant Stars",
    "sswsh10": "Astral Radiance",
    "swsh10.5": "Pokémon Go",
    "swsh11": "Silver Tempest",
    "swsh12": "Lost Origin",
    "swsh12.5": "Crown Zenith",
    "sv1": "Base",
    "sv2": "Paldea Evolved",
    "sv3": "Obsidian Flames",
    "sv3.5": "151",
    "sv4": "Paradox Rift",
    "sv4.5": "Paldean Fates",
    "sv5": "Temporal Forces",
    "sv6": "Twilight Masquerade",
    "sv6.5": "Shrouded Fable",
    "sv7": "Stellar Crown",
    "sv8": "Surging Sparks",
    "sv8.5": "Prismatic Evolutions"
}

#Elite Trainer Box promo card map
promo_map_etb = {
    "sv1": ("Koraidon", "Miraidon"),
    "sv2": "Pikachu",
    "sv3": "Charmander",
    "sv3.5": "Snorlax",
    "sv4": ("Scream Tail", "Iron Bundle"),
    "sv4.5": "Mimikyu",
    "sv5": ("Iron Thorns", "Flutter Mane"),
    "sv6": "Teal Mask Ogerpon",
    "sv6.5": "Percharunt",
    "sv7": "Noctowl",
    "sv8": "Magneton",
    "sv8.5": "Eevee"
}

#3 pack blister promo card map

promo_map_3pack = {
    "sv1": ("Arcanine", "Dondozo"),
    "sv2": ("Varoom", "Tinkatink"),
    "sv3": ("Houndstone", "Eevee"),
    "sv4": ("Cetitan", "Arctibax"),
    "sv5": ("Cyclizar", "Cleffa"),
    "sv6": ("Revaroom", "Snorlax"),
    "sv7": ("Tinkaton", "Latias"),
    "sv8": ("Zapdos", "Quagsire")
}


#Determine full product era name from abbreviation.
product_era = era_map[product_era_abbr]

#Determine full expansion name from expansion abbreviation
product_expansion = expansion_map[tcg_expansion_abbr]

#Determine promo card name from expansion abbreviation
etb_promo = expansion_map



#Variables specific to the 'Elite Trainer Box' product
promo_card_etb = "Magneton"
product_mascot_etb = "Pikachu"
quantity_of_packs_etb = 9
rrp_etb = "49.99"

#Variables specific to the '3 pack blister' product
promo_card_1_3pack = "Charmander"
promo_card_2_3pack = "Bulbasaur"
quantity_of_packs_3pack = 3
rrp_3pack = "13.99"


#Variables specific to the 'Booster Box' product
quantity_of_packs_boosterbox = 36
rrp_booster_box = "154.44"


#Variables specific to the 'Ultra Premium Collection' product
quantity_of_packs_upc = 14
rrp_upc = "129.99"

#Variables specific to the 'Mini tin' product
quantity_of_packs_minitin = 2
rrp_mini_tin = "10.99"


#Variables specific to the 'Tin' product
quantity_of_packs_tin = 4
rrp_tin = "23.99"


#Variables specific to the 'Collection box' product
quantity_of_packs_box = 4
rrp_collection_box = "52.99"