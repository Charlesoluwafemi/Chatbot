# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random


class Property:
    def __init__(self, location, property_type, price):
        self.location = location
        self.property_type = property_type
        self.price = price


property_types = ["Apartment", "House", "Condo", "Townhouse"]

locations = ["Downtown", "Suburb", "Waterfront", "Countryside"]


def generate_property(location, property_type, budget):
    price_range = {
        "Apartment": (100000, 300000),
        "House": (200000, 700000),
        "Condo": (150000, 400000),
        "Townhouse": (180000, 450000)
    }
    min_price, max_price = price_range[property_type]
    if budget < min_price:
        return None
    price = min(budget, max_price)
    return Property(location, property_type, price)


def main():
    print("Hello! I'm your virtual real estate agent.")
    print("Type 'quit' to exit.")

    while True:
        location = input("Where are you looking for properties? (Downtown, Suburb, Waterfront, Countryside): ")

        if location.lower() == 'quit':
            print("Goodbye! Have a great day!")
            break

        if location.capitalize() not in locations:
            print("Sorry, I don't have listings for that location.")
            continue

        property_type = input("What type of property are you interested in? (Apartment, House, Condo, Townhouse): ")

        if property_type.capitalize() not in property_types:
            print("Sorry, I don't have listings for that property type.")
            continue

        budget = int(input("What is your budget for the property? "))

        property_listing = generate_property(location.capitalize(), property_type.capitalize(), budget)

        if property_listing:
            print("\nHere's a property listing that matches your preferences:")
            print(f"Location: {property_listing.location}")
            print(f"Property Type: {property_listing.property_type}")
            print(f"Price: ${property_listing.price:,}")
        else:
            print("\nSorry, I couldn't find any listings that match your preferences within your budget.Our customer agent will attend to you shortly")


if __name__ == "__main__":
    main()
