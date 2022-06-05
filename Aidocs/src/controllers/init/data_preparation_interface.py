import csv


class DataPreparationInterface:

    def organize_data(self,data_reader: csv.DictReader, data_fields: list):
        pass

    def load_data_to_db(self, data):
        pass
