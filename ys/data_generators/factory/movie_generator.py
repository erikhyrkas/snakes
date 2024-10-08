import random


class MovieCollectionDataGenerator:
    def __init__(self):
        self.titles = [
            "The Endless Horizon", "Starbound Odyssey", "Mystery of the Depths", "The Final Voyage",
            "Escape from Earth",
            "Dreamwalker", "Beyond the Veil", "The Great Expedition", "Edge of Infinity", "Rise of the Titans"
        ]
        self.directors = [
            "Aria Ravenwood", "Drake Nightshade", "Zara Stormrider", "Talon Blackthorn", "Mara Moonshadow",
            "Rylan Frostblade", "Selene Darkwhisper", "Cade Firebrand", "Lira Silverleaf", "Orin Shadowalker"
        ]
        self.genres = ["Action", "Adventure", "Drama", "Comedy", "Sci-Fi", "Fantasy", "Horror", "Thriller"]
        self.release_years = [random.randint(1970, 2023) for _ in range(100)]
        self.box_office = [round(random.uniform(10.0, 1000.0), 2) for _ in range(100)]  # In millions

    def generate(self, num_records):
        data = []
        for _ in range(num_records):
            record = {
                "Title": random.choice(self.titles),
                "Director": random.choice(self.directors),
                "Genre": random.choice(self.genres),
                "Release Year": random.choice(self.release_years),
                "Box Office Earnings (M)": random.choice(self.box_office),
            }
            data.append(record)
        return data
