import random

from ys.data_generators.util.item_loader import file_to_list, tsv_to_list_of_lists


class PersonDataGenerator:
    def __init__(self, names_file: str, cities_file: str):
        self.names = file_to_list(names_file)
        city_states = tsv_to_list_of_lists(cities_file)

        self.cities = []
        self.states = []
        for record in city_states:
            self.cities.append(record[0])
            self.states.append(record[1])
        self.ages = list(range(18, 70))
        self.income = list(range(20000, 500000, 5000))
        self.birth_month = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                            "October", "November", "December"]

    def generate(self, num_records):
        data = []
        for _ in range(num_records):
            record = {
                "Name": random.choice(self.names),
                "Age": random.choice(self.ages),
                "Birth Month": random.choice(self.birth_month),
                "City": random.choice(self.cities),
                "State": random.choice(self.states),
                "Income": random.choice(self.income),
            }
            data.append(record)
        return data