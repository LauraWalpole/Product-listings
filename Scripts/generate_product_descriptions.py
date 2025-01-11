import config


"""
Generate ETB product details dynamically.

"""

def generate_sv_etb_description(tcg_expansion_abbr):
    """
    Generate the description for an Elite Trainer Box based on the expansion abbreviation.
    """
    expansion_data = config.expansion_map_sv_core.get(tcg_expansion_abbr,{})
    
    #Retreive the attributes for the expansion
    name = expansion_data.get("name")
    tag_line = expansion_data.get("tag_line")
    release_day = expansion_data.get("release_day")
    release_month = expansion_data.get("release_month")
    release_year = expansion_data.get("release_year")


    etb_data = config.etb_map_sv.get(tcg_expansion_abbr,{})

    rrp=etb_data.get("rrp")
    quantity_of_packs=etb_data.get("quantity_of_packs")
    promo_card=etb_data.get("")
    card_sleeves=etb_data.get("")

    #Retreive the attributes for the Elite trainer box


    #Insert expansion data into ETB template


    #Insert product data into ETB template
    etb_description = f"""
    RRP = {rrp}
    Release date: {release_day}/{release_month}/{release_year}
    {tag_line}
    Each Pokémon TCG Scarlet & Violet {name} Elite Trainer Box contains:
    - {quantity_of_packs} Pokémon TCG: Scarlet & Violet: {name} booster packs
    - A promo card featuring {promo_card}
    - 65 card sleeves featuring {card_sleeves}
    - 45 Pokémon TCG Energy cards
    - A player’s guide to the Pokémon TCG Scarlet & Violet {name} expansion
    - 6 damage-counter dice
    - 1 competition-legal coin-flip die
    - 2 plastic condition markers
    - A collector’s box to hold everything, with 4 dividers to keep it organised
    - A code card for Pokémon Trading Card Game Live
    """
