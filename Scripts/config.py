#config.py
#Mapping for Pokémon TCG eras
era_map = {
    "1": "Scarlet & Violet",
    "2": "Sword & Shield",
    }

#Map for Pokémon TCG Expansions
expansion_type_map = {
    "1": "Core Expansion",
    "2": "Special Set",
}

#Map for Pokémon TCG products 
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

#Map for Pokémon TCG expansions
expansion_map = {
    "swsh1": {
        "name": "Base",
        "era": "Sword & Shield",
        "type": "Core Expansion",
        "tag_line":"Welcome to the Galar region with the Pokémon TCG: Sword & Shield expansion!",
        "release_day":"07",
        "release_month":"02",
        "release_year": "2020",
        "etb_card_sleeves": "Zacian or Zamazenta",
        "etb_rrp": "42.50",
        "etb_quantity_of_packs": "8",
        "blister_promo_card": "",
        "blister_rrp": "13.50",
        "booster_box_rrp": "143.64"
    },
    "swsh2": {
        "name":"Rebel Clash",
        "era": "Sword & Shield",
        "type": "Core Expansion",
        "tag_line":"Rock out with new Pokémon!",
        "release_day":"01",
        "release_month":"05",
        "release_year": "2020",
        "etb_card_sleeves": "Copperajah",
        "etb_rrp": "42.50",
        "etb_quantity_of_packs": "8",
        "blister_promo_card": "",
        "blister_rrp": "13.50",
        "booster_box_rrp": "143.64"
    },
    "swsh3": {
        "name":"Darkness Ablaze",
        "era": "Sword & Shield",
        "type": "Core Expansion",
        "tag_line": "A Brilliant Flame on the Darkest Day!",
        "release_day":"14",
        "release_month":"08",
        "release_year": "2020",
        "etb_card_sleeves": "Eternatus",
        "etb_rrp": "42.50",
        "etb_quantity_of_packs": "8",
        "blister_promo_card": "",
        "blister_rrp": "13.50",
        "booster_box_rrp": "143.64"
    },
    "swsh3.5": {
        "name":"Champions Path",
        "era": "Sword & Shield",
        "type": "Special Set",
        "tag_line":"Embark on an exciting new adventure through the Galar region with the Pokémon TCG: Champion’s Path expansion!",
        "release_day":"25",
        "release_month":"09",
        "release_year": "2020",
        "etb_promo_card": "Charizard V",
        "etb_card_sleeves": "Gigantamax Charizard",
        "etb_rrp": "42.50",
        "etb_quantity_of_packs": "10",
        "blister_promo_card": "",
        "blister_rrp": "13.50",
        "booster_box_rrp": "143.64"
        } ,
    "swsh4": {
        "name":"Vivid Voltage",
        "era": "Sword & Shield",
        "type": "Core Expansion",
        "tag_line":"Massive Energy & Wild Color!",
        "release_day":"13",
        "release_month":"11",
        "release_year": "2020",
        "etb_card_sleeves": "Gigantamax Pikachu",
        "etb_rrp": "42.50",
        "etb_quantity_of_packs": "8",
        "blister_promo_card": "",
        "blister_rrp": "13.50",
        "booster_box_rrp": "143.64"
        },
    "swsh4.5": {
        "name":"Shining Fates",
        "era": "Sword & Shield",
        "type": "Special Set",
        "tag_line":"Reveal a Shining Destiny!",
        "release_day":"19",
        "release_month":"02",
        "release_year": "2021",
        "etb_promo_card": "Eevee VMAX",
        "etb_card_sleeves": "Gigantamax Eevee",
        "etb_rrp": "42.50",
        "etb_quantity_of_packs": "10",
        "blister_promo_card": "",
        "blister_rrp": "13.50",
        "booster_box_rrp": "143.64"
    },
    "swsh5": {
        "name":"Battle Styles",
        "era": "Sword & Shield",
        "type": "Core Expansion",
        "tag_line":"Choose Your Battle Style Wisely!",
        "release_day":"19",
        "release_month":"03",
        "release_year": "2021",
        "etb_card_sleeves": "Gigantamax Single Strike Urshifu or Gigantamax Rapid Strike Urshifu",
        "etb_rrp": "42.50",
        "etb_quantity_of_packs": "8",
        "blister_promo_card": "",
        "blister_rrp": "13.50",
        "booster_box_rrp": "143.64"
    },
    "swsh6": {
        "name":"Chilling Reign",
        "era": "Sword & Shield",
        "type": "Core Expansion",
        "tag_line":"Rule the Frozen Tundra!",
        "release_day":"18",
        "release_month":"06",
        "release_year": "21", 
        "etb_card_sleeves": "Ice Rider Calyrex or Shadow Rider Calyrex",
        "etb_rrp": "42.50",
        "etb_quantity_of_packs": "8",
        "blister_promo_card": "",
        "blister_rrp": "13.50",
        "booster_box_rrp": "143.64"
    },
    "swsh7": {
        "name":"Evolving Skies",
        "era": "Sword & Shield",
        "type": "Core Expansion",
        "tag_line":"Dynamic Power on the Horizon!",
        "release_day":"27",
        "release_month":"08",
        "release_year": "21",
        "etb_card_sleeves": "",
        "etb_rrp": "42.50",
        "etb_quantity_of_packs": "8",
        "blister_promo_card": "",
        "blister_rrp": "13.50",
        "booster_box_rrp": "143.64"
    },
    "swsh7.5": {
        "name":"Celebrations",
        "era": "Sword & Shield",
        "type": "Special Set",
        "tag_line":"Celebrate the Pokémon TCG!",
        "release_day":"08",
        "release_month":"10",
        "release_year": "21",
        "etb_promo_card": "Greninja ☆",
        "etb_card_sleeves": "the Pokémon 25 logo and lightning tail design",
        "etb_rrp": "42.50",
        "etb_quantity_of_packs": "10",
        "blister_promo_card": "",
        "blister_rrp": "13.50",
        "booster_box_rrp": "143.64"
    },
    "swsh8": {
        "name":"Fusion Strike",
        "era": "Sword & Shield",
        "type": "Core Expansion",
        "tag_line":"Styles Combine in a New Strategy!",
        "release_day":"12",
        "release_month":"11",
        "release_year": "21",
        "etb_card_sleeves": "Mew",
        "etb_rrp": "42.50",
        "etb_quantity_of_packs": "8",
        "blister_promo_card": "",
        "blister_rrp": "13.50",
        "booster_box_rrp": "143.64"
    },
    "swsh9": {
        "name":"Brilliant Stars",
        "era": "Sword & Shield",
        "type": "Core Expansion",
        "tag_line":"Constellations Align in a Show of Force!",
        "release_day":"25",
        "release_month":"02",
        "release_year": "2022",
        "etb_card_sleeves": "Arceus",
        "etb_rrp": "42.50",
        "etb_quantity_of_packs": "8",
        "blister_promo_card": "",
        "blister_rrp": "13.50",
        "booster_box_rrp": "143.64"
    },
    "swsh10": {
        "name":"Astral Radiance",
        "era": "Sword & Shield",
        "type": "Core Expansion",
        "tag_line":"Legends of Time & Space Take Charge!",
        "release_day":"27",
        "release_month":"05",
        "release_year": "2022",
        "etb_card_sleeves": "",
        "etb_rrp": "42.50",
        "etb_quantity_of_packs": "8",
        "blister_promo_card": "Darkrai",
        "blister_rrp": "13.50",
        "booster_box_rrp": "143.64"
    },
    "swsh10.5": {
        "name":"Pokémon Go",
        "era": "Sword & Shield",
        "type": "Special Set",
        "tag_line":"Get Up & Go Battle!",
        "release_day":"01",
        "release_month":"07",
        "release_year": "2023",
        "etb_quantity_of_packs": "10",
        "etb_promo_card": "Mewtwo V",
    },
    "swsh11": {
        "name":"Lost Origin",
        "era": "Sword & Shield",
        "type": "Core Expansion",
        "tag_line":"Surpass the Point of No Return!",
        "release_day":"09",
        "release_month":"09",
        "release_year": "2022",
        "etb_card_sleeves": "Giratina",
        "etb_rrp": "42.50",
        "etb_quantity_of_packs": "8",
        "blister_promo_card": "",
        "blister_rrp": "13.50",
        "booster_box_rrp": "143.64"
    },
    "swsh12": {
        "name":"Silver Tempest",
        "era": "Sword & Shield",
        "type": "Core Expansion",
        "tag_line":"Argent Adventure & Dazzling Discovery!",
        "release_day":"11",
        "release_month":"11",
        "release_year": "2022",
        "etb_card_sleeves": "Alolan Vulpix",
        "etb_rrp": "42.50",
        "etb_quantity_of_packs": "8",
        "blister_promo_card": "",
        "blister_rrp": "13.50",
        "booster_box_rrp": "143.64"
    },
    "swsh12.5": {
        "name":"Crown Zenith",
        "era": "Sword & Shield",
        "type": "Special Set",
        "tag_line":"All-Stars from Galar, Hisui & Beyond!",
        "release_day":"20",
        "release_month":"01",
        "release_year": "2023",
        "etb_promo_card": "Lucario VSTAR",
        "etb_card_sleeves": "Lucario",
        "etb_rrp": "42.50",
        "etb_quantity_of_packs": "10",
        "blister_promo_card": "",
        "blister_rrp": "13.50",
        "booster_box_rrp": "143.64"
    },
    "sv1": {
        "name":"Base",
        "era": "Scarlet & Violet",
        "type": "Core Expansion",
        "tag_line":"Begin a New Adventure with Pokémon ex!",
        "release_day":"31",
        "release_month":"03",
        "release_year":"2023",
        "etb_promo_card": "Koraidon or Miraidon",
        "etb_card_sleeves": "Koraidon or Miraidon",
        "etb_rrp": "£49.99",
        "etb_quantity_of_packs": "9",
        "blister_promo_card": "Arcanine or Dondozo",
        "blister_rrp": "13.99",
        "booster_box_rrp": "154.44"


    } ,
    "sv2": {
        "name":"Paldea Evolved",
        "era": "Scarlet & Violet",
        "type": "Core Expansion",
        "tag_line":"Command a Rousing Performance!",
        "release_day":"09",
        "release_month":"06",
        "release_year": "2023",
        "etb_promo_card": "Pikachu",
        "etb_card_sleeves": "Sprigatito, Fuecoco, and Quaxly",
        "etb_rrp": "£49.99",
        "etb_quantity_of_packs": "9",
        "blister_promo_card": "Varoom or Tinkatink",
        "blister_rrp": "13.99",
        "booster_box_rrp": "154.44"
    },
    "sv3": {
        "name":"Obsidian Flames",
        "era": "Scarlet & Violet",
        "type": "Core Expansion",
        "tag_line":"Raging Flames Forged in Darkness!",
        "release_day":"11",
        "release_month":"08",
        "release_year": "23",
        "etb_promo_card": "Charmander",
        "etb_card_sleeves": "Charmander",
        "etb_rrp": "£49.99",
        "etb_quantity_of_packs": "9",
        "blister_promo_card": "Houndstone or Eevee",
        "blister_rrp": "13.99",
        "booster_box_rrp": "154.44"
    },
    "sv3.5": {
        "name":"151",
        "era": "Scarlet & Violet",
        "type": "Special Set",
        "tag_line":"Gotta Catch ’Em All!",
        "release_day":"22",
        "release_month":"09",
        "release_year": "2023",
        "etb_promo_card": "Snorlax",
        "etb_card_sleeves": "a pattern showcasing Pokémon silhouettes from the Kanto region",
        "etb_rrp": "£49.99",
        "etb_quantity_of_packs": "9",
        "blister_promo_card": "",
        "blister_rrp": "",
        "booster_box_rrp": ""

    },
    "sv4": {
        "name":"Paradox Rift",
        "era": "Scarlet & Violet",
        "type": "Core Expansion",
        "tag_line":"Uncover the Anomalies of Area Zero!",
        "release_day":"03",
        "release_month":"11",
        "release_year": "2023",
        "etb_promo_card": "Iron Bundle or Scream Tail",
        "etb_card_sleeves": "Iron Valiant or Roaring Moon",
        "etb_rrp": "£49.99",
        "etb_quantity_of_packs": "9",
        "blister_promo_card": "Cetitan or Arctibax",
        "blister_rrp": "13.99",
        "booster_box_rrp": "154.44"
    },
    "sv4.5": {
        "name":"Paldean Fates",
        "era": "Scarlet & Violet",
        "type": "Special Set",
        "tag_line":"Shine Bright with Pokémon from Paldea!",
        "release_day":"26",
        "release_month":"01",
        "release_year":"2024",
        "etb_promo_card": "Mimikyu",
        "etb_card_sleeves": "Mimikyu",
        "etb_rrp": "£49.99",
        "etb_quantity_of_packs": "9",
        "blister_rrp": "",
        "booster_box_rrp": "",
        "booster_box_rrp":""

    },
    "sv5": {
        "name":"Temporal Forces",
        "era": "Scarlet & Violet",
        "type": "Core Expansion",
        "tag_line":"Ancient & Future Powers Endure!",
        "release_day":"22",
        "release_month":"03",
        "release_year": "2024",
        "etb_promo_card": "Flutter Mane or Iron Thorns",
        "etb_card_sleeves": "Iron Leaves or Walking Wake",
        "etb_rrp": "£49.99",
        "etb_quantity_of_packs": "9",
        "blister_promo_card": "Cyclizar or Cleffa",
        "blister_rrp": "13.99",
        "booster_box_rrp": "154.44"

    },
    "sv6": {
        "name":"Twilight Masquerade",
        "era": "Scarlet & Violet",
        "type": "Core Expansion",
        "tag_line":"A Festival of Mischief & Mystery!",
        "release_day":"24",
        "release_month":"05",
        "release_year": "2024",
        "etb_promo_card": "Teal Mask Ogerpon",
        "etb_card_sleeves": "Ogerpon",
        "etb_rrp": "£49.99",
        "etb_quantity_of_packs": "9",
        "blister_promo_card": "Revaroom or Snorlax",
        "blister_rrp": "13.99",
        "booster_box_rrp": "154.44"
    },
    "sv6.5": {
        "name":"Shrouded Fable",
        "era": "Scarlet & Violet",
        "type": "Special Set",
        "tag_line":"Shadowy Secrets & Toxic Tricks!",
        "release_day":"02",
        "release_month":"08",
        "release_year":"2024",
        "etb_promo_card": "Pecharunt",
        "etb_card_sleeves": "Okidogi, Munkidori, and Fezandipiti",
        "etb_rrp": "£49.99",
        "etb_quantity_of_packs": "9",
        "blister_rrp": "",
        "booster_box_rrp": "",
        "booster_box_rrp":""
    },
    "sv7": {
        "name":"Stellar Crown",
        "era": "Scarlet & Violet",
        "type": "Core Expansion",
        "tag_line":"An Adventure to Awaken the Power Within!",
        "release_day":"13",
        "release_month":"09",
        "release_year":"2024",
        "etb_promo_card": "Noctowl",
        "etb_card_sleeves": "Stellar Form Terapagos",
        "etb_rrp": "£49.99",
        "etb_quantity_of_packs": "9",
        "blister_promo_card": "Tinkaton or Latias",
        "blister_rrp": "13.99",
        "booster_box_rrp": "154.44"
    },
    "sv8": {
        "name":"Surging Sparks",
        "era": "Scarlet & Violet",
        "type": "Core Expansion",
        "tag_line":"A Growing Storm of Stellar Strength!",
        "release_day":"09",
        "release_month":"11",
        "release_year": "2024",
        "etb_promo_card": "Magneton",
        "etb_card_sleeves": "Pikachu",
        "etb_rrp": "£49.99",
        "etb_quantity_of_packs": "9",
        "blister_promo_card": "Zapdos or Quagsire",
        "blister_rrp": "13.99",
        "booster_box_rrp": "154.44"
    },
    "sv8.5": {
        "name":"Prismatic Evolutions",
        "era": "Scarlet & Violet",
        "type": "Special Set",
        "tag_line":" Eevee & Friends Light Up with Stellar Colors!",
        "release_day":"17",
        "release_month":"01",
        "release_year":"2025",
        "etb_promo_card": "Eevee",
        "etb_card_sleeves": "Eevee",
        "etb_rrp": "£49.99",
        "etb_quantity_of_packs": "9",
        "blister_rrp": "",
        "booster_box_rrp": "",
        "booster_box_rrp":""
    }
}

#Map for Pokémon TCG product templates
product_templates = {
    #Sword & Shield era product list
    "Sword & Shield": {
        #Sword & Shield core expansion product templates
        "Core Expansion": {
            "Elite Trainer Box": """
                <h2>{tagline}</h2>
                <h3>RRP: {etb_rrp}</h3>
                <h3>Release date: {release_day}/{release_month}/{release_year}</h3>
                <h2>What's inside?</h2>
                <p>Each {era} {name} Elite Trainer Box contains:</p>
                <ul>
                    <li>8 Pokémon TCG: {era} {name} booster packs</li>
                    <li>A promo card featuring {etb_promo_pokemon}</li>
                    <li>65 card sleeves featuring {etb_card_sleeves}</li>
                    <li>45 Pokémon TCG Energy cards</li>
                    <li>A player’s guide to the {era}: {expansion} expansion</li>
                    <li>6 damage-counter dice</li>
                    <li>1 competition-legal coin-flip die</li>
                    <li>2 plastic condition markers</li>
                    <li>A collector’s box to hold everything, with 4 dividers to keep it organised</li>
                    <li>A code card for Pokémon Trading Card Game Live</li>
                </ul>
            """,
            "Booster Box": """
                <h2>{tagline}</h2>
                <h3>RRP: {booster_box_rrp}</h3>
                <h3>Release date: {release_day}/{release_month}/{release_year}</h3>
                <h2>What's inside?</h2> 
                <p>Each Booster Box contains 36 Pokémon TCG {era} {expansion} booster packs</p> 
            """,
            "3 Pack Blister": """
                <h2>{tagline}</h2>
                <h3>RRP: {blister_rrp}</h3>
                <h3>Release date: {release_day}/{release_month}/{release_year}</h3>
                <h2>Contents</h2>
                <p> Each set contains:
                <ul>
                    <li>3 {era} {era} booster packs.</li>
                    <li>A foil promo card featuring {blister_promo_card}</li>
                    <li>A code card for Pokémon TCG Live</li>
                </ul>
                </p>
            """

        },



            
        "Special Set": {
            # Sword & Shield special set product templates
            "Elite Trainer Box": """
                    <h2>{tagline}</h2>
                    <h3>RRP: {etb_rrp}</h3>
                    <h3>Release date: {release_day}/{release_month}/{release_year}</h3>
                    <h2>What's included?</h2>
                    <p>Each {era} {expansion} Elite Trainer Box contains:</p>
                    <ul>               
                        <li>10 Pokémon TCG: {era} {expansion} booster packs</li>
                        <li>A promo card featuring {etb_promo_card}</li>
                        <li>65 card sleeves featuring {etb_card_sleeves}</li>
                        <li>45 Pokémon TCG Energy cards</li>
                        <li>A player’s guide to the {era}: {expansion} expansion</li>
                        <li>6 damage-counter dice</li>
                        <li>1 competition-legal coin-flip die</li>
                        <li>2 acrylic condition markers</li>
                        <li>A collector’s box to hold everything, with 4 dividers to keep it organised</li>
                        <li>A code card for Pokémon TCG Live</li>
                    </ul>
                """
        }
    },
    "Scarlet & Violet": {
        #Scarlet & Violet core expansion product templates
        "Core Expansion": {
            "Elite Trainer Box": """
                <h2>{tagline}</h2>
                <h3>RRP: {etb_rrp}</h3>
                <h3>Release date: {release_day}/{release_month}/{release_year}</h3>
                <h2>What's included?</h2>
                <p>Each {era} {expansion} Elite Trainer Box contains:</p>
                <ul>               
                    <li>9 Pokémon TCG: {era} {expansion} booster packs</li>
                    <li>A promo card featuring {etb_promo_card}</li>
                    <li>65 card sleeves featuring {etb_card_sleeves}</li>
                    <li>45 Pokémon TCG Energy cards</li>
                    <li>A player’s guide to the {era}: {expansion} expansion</li>
                    <li>6 damage-counter dice</li>
                    <li>1 competition-legal coin-flip die</li>
                    <li>2 acrylic condition markers</li>
                    <li>A collector’s box to hold everything, with 4 dividers to keep it organised</li>
                    <li>A code card for Pokémon TCG Live</li>
                </ul>
            """,
            "Booster Box": """
                <h2>{tagline}</h2>
                <h3>RRP: {booster_box_rrp}</h3>
                <h3>Release date: {release_day}/{release_month}/{release_year}</h3>
                <h2>What's inside?</h2> 
                <p>Each Booster Box contains 36 Pokémon TCG {era} {expansion} booster packs</p> 
            """,
            "3-pack Blister": """
                <h2>{tagline}</h2>
                <h3>RRP: {blister_rrp}</h3>
                <h3>Release date: {release_day}/{release_month}/{release_year}</h3>
                <h2>Contents</h2>
                <p> Each set contains:
                <ul>
                    <li>3 {era} {era} booster packs.</li>
                    <li>A foil promo card featuring {blister_promo_card}</li>
                    <li>A code card for Pokémon TCG Live</li>
                </ul>
                </p>
            """
        },
        "Special Set": {
            # Scarlet & Violet special set product templates
                "Elite Trainer Box": """
                    <h2>{tagline}</h2>
                    <h3>RRP: {etb_rrp}</h3>
                    <h3>Release date: {release_day}/{release_month}/{release_year}</h3>
                    <h2>What's included?</h2>
                    <p>Each {era} {expansion} Elite Trainer Box contains:</p>
                    <ul>               
                        <li>9 Pokémon TCG: {era} {expansion} booster packs</li>
                        <li>A promo card featuring {etb_promo_card}</li>
                        <li>65 card sleeves featuring {etb_card_sleeves}</li>
                        <li>45 Pokémon TCG Energy cards</li>
                        <li>A player’s guide to the {era}: {expansion} expansion</li>
                        <li>6 damage-counter dice</li>
                        <li>1 competition-legal coin-flip die</li>
                        <li>2 acrylic condition markers</li>
                        <li>A collector’s box to hold everything, with 4 dividers to keep it organised</li>
                        <li>A code card for Pokémon TCG Live</li>
                    </ul>
                """
        }
    }

}
    