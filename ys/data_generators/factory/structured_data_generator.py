import random

from ys.data_generators.factory.book_generator import BookCollectionDataGenerator
from ys.data_generators.factory.database_state_generator import DatabaseStatsGenerator
from ys.data_generators.factory.financial_generator import FinancialDataGenerator
from ys.data_generators.factory.iot_data_generator import IoTDataGenerator
from ys.data_generators.factory.movie_generator import MovieCollectionDataGenerator
from ys.data_generators.factory.person_generator import PersonDataGenerator
from ys.data_generators.factory.product_inventory_generator import ProductInventoryDataGenerator
from ys.data_generators.factory.restraurant_generator import RestaurantDataGenerator
from ys.data_generators.factory.road_trip_generator import RoadTripHistoryGenerator
from ys.data_generators.factory.stock_market_generator import StockMarketHistoryGenerator
from ys.data_generators.factory.weather_generator import WeatherDataGenerator


class StructuredDataGenerator:
    def __init__(self, names_file: str, cities_file: str):
        self.names_file = names_file
        self.cities_file = cities_file
        self.generators = [
            self._create_person_generator,
            self._create_product_inventory_generator,
            self._create_restaurant_data_generator,
            self._create_financial_data_generator,
            self._create_weather_data_generator,
            self._create_book_collection_generator,
            self._create_movie_collection_generator,
            self._create_iot_data_generator,
            self._create_database_stats_generator,
            self._create_stock_market_history_generator,
            self._create_road_trip_history_generator
        ]

    def _create_person_generator(self):
        return PersonDataGenerator(self.names_file, self.cities_file)

    def _create_product_inventory_generator(self):
        return ProductInventoryDataGenerator()

    def _create_restaurant_data_generator(self):
        return RestaurantDataGenerator(self.cities_file)

    def _create_financial_data_generator(self):
        return FinancialDataGenerator()

    def _create_weather_data_generator(self):
        return WeatherDataGenerator(self.cities_file)

    def _create_book_collection_generator(self):
        return BookCollectionDataGenerator()

    def _create_movie_collection_generator(self):
        return MovieCollectionDataGenerator()

    def _create_iot_data_generator(self):
        return IoTDataGenerator()

    def _create_database_stats_generator(self):
        return DatabaseStatsGenerator()

    def _create_stock_market_history_generator(self):
        return StockMarketHistoryGenerator()

    def _create_road_trip_history_generator(self):
        return RoadTripHistoryGenerator()

    def _remove_random_columns(self, data):
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

    def generate_random_structured_data(self):
        # Randomly select a data generator and generate the data
        generator = random.choice(self.generators)()
        data = generator.generate(random.randint(3, 10))

        # Randomly remove 0 to 3 columns from the data
        data = self._remove_random_columns(data)
        return data
