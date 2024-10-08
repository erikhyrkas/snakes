import random


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