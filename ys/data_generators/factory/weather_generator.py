import random

from ys.data_generators.util.item_loader import tsv_to_list_of_lists


class WeatherDataGenerator:
    def __init__(self, cities_file: str):
        city_states = tsv_to_list_of_lists(cities_file)
        self.locations = []
        for record in city_states:
            self.locations.append(f"{record[0]}, {record[1]}")
        self.conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Snowy", "Windy", "Foggy"]
        self.temperatures = [round(random.uniform(-10.0, 40.0), 1) for _ in range(100)]  # In Celsius
        self.humidity_levels = [random.randint(20, 100) for _ in range(100)]  # Percentage
        self.wind_speeds = [round(random.uniform(0.0, 30.0), 1) for _ in range(100)]  # In km/h
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def generate(self, num_records):
        data = []
        for _ in range(num_records):
            record = {
                "Location": random.choice(self.locations),
                "Condition": random.choice(self.conditions),
                "Temperature (C)": random.choice(self.temperatures),
                "Humidity (%)": random.choice(self.humidity_levels),
                "Wind Speed (km/h)": random.choice(self.wind_speeds),
                "Day": random.choice(self.days),
            }
            data.append(record)
        return data
