import random

from ys.data_generators.util.item_loader import tsv_to_list_of_lists


class RestaurantDataGenerator:
    def __init__(self, cities_file: str):
        self.restaurant_names = [
            "The Golden Spoon", "Pasta Palace", "Burger Haven", "Sushi World", "Taco Town",
            "Pizza Planet", "The Steakhouse", "Vegan Delight", "Curry Corner", "BBQ Barn"
        ]
        self.cuisines = ["Italian", "American", "Japanese", "Mexican", "Indian", "Chinese", "French", "Mediterranean"]
        city_states = tsv_to_list_of_lists(cities_file)

        self.locations = []
        for record in city_states:
            self.locations.append(f"{record[0]}, {record[1]}")
        self.rating = [1, 2, 3, 4, 5]
        self.price_range = ["$", "$$", "$$$", "$$$$", "$$$$$"]

    def generate(self, num_records):
        data = []
        for _ in range(num_records):
            record = {
                "Restaurant Name": random.choice(self.restaurant_names),
                "Cuisine": random.choice(self.cuisines),
                "Location": random.choice(self.locations),
                "Rating": random.choice(self.rating),
                "Price Range": random.choice(self.price_range),
            }
            data.append(record)
        return data