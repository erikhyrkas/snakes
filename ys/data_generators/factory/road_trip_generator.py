import random


class RoadTripHistoryGenerator:
    def __init__(self):
        self.trip_names = [
            "Coast to Coast", "Mountain Adventure", "Desert Drive", "Lakeside Retreat", "City Explorer",
            "Canyon Trek", "Forest Journey", "Valley Voyage", "Highway Odyssey", "Historic Route"
        ]
        self.locations = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Denver", "Miami",
                          "San Francisco"]
        self.distances = [round(random.uniform(50.0, 3000.0), 1) for _ in range(100)]  # In miles
        self.durations = [round(random.uniform(1.0, 72.0), 1) for _ in range(100)]  # In hours
        self.fuel_used = [round(random.uniform(5.0, 100.0), 1) for _ in range(100)]  # In gallons

    def generate(self, num_records):
        data = []
        for _ in range(num_records):
            start_location = random.choice(self.locations)
            end_location = random.choice([loc for loc in self.locations if loc != start_location])
            record = {
                "Trip Name": random.choice(self.trip_names),
                "Start Location": start_location,
                "End Location": end_location,
                "Distance (miles)": random.choice(self.distances),
                "Duration (hours)": random.choice(self.durations),
                "Fuel Used (gallons)": random.choice(self.fuel_used),
            }
            data.append(record)
        return data