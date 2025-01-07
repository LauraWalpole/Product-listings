    
product_expansion = "Surging Sparks"
product_era = "Scarlet & Violet"
quantity_boosterpacks = 3
promo_card_1= "Zapdos"
promo_card_2="Quagsire"


"""
    Generate a description of the contents of a blister pack product dynamically.
    
    Parameters:
    - product_expansion (str): The expansion name.
    - product_era (str): The era of the product.
    - quantity_boosterpacks (int): Number of booster packs included in the product.
    - promo_card_1 (str): One of the possible Pokémon featured on the promo card.
    - promo_card_2 (str): Another possible Pokémon featured on the promo card.
    
    Returns:
    - str: The complete description text.
    """

def generate_blister_pack_description(product_expansion, product_era, quantity_boosterpacks, promo_card_1, promo_card_2):

    template = """
Each Pokémon TCG {product_era}: {product_expansion} blister pack contains:
- {quantity_boosterpacks} Pokémon TCG {product_era} {product_expansion} booster packs
- A foil promo card featuring {promo_card_1} or {promo_card_2}
"""
    # Use the `format` method to fill in the placeholders
    return template.format(
        product_expansion=product_expansion,
        product_era=product_era,
        quantity_boosterpacks=quantity_boosterpacks,
        promo_card_1=promo_card_1,
        promo_card_2=promo_card_2
    )

description = generate_blister_pack_description(
    product_expansion, 
    product_era, 
    quantity_boosterpacks, 
    promo_card_1, 
    promo_card_2
)

print(description)
