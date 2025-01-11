import config

# Select the Pokémon TCG era from the era map
def select_tcg_era():
    print("Select Pokémon TCG era: ")
    for key, era in config.era_map.items():
        print(f"{key}: {era}")
    era_selection = input("Enter the number corresponding to the TCG Era: ")
    return config.era_map.get(era_selection, None)

#Select the expansion type from the expansion type map
def select_expansion_type():
     print(f"\nSelect Expansion Type for the product:")
     for key, type in config.expansion_type_map.items():
        print(f"{key}: {type}")
     expansion_type_selection = input("Enter the number corresponding to the TCG expansion type: ")
     return config.expansion_type_map.get(expansion_type_selection, None)

#Select the product from the product map
def select_product(expansion_type):
     #Filter products bys expansion type
     product_options=config.product_map.get(expansion_type)
     if not product_options:
          print(f"Expansion type does not map to product map")
          return None
     
     #List the relevant product options
     print(f"\nSelect a product for the {expansion_type}: ")
     for key, product in enumerate(product_options, start=1):
          print(f"{key}:{product}")

     #Get user input
     product_selection=input("Enter the number corresponding to the product: ")

     #Validate input and return the selected product
     if product_selection.isdigit() and 1<= int(product_selection) <=len(product_options):
          product=product_options[int(product_selection)-1]
          return product
     else:
          print("Invalid product selection.")
          return None

#Select the Pokémon TCG expansion
def select_expansion(era, expansion_type):
     #Filter expansions by era and expansion type
     expansion_options = [
          key for key, details in config.expansion_map.items()
          if details["era"] == era and details["type"] == expansion_type
     ]
     if not expansion_options:
          print(f"No expansions available")
          return None
     
     #List the expansions
     print(f"\nSelect an expansion from the Pokémon TCG {era} {expansion_type}s: ")
     for key, expansion in enumerate(expansion_options, start=1):
          print(f"{key}:{config.expansion_map[expansion]['name']}")
     
     #User selects an expansion from the list
     expansion_selection = input("Enter the number corresponding to the expansion: ")

     #Validate selection and return the expansion
     if expansion_selection.isdigit() and 1 <= int(expansion_selection) <= len(expansion_options):
          expansion = expansion_options[int(expansion_selection) - 1]
          print(f"\nYou selected: {config.expansion_map[expansion]['name']}")
          return expansion
     else:
          print("Invalid expansion.")
          return None


#Retreive the product description template
def get_product_description(era, expansion_type, product):
     try:
          #Access nested dictionary and find template matching the era, expansion type and product values
          template = config.product_templates[era][expansion_type][product]
          return template
     except KeyError:
          return "No template found for era: {era}, type: {expansion_type}, product: {product}"
     
#Generate a product description
def generate_product_description(era, expansion_type, product, expansion):
     #Retreive the expansion details
     expansion_details = config.expansion_map.get(expansion)
     if not expansion_details:
          return "Invalid expansion key. Unable to generate description."
     
     #Get the product descriptioin template
     template = get_product_description(era, expansion_type, product)
     if "No template found" in template:
          return template
     
     #Format the template using the expansion data
     description = template.format(
          era=expansion_details["era"],
          expansion=expansion_details["name"],
          tagline=expansion_details["tag_line"],
          release_day=expansion_details["release_day"],
          release_month=expansion_details["release_month"],
          release_year=expansion_details["release_year"],
          etb_promo_card=expansion_details.get("etb_promo_card"),
          etb_card_sleeves=expansion_details.get("etb_card_sleeves"),
          etb_rrp=expansion_details["etb_rrp"],
          blister_promo_card=expansion_details["blister_promo_card"],
          blister_rrp=expansion_details["blister_rrp"],
          booster_box_rrp=expansion_details["booster_box_rrp"]
     )
     return description


def main():
        era = select_tcg_era()
        print(era)
        if not era:
             print("Invalid option.")
             return 
        
        expansion_type = select_expansion_type()
        print(expansion_type)
        if not expansion_type:
             print("Invalid expansion type selected.")
             return
        
        product = select_product(expansion_type)
        print(product)
        if not product:
             print("Invalid product.")
     
        expansion = select_expansion(era, expansion_type)
        print(expansion)
        if not expansion:
             print("Invalid expansion")
        
        description = generate_product_description (era, expansion_type, product, expansion)
        if description:
          print("\nGenerated Product Description: ")
          print(description)


main()