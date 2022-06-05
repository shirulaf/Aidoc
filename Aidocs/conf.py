CONFIG = {
    "dataset": {
        "url_csv": "https://covid.ourworldindata.org/data/owid-covid-data.csv",
        "local_data_file": "data.csv",
        "fields": [{"name": "location", "type": "str"},
                   {"name": "date", "type": "str"},
                   {"name": "total_cases", "type": "int"},
                   {"name": "new_cases", "type": "int"},
                   {"name": "iso_code", "type": "str"},
                   {"name": "population_density", "type": "float"},
                   {"name": "new_cases_smoothed_per_million", "type": "float"}],

    },
    "db": {
        "type": "mongo",
        "config": {
            "mongo": {
                "connection_string": "mongodb://devroot:devroot@localhost:27017",
                "db_name": "covid",
                "dataset": {

                    "index": [("date" ,-1)],
                    "collection_name": "stat"
                },
            }
        }

    }
}
