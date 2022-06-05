import traceback

from .connection import MongoDbConnection
from conf import CONFIG
from src.utils.convert_string_to_type import convert_string_to_type

import pymongo
import csv
import logging
from operator import itemgetter

# INTERFACES
from src.controllers.init.data_preparation_interface import DataPreparationInterface
from src.controllers.stats.country.country_stats_interface import CountryStatInterface


class MongoQueries(DataPreparationInterface, CountryStatInterface):
    mongo_config = CONFIG["db"]["config"]["mongo"]
    collection_inst = MongoDbConnection().db_instance[mongo_config["dataset"]["collection_name"]]

    def organize_data(self, data_reader: csv.DictReader, data_fields: list) -> list[dict]:
        logging.info("Organizing data to collection")
        collection_data: list = []
        for row in data_reader:
            document = {}
            for field in data_fields:
                document[field["name"]] = \
                    row[field["name"]] if field["type"] == "str" else \
                        convert_string_to_type(row[field["name"]], field["type"])

            collection_data.append(document)

        return collection_data

    def load_data_to_db(self, data: list[dict]):
        logging.info("Loading data into DB")

        try:
            db_inst = MongoDbConnection().db_instance
            temp_coll = db_inst.temp
            temp_coll.insert_many(data)
            temp_coll.rename(self.mongo_config["dataset"]["collection_name"], dropTarget=True)

            countries_stat_coll = db_inst.stat
            countries_stat_coll.create_index(self.mongo_config["dataset"]["index"])

            temp_coll.drop()

            logging.info("Data was loaded to db")

        except Exception as e:
            print(e, traceback.print_exc())

    def country_daily_new_cases(self, country_name, limit=14):
        # for a given country name print a list of the last 14 days and the number of daily new cases in that country
        last_cases = self.collection_inst. \
            find({"location": country_name}, {"new_cases": 1, "date": 1, "_id": 0}) \
            .sort("date", pymongo.DESCENDING) \
            .limit(limit)

        return list(last_cases)

    def total_cases_for_every_country(self, limit=10):
        # For the 10 countries with the largest number of total cases, shows the total number of cases for each
        # country since the epidemic started
        newest_date = self.collection_inst \
            .find({}, {"date": 1, "_id": 0}) \
            .sort("date", pymongo.DESCENDING) \
            .limit(1)[0]["date"]

        total_cases = self.collection_inst \
            .find({"date": newest_date, "$expr": {"$eq": [{"$strLenCP": "$iso_code"}, 3]}},
                  {"location": 1, "total_cases": 1, "_id": 0}) \
            .sort("total_cases", pymongo.DESCENDING) \
            .limit(limit)

        return list(total_cases)

    def country_naive_possibility_to_covid(self, country_name):
        logging.info("Getting data from collection for country_naive_possibility_to_covid")

        try:
            country_data = list(self.collection_inst. \
                                find({"location": country_name, "population_density": {"$ne": ''}, "new_cases_smoothed_per_million": {"$ne": ''}},
                                     {"new_cases_smoothed_per_million": 1, "population_density": 1, "_id": 0})
                                .sort("date", pymongo.DESCENDING).limit(1))[0]

            max_population_density = list(self.collection_inst. \
                                          find({"population_density": {"$ne": ''}}, {"population_density": 1,
                                                                                       "_id": 0}) \
                                          .sort("population_density", pymongo.DESCENDING) \
                                          .limit(1))[0]["population_density"]

            return country_data["new_cases_smoothed_per_million"], \
                   country_data["population_density"], max_population_density

        except Exception as e:
            print(e, traceback.print_exc())
