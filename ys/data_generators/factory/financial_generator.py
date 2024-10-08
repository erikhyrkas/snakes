import random


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