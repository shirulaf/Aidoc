from conf import CONFIG

import pymongo


class MongoDbConnection:
    mongo_config = CONFIG["db"]["config"]["mongo"]

    def __init__(self):
        mongo_client = pymongo.MongoClient(self.mongo_config["connection_string"])  # NOQA

        self.db_instance = mongo_client[self.mongo_config["db_name"]]
