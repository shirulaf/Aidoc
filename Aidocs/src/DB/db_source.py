from conf import CONFIG
from .Mongodb.queries import MongoQueries


class DBSource:
    config_mapper = {
        "mongo": MongoQueries
    }

    def __init__(self):
        self.queries = self.config_mapper[CONFIG["db"]["type"]]()
