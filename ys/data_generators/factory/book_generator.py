import random


class BookCollectionDataGenerator:
    def __init__(self):
        self.titles = [
            "The Silent Grove", "Echoes of Eternity", "Whispers of the Abyss", "The Last Sky", "Shadows of Solitude",
            "A Journey Through Time", "The Forgotten World", "The Crystal Key", "Legends of the Rift",
            "Tales of the Brave"
        ]
        self.authors = [
            "Elara Moonshadow", "Galen Starfire", "Isla Windrider", "Thorne Ironwood", "Sylvia Nightshade",
            "Draven Blackthorn", "Luna Silverleaf", "Rowan Ashborne", "Kara Firebrand", "Orion Frostblade"
        ]
        self.genres = ["Fantasy", "Science Fiction", "Mystery", "Horror", "Historical", "Thriller", "Romance",
                       "Non-Fiction"]
        self.publication_years = [random.randint(1950, 2023) for _ in range(100)]
        self.ratings = [round(random.uniform(1.0, 5.0), 1) for _ in range(100)]

    def generate(self, num_records):
        data = []
        for _ in range(num_records):
            record = {
                "Title": random.choice(self.titles),
                "Author": random.choice(self.authors),
                "Genre": random.choice(self.genres),
                "Publication Year": random.choice(self.publication_years),
                "Rating": random.choice(self.ratings),
            }
            data.append(record)
        return data
