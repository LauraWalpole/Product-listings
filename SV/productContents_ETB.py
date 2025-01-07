    
product_expansion = "Surging Sparks"
product_era = "Scarlet & Violet"
quantity_boosterpacks = 9
promo_card= "Magneton"
product_mascot = "Pikachu"


"""
    Generate a description of the contents of an Elite Trainer Box product dynamically.
    
    Parameters:
    - product_expansion (str): The expansion name.
    - product_era (str): The era of the product.
    - quantity_boosterpacks (int): Number of booster packs included in the product.
    - promo_card (str): The Pokémon featured on the promo card.
    - product_mascot (str): The mascot featured on the card sleeves.
    
    Returns:
    - str: The complete description text.
    """

def generate_ETB_description(product_expansion, product_era, quantity_boosterpacks, promo_card, product_mascot):

    template = """
Each Pokémon TCG {product_expansion} Elite Trainer Box contains:
- {quantity_boosterpacks} Pokémon TCG: {product_era}: {product_expansion} booster packs
- A promo card featuring {promo_card}
- 65 card sleeves featuring {product_mascot}
- 45 Pokémon TCG Energy cards
- A player’s guide to the {product_era}: {product_expansion} expansion
- 6 damage-counter dice
- 1 competition-legal coin-flip die
- 2 plastic condition markers
- A collector’s box to hold everything, with 4 dividers to keep it organized
- A code card for Pokémon Trading Card Game Live
"""
    # Use the `format` method to fill in the placeholders
    return template.format(
        product_expansion=product_expansion,
        product_era=product_era,
        quantity_boosterpacks=quantity_boosterpacks,
        promo_card=promo_card,
        product_mascot=product_mascot
    )

description = generate_ETB_description(
    product_expansion, 
    product_era, 
    quantity_boosterpacks, 
    promo_card, 
    product_mascot
)

print(description)
