
headline="A Growing Storm of Stellar Strength!"
rrp=49.99
release_day=20
release_month=10
release_year=2024
description= "Terawatts of electricity crash down from the sky in a tropical paradise, setting the stage for the supercharged Pikachu ex! With the power of a Stellar Tera Pokémon ex, it lights up the shoreline, revealing a parade of dragon Pokémon led by the towering Alolan Exeggutor ex! Archaludon ex and Latias ex round out the horde, while new ACE SPEC cards and more new Pokémon ex bring surprises of their own. Currents crackle and dragons roar in the Pokémon TCG: Scarlet & Violet—Surging Sparks expansion!"

"""
    Generate the product details dynamically.
    
    Parameters:
    - headline (str): The headline for the product description.
    - rrp (float): The recommended retail price of the product.
    - release_day (int): The day the product is released.
    - release_month (int): The month the product is released.
    - release_year (int): The year the product is released.
    - description (str): The description text for the product.
    
    Returns:
    - str: The complete product content text.
    """


def generate_ETB_contents(headline, rrp, release_day, release_month, release_year, description):

    template = """
{headline}
RRP: £{rrp}
Release date: {release_day}/{release_month}/{release_year}
{description}

"""
    # Use the `format` method to fill in the placeholders
    return template.format(
        headline=headline,
        rrp=rrp,
        release_day=release_day,
        release_month=release_month,
        release_year=release_year,
        description=description
    )

description = generate_ETB_contents(
    headline, 
    rrp, 
    release_day, 
    release_month, 
    release_year,
    description

)

print(description)
