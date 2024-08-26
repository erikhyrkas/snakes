import json
import csv
import os
from io import StringIO

import random

import yaml


# a bunch of convertions from json<->csv<->md table<->text


class TabularDataFormatter:
    def __init__(self, data):
        self.data = data  # Expecting a list of dictionaries

    def to_markdown(self):
        headers = self.data[0].keys()
        lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
        for row in self.data:
            lines.append("| " + " | ".join(str(row[key]) for key in headers) + " |")
        return "\n".join(lines)

    def to_csv(self):
        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=self.data[0].keys())
        writer.writeheader()
        writer.writerows(self.data)
        return output.getvalue()

    def to_json(self):
        return json.dumps(self.data, indent=4)

    def to_yaml(self):
        return yaml.safe_dump(self.data)

    def to_yml(self):
        return yaml.safe_dump(self.data)

    def to_plain_text(self):
        text = ""
        for row in self.data:
            text += " | ".join(f"{key}: {value}" for key, value in row.items()) + "\n"
        return text


class PersonDataGenerator:
    def __init__(self, names_file):
        self.names = self.load_names(names_file)
        self.cities = [
            "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
            "San Antonio", "San Diego", "Dallas", "San Jose", "Austin",
            "Jacksonville", "Fort Worth", "Columbus", "Charlotte", "San Francisco",
            "Indianapolis", "Seattle", "Denver", "Washington", "Boston",
            "El Paso", "Nashville", "Detroit", "Oklahoma City", "Portland",
            "Las Vegas", "Memphis", "Louisville", "Baltimore", "Milwaukee"
        ]
        self.ages = list(range(18, 70))
        self.income = list(range(20000, 500000, 5000))
        self.birth_month = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                            "October", "November", "December"]

    def load_names(self, names_file):
        with open(names_file, 'r') as file:
            names = [line.strip() for line in file.readlines()]
        return names

    def generate(self, num_records):
        data = []
        for _ in range(num_records):
            record = {
                "Name": random.choice(self.names),
                "Age": random.choice(self.ages),
                "Birth Month": random.choice(self.birth_month),
                "City": random.choice(self.cities),
                "Income": random.choice(self.income),
            }
            data.append(record)
        return data


class ProductInventoryDataGenerator:
    def __init__(self):
        self.product_names = [
            "Widget", "Gadget", "Doohickey", "Thingamajig", "Whatchamacallit",
            "Gizmo", "Contraption", "Device", "Instrument", "Apparatus"
        ]
        self.skus = [f"SKU-{i:04d}" for i in range(1000, 1100)]
        self.categories = ["Electronics", "Toys", "Household", "Sports", "Automotive"]
        self.suppliers = ["ACME Corp", "Globex", "Umbrella Corp", "Wayne Enterprises", "Wonka Industries"]

    def generate_price(self):
        return round(random.uniform(5.99, 499.99), 2)

    def generate_stock_quantity(self):
        return random.randint(0, 500)

    def generate(self, num_records):
        data = []
        for _ in range(num_records):
            record = {
                "Product Name": random.choice(self.product_names),
                "SKU": random.choice(self.skus),
                "Price": self.generate_price(),
                "Stock Quantity": self.generate_stock_quantity(),
                "Category": random.choice(self.categories),
                "Supplier Name": random.choice(self.suppliers),
            }
            data.append(record)
        return data


class RestaurantDataGenerator:
    def __init__(self):
        self.restaurant_names = [
            "The Golden Spoon", "Pasta Palace", "Burger Haven", "Sushi World", "Taco Town",
            "Pizza Planet", "The Steakhouse", "Vegan Delight", "Curry Corner", "BBQ Barn"
        ]
        self.cuisines = ["Italian", "American", "Japanese", "Mexican", "Indian", "Chinese", "French", "Mediterranean"]
        self.locations = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "San Francisco", "Seattle",
                          "Miami"]
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


class WeatherDataGenerator:
    def __init__(self):
        self.locations = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Miami", "Denver", "Seattle"]
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


class FinancialDataGenerator:
    def __init__(self):
        self.companies = [
            "TechCorp", "HealthPlus", "FinanceWorks", "EcoEnergy", "RetailHub",
            "GlobalTrade", "AeroSpace", "AutoDrive", "BioPharm", "Foodies"
        ]
        self.sectors = ["Technology", "Healthcare", "Finance", "Energy", "Retail", "Aerospace", "Automotive", "Biotech"]
        self.market_caps = ["Small Cap", "Mid Cap", "Large Cap", "Mega Cap"]
        self.stock_prices = [round(random.uniform(10.0, 1000.0), 2) for _ in range(100)]
        self.annual_revenues = [round(random.uniform(50.0, 500.0), 2) for _ in range(100)]  # In billions
        self.quarters = ["Q1", "Q2", "Q3", "Q4"]

    def generate(self, num_records):
        data = []
        for _ in range(num_records):
            record = {
                "Company": random.choice(self.companies),
                "Sector": random.choice(self.sectors),
                "Market Cap": random.choice(self.market_caps),
                "Stock Price": random.choice(self.stock_prices),
                "Annual Revenue (B)": random.choice(self.annual_revenues),
                "Quarter": random.choice(self.quarters),
            }
            data.append(record)
        return data


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


class DatabaseStatsGenerator:
    def __init__(self):
        self.database_names = [
            "UserDB", "InventoryDB", "SalesDB", "LogsDB", "MetricsDB",
            "ProductsDB", "AnalyticsDB", "SessionsDB", "OrdersDB", "ProfilesDB"
        ]
        self.queries_per_second = [round(random.uniform(50.0, 5000.0), 2) for _ in range(100)]
        self.cache_hit_ratios = [round(random.uniform(70.0, 99.9), 2) for _ in range(100)]  # Percentage
        self.connections = [random.randint(10, 500) for _ in range(100)]
        self.latencies = [round(random.uniform(1.0, 100.0), 2) for _ in range(100)]  # Milliseconds

    def generate(self, num_records):
        data = []
        for _ in range(num_records):
            record = {
                "Database Name": random.choice(self.database_names),
                "Queries per Second": random.choice(self.queries_per_second),
                "Cache Hit Ratio (%)": random.choice(self.cache_hit_ratios),
                "Connection Count": random.choice(self.connections),
                "Average Latency (ms)": random.choice(self.latencies),
                "Timestamp": f"{random.randint(2021, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d} "
                             f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
            }
            data.append(record)
        return data


class IoTDataGenerator:
    def __init__(self):
        self.device_ids = [f"device-{i:04d}" for i in range(1, 101)]
        self.device_types = ["Temperature Sensor", "Humidity Sensor", "Motion Detector", "Light Sensor",
                             "Pressure Sensor"]
        self.locations = ["Living Room", "Bedroom", "Kitchen", "Garage", "Office", "Garden", "Hallway", "Bathroom"]
        self.battery_levels = [round(random.uniform(10.0, 100.0), 1) for _ in range(100)]
        self.reading_values = [round(random.uniform(-40.0, 85.0), 2) for _ in range(100)]  # Varies by device type

    def generate(self, num_records):
        data = []
        for _ in range(num_records):
            record = {
                "Device ID": random.choice(self.device_ids),
                "Device Type": random.choice(self.device_types),
                "Location": random.choice(self.locations),
                "Battery Level (%)": random.choice(self.battery_levels),
                "Reading Value": random.choice(self.reading_values),
                "Timestamp": f"{random.randint(2021, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d} "
                             f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
            }
            data.append(record)
        return data


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


class StockMarketHistoryGenerator:
    def __init__(self):
        self.companies = [
            "TechnoCorp", "HealthGen", "GreenEnergy", "RetailWorld", "FinanceTrust",
            "BioLife", "AutoMotive", "AeroSystems", "FoodChain", "MediaGroup"
        ]
        self.price_range = [round(random.uniform(10.0, 1500.0), 2) for _ in range(100)]
        self.volumes = [random.randint(100000, 10000000) for _ in range(100)]

    def generate(self, num_records):
        data = []
        for _ in range(num_records):
            open_price = random.choice(self.price_range)
            close_price = random.choice(self.price_range)
            high_price = max(open_price, close_price, random.choice(self.price_range))
            low_price = min(open_price, close_price, random.choice(self.price_range))
            record = {
                "Company": random.choice(self.companies),
                "Date": f"{random.randint(2010, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
                "Open Price": open_price,
                "Close Price": close_price,
                "High Price": high_price,
                "Low Price": low_price,
                "Volume": random.choice(self.volumes),
            }
            data.append(record)
        return data


class PromptGenerator:
    def __init__(self, names_file):
        self.names_file = names_file
        self.generators = [
            self.create_person_generator,
            self.create_product_inventory_generator,
            self.create_restaurant_data_generator,
            self.create_financial_data_generator,
            self.create_weather_data_generator,
            self.create_book_collection_generator,
            self.create_movie_collection_generator,
            self.create_iot_data_generator,
            self.create_database_stats_generator,
            self.create_stock_market_history_generator,
            self.create_road_trip_history_generator
        ]

    def create_person_generator(self):
        return PersonDataGenerator(self.names_file)

    def create_product_inventory_generator(self):
        return ProductInventoryDataGenerator()

    def create_restaurant_data_generator(self):
        return RestaurantDataGenerator()

    def create_financial_data_generator(self):
        return FinancialDataGenerator()

    def create_weather_data_generator(self):
        return WeatherDataGenerator()

    def create_book_collection_generator(self):
        return BookCollectionDataGenerator()

    def create_movie_collection_generator(self):
        return MovieCollectionDataGenerator()

    def create_iot_data_generator(self):
        return IoTDataGenerator()

    def create_database_stats_generator(self):
        return DatabaseStatsGenerator()

    def create_stock_market_history_generator(self):
        return StockMarketHistoryGenerator()

    def create_road_trip_history_generator(self):
        return RoadTripHistoryGenerator()

    def remove_random_columns(self, data):
        # Get the list of keys (column names)
        keys = list(data[0].keys())
        # Determine how many columns to remove (0 to 3)
        num_columns_to_remove = random.randint(0, min(3, len(keys)))
        if num_columns_to_remove == 0:
            return data
        # Randomly select columns to remove
        columns_to_remove = random.sample(keys, num_columns_to_remove)
        # Remove the selected columns from each record in the data
        for record in data:
            for column in columns_to_remove:
                record.pop(column)
        return data

    def generate_prompt_and_response(self):
        # Randomly select a data generator and generate the data
        generator = random.choice(self.generators)()
        data = generator.generate(random.randint(3, 10))

        # Randomly remove 0 to 3 columns from the data
        data = self.remove_random_columns(data)

        formatter = TabularDataFormatter(data)
        formats = ['json', 'csv', 'markdown', 'plain text', 'yaml']
        from_format = random.choice(formats)
        to_format = random.choice([fmt for fmt in formats if fmt != from_format])

        if from_format == 'yaml' and random.choice([True, False]):
            from_format = 'yml'
        if to_format == 'yaml' and random.choice([True, False]):
            to_format = 'yml'

        # Get data in the 'from' format
        data_in_format = getattr(formatter, f'to_{from_format.replace(" ", "_")}')()

        # Convert the data to the 'to' format
        response_data = getattr(formatter, f'to_{to_format.replace(" ", "_")}')()

        # Wrap the response in <start><end> tags
        response = f"<start>\n{response_data.strip()}\n<end>"

        if random.choice([True, False]):
            if random.choice([True, False]):
                to_format = to_format.upper()
            else:
                to_format = to_format.capitalize()
        if random.choice([True, False]):
            if random.choice([True, False]):
                from_format = from_format.upper()
            else:
                from_format = from_format.capitalize()

        # Generate the prompt with variations
        prompts = [
            f"Convert this {from_format} to {to_format}:\n{data_in_format}",
            f"Please transform the following {from_format} data into {to_format}:\n{data_in_format}",
            f"Here's some {from_format} data, can you convert it to {to_format}?\n{data_in_format}",
            f"Can you change this {from_format} into {to_format}?\n{data_in_format}",
            f"Transform this {from_format} structure to a {to_format} format:\n{data_in_format}",
        ]

        prompt = random.choice(prompts)

        return prompt, response


def main():
    base_file_name = 'format-convertion'
    prompt_generator = PromptGenerator('./names.txt')
    for file_count in range(20):
        output_file = f'./training_data/{base_file_name}-{file_count}.md'
        if os.path.exists(output_file):
            continue
        with open(output_file, 'w', encoding="utf-8") as file:
            for _ in range(200):
                prompt, response = prompt_generator.generate_prompt_and_response()
                record = f"{prompt}{response}"
                record = record.replace("\n\n", "\n")
                record = record.replace("\r", "")
                print(record)
                print('-' * 80)
                file.write(record)
                file.flush()


if __name__ == '__main__':
    main()
