<h2>The main idea behind the architecture </h2>

- Using a serverless code
- Keeping the DB source generic with option to connect more DBs frameworks, as some statistics better be calculated in a
  specific DB type (i.e. Graph, SQL, etc. )
    - Dataset:
        - Defining in a configuration file which columns should be imported
            - When getting the csv dataset:
                - an approach of writing to the disk and then reading each row was taken for time and space performance
                  considerations (As opposed to using pandas.read_csv, and reading all data in_memory when the dataset
                  is getting larger every day)
                - Only the relevant columns are loaded to DB, according to the configuration file, to save space and
                  avoid redundant data
                - The local copy of the dataset is being deleted when data is loaded to the DB in order to avoid
                  redundant resources costs

<h2>Main modules</h2>

- conf.py - holds the application configuration
- `src/DB` :
    - Holds different DB usage/implementation
        - db_source: returns queries object according to the configuration
    - Each DB type should have 2 files:
        - connection.py - for connecting and returning a db connection instance
        - queries.py
            - Holds all the code queries, enforced by implementing all the existing logics interfaces
            - Each logic controller implements an interface, so in return the controllers calls the adequate function
              from the queries' module, when data retrieval is needed

- `controllers`
    - `init`:
        - Holds the logic of the data preparation
        - Contains the interface to be implemented by the Db module and the controller logic
    - `stats`:
        - `country`:
            - Holds all the country regarding statistics
            - Contains the interface to be implemented by the Db module and the controller logic
            - Results are written to the console, and plots are saved to the `stats/` directory, with the function name,
              params and the saving timestamp, for
              example: `country_daily_new_cases__Israel_2022-06-05 20:29:12.600955.pdf`
    