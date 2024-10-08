import random


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
