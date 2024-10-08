import random


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