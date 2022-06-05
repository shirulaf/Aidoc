import os
import traceback

from .data_preparation_interface import DataPreparationInterface
from src.DB.db_source import DBSource

from conf import CONFIG
import logging
import csv
import requests


class DataPreparation(DataPreparationInterface):
    data_fields = CONFIG["dataset"]["fields"]
    local_data_path = CONFIG["dataset"]["local_data_file"]

    queries = DBSource().queries

    def prepare_data(self):
        try:
            data_reader = self.get_data()

            org_data = self.organize_data(data_reader, self.data_fields)
            self.load_data_to_db(org_data)
            os.remove(self.local_data_path)  # Remove local copy to avoid redundant storage-cost

            print("Data was loaded successfully")
        except Exception as e:
            print(e, traceback.format_exc())

    def get_data(self) -> csv.DictReader:
        logging.info("Retrieving data from source")
        try:
            url = CONFIG["dataset"]["url_csv"]
            r = requests.get(url, allow_redirects=True)
            open(self.local_data_path, 'wb').write(r.content)  # No need to delete the file when done
            # since its being truncate
            data_reader = csv.DictReader(open(CONFIG["dataset"]["local_data_file"]))
            logging.info(f"Data retrieved successfully and was written to {CONFIG['dataset']['local_data_file']}")

            return data_reader

        except Exception as e:
            logging.error(f"Failed retrieving from source, {e}")
            raise Exception(f"Failed retrieving from source, {e}")

    def organize_data(self, data_reader: csv.DictReader, data_fields: list):
        return self.queries.organize_data(data_reader, data_fields)

    def load_data_to_db(self, data):
        self.queries.load_data_to_db(data)


import sys

if __name__ == '__main__':
    globals()
    DataPreparation()[sys.argv[1]](sys.argv[2])
