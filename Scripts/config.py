#config.py
#Mapping for Pokémon TCG eras
era_map = {
    "1": "Scarlet & Violet",
    "2": "Sword & Shield",
    }

expansion_type_map = {
    "1": "Core Expansion",
    "2": "Special Set",
}

product_map = {
    "Core Expansion": [
        "Elite Trainer Box",
        "Booster Box",
        "3-pack Blister"
    ],
    "Special Set": [
        "Elite Trainer Box",
        "Booster Bundle",
        "Collection Box",
        "Premium Collection Box",
        "Ultra Premium Collection",
        "Mini Tin",
        "Tin"
    ]
}

expansion_map = {
    "swsh1": {
        "name": "Base",
        "type": "Core Expansion",
        "tag_line":"Welcome to the Galar region with the Pokémon TCG: Sword & Shield expansion!",
        "release_day":"07",
        "release_month":"02",
        "release_year": "2020"
    },
    "swsh2": {
        "name":"Rebel Clash",
        "type": "Core Expansion",
        "tag_line":"Rock out with new Pokémon!",
        "release_day":"01",
        "release_month":"05",
        "release_year": "2020",
    },
    "swsh3": {
        "name":"Darkness Ablaze",
        "type": "Core Expansion",
        "tag_line": "A Brilliant Flame on the Darkest Day!",
        "release_day":"14",
        "release_month":"08",
        "release_year": "2020",
    },
    "swsh3.5": {
        "name":"Champions Path",
        "type": "Special Set",
        "tag_line":"Embark on an exciting new adventure through the Galar region with the Pokémon TCG: Champion’s Path expansion!",
        "release_day":"25",
        "release_month":"09",
        "release_year": "2020",
        } ,
    "swsh4": {
        "name":"Vivid Voltage",
        "type": "Core Expansion",
        "tag_line":"Massive Energy & Wild Color!",
        "release_day":"13",
        "release_month":"11",
        "release_year": "2020",
        },
    "swsh4.5": {
        "name":"Shining Fates",
        "type": "Special Set",
        "tag_line":"Reveal a Shining Destiny!",
        "release_day":"19",
        "release_month":"02",
        "release_year": "2021",
    },
    "swsh5": {
        "name":"Battle Styles",
        "type": "Core Expansion",
        "tag_line":"Choose Your Battle Style Wisely!",
        "release_day":"19",
        "release_month":"03",
        "release_year": "2021",
    },
    "swsh6": {
        "name":"Chilling Reign",
        "type": "Core Expansion",
        "tag_line":"Rule the Frozen Tundra!",
        "release_day":"18",
        "release_month":"06",
        "release_year": "21", 
    },
    "swsh7": {
        "name":"Evolving Skies",
        "type": "Core Expansion",
        "tag_line":"Dynamic Power on the Horizon!",
        "release_day":"27",
        "release_month":"08",
        "release_year": "21",
    },
    "swsh7.5": {
        "name":"Celebrations",
        "type": "Special Set",
        "tag_line":"Celebrate the Pokémon TCG!",
        "release_day":"08",
        "release_month":"10",
        "release_year": "21",
    },
    "swsh8": {
        "name":"Fusion Strike",
        "type": "Core Expansion",
        "tag_line":"Styles Combine in a New Strategy!",
        "release_day":"12",
        "release_month":"11",
        "release_year": "21",
    },
    "swsh9": {
        "name":"Brilliant Stars",
        "type": "Core Expansion",
        "tag_line":"Constellations Align in a Show of Force!",
        "release_day":"25",
        "release_month":"02",
        "release_year": "2022",
    },
    "swsh10": {
        "name":"Astral Radiance",
        "type": "Core Expansion",
        "tag_line":"Legends of Time & Space Take Charge!",
        "release_day":"27",
        "release_month":"05",
        "release_year": "2022",
    },
    "swsh10.5": {
        "name":"Pokémon Go",
        "type": "Special Set",
        "tag_line":"Get Up & Go Battle!",
        "release_day":"01",
        "release_month":"07",
        "release_year": "2023",
    },
    "swsh11": {
        "name":"Lost Origin",
        "type": "Core Expansion",
        "tag_line":"Surpass the Point of No Return!",
        "release_day":"09",
        "release_month":"09",
        "release_year": "2022",
    },
    "swsh12": {
        "name":"Silver Tempest",
        "type": "Core Expansion",
        "tag_line":"Argent Adventure & Dazzling Discovery!",
        "release_day":"11",
        "release_month":"11",
        "release_year": "2022",
    },
    "swsh12.5": {
        "name":"Crown Zenith",
        "type": "Special Set",
        "tag_line":"All-Stars from Galar, Hisui & Beyond!",
        "release_day":"20",
        "release_month":"01",
        "release_year": "2023",
    },
    "sv1": {
        "name":"Base",
        "type": "Core Expansion",
        "tag_line":"Begin a New Adventure with Pokémon ex!",
        "release_day":"31",
        "release_month":"03",
        "release_year":"2023",
    } ,
    "sv2": {
        "name":"Paldea Evolved",
        "type": "Core Expansion",
        "tag_line":"Command a Rousing Performance!",
        "release_day":"09",
        "release_month":"06",
        "release_year": "2023",
    },
    "sv3": {
        "name":"Obsidian Flames",
        "type": "Core Expansion",
        "tag_line":"Raging Flames Forged in Darkness!",
        "release_day":"11",
        "release_month":"08",
        "release_year": "23",
    },
    "sv3.5": {
        "name":"151",
        "type": "Special Set",
        "tag_line":"Gotta Catch ’Em All!",
        "release_day":"22",
        "release_month":"09",
        "release_year": "2023",
    },
    "sv4": {
        "name":"Paradox Rift",
        "type": "Core Expansion",
        "tag_line":"Uncover the Anomalies of Area Zero!",
        "release_day":"03",
        "release_month":"11",
        "release_year": "2023",
    },
    "sv4.5": {
        "name":"Paldean Fates",
        "type": "Special Set",
        "tag_line":"Shine Bright with Pokémon from Paldea!",
        "release_day":"26",
        "release_month":"01",
        "release_year":"2024",
    },
    "sv5": {
        "name":"Temporal Forces",
        "type": "Core Expansion",
        "tag_line":"Ancient & Future Powers Endure!",
        "release_day":"22",
        "release_month":"03",
        "release_year": "2024",
    },
    "sv6": {
        "name":"Twilight Masquerade",
        "type": "Core Expansion",
        "tag_line":"A Festival of Mischief & Mystery!",
        "release_day":"24",
        "release_month":"05",
        "release_year": "2024",
    },
    "sv6.5": {
        "name":"Shrouded Fable",
        "type": "Special Set",
        "tag_line":"Shadowy Secrets & Toxic Tricks!",
        "release_day":"02",
        "release_month":"08",
        "release_year":"2024",
    },
    "sv7": {
        "name":"Stellar Crown",
        "type": "Core Expansion",
        "tag_line":"An Adventure to Awaken the Power Within!",
        "release_day":"13",
        "release_month":"09",
        "release_year":"2024",
    },
    "sv8": {
        "name":"Surging Sparks",
        "type": "Core Expansion",
        "tag_line":"A Growing Storm of Stellar Strength!",
        "release_day":"09",
        "release_month":"11",
        "release_year": "2024",
    },
    "sv8.5": {
        "name":"Prismatic Evolutions",
        "type": "Special Set",
        "tag_line":" Eevee & Friends Light Up with Stellar Colors!",
        "release_day":"17",
        "release_month":"01",
        "release_year":"2025", 
    }
    }







#Mapping for Pokémon TCG Sword & Shield RRP's for core products
rrp_map_swsh_core = {
    "rrp_etb":"42.50",
    "rrp_boosterbox":"143.64",
    "rrp_blister":"13.50",
}



booster_box_map_sv_core = {
    "rrp":"154.44",
    "quantity_of_packs":"36"

}

#Mapping for Pokémon TCG Scarlet & Violet Elite Trainer Box product
etb_map_sv = {
    "rrp":"49.99",
    "quantity_of_packs":"9",
    "promo_card":{
        "sv1": "Koraidon or Miraidon",
        "sv2": "Pikachu",
        "sv3": "Charmander",
        "sv3.5": "Snorlax",
        "sv4": "Scream Tail or Iron Bundle",
        "sv4.5": "Mimikyu",
        "sv5": "Flutter Mane or Iron Thorns",
        "sv6": "Teal Mask Ogerpon",
        "sv6.5": "Pecharunt",
        "sv7": "Noctowl",
        "sv8": "Magneton",
        "sv8.5": "Eevee"
    },
    "card_sleeves":{
        "sv1": "Koraidon or Miraidon",
        "sv2": "Sprigatito, Fuecoco, and Quaxly",
        "sv3": "Charmander",
        "sv3.5": "Snorlax",
        "sv4": "Roaring Moon or Iron Valiant",
        "sv4.5": "Mimikyu",
        "sv5": "Walking Wake or Iron Leaves",
        "sv6": "Ogerpon",
        "sv6.5": "Okidogi, Munkidori, and Fezandipiti",
        "sv7": "Stellar Form Terapagos",
        "sv8": "Pikachu",
        "sv8.5": "Eevee"
    }
}

#Mapping for Pokémon TCG Scarlet & Violet 3 pack blister product
triple_blister_map_sv_core = {
    "rrp":"13.99",
    "quantity_of_packs":"3",
    "promo_card":{
        "sv1": "Arcanine or Dondozo",
        "sv2": "Varoom or Tinkatink",
        "sv3": "Houndstone or Eevee",
        "sv4": "Cetitan or Arctibax",
        "sv5": "Cyclizar or Cleffa",
        "sv6": "Revaroom or Snorlax",
        "sv7": "Tinkaton or Latias",
        "sv8": "Zapdos or Quagsire"
        }
    }


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

