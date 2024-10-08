import random


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
