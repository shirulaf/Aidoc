1. Run `pip install -r ./requirements.txt` to install required libraries

<h4>
This service is serverless, it is currently works only on Dev env with local Docker image of Mongodb and 
mongo-express</h4>

2. Uploading the DB services

    1. Uploading the db service: make sure you have docker-compose installed, and run:
        1. `make db_up`
        3. Make sure the services are running with `docker ps` (Expecting 'mongo', 'mongo-express')

    2. Preparing the DB
        * Run: `make prepare_data`
        * Now the db can be seen on mongo-express : [http://localhost:8081/db/covid/stat](http://localhost:8081/db/covid/stat)

    3. When done - Shutting down the service run: `make db_down`

3. Running statistics functions:
    - The functions can be executed from the command line using a Makefile

    - The available statistics and their commands are:
        1. **country_daily_new_cases**
            * For a given country name print a list of the last 14 days and the number of daily new cases in that
              country
            * Run the function with: `make country=<country_name> country_daily_new_cases`, when country_name is the
              country name you would like to get the stat. for. **country_name - should be capitalized (e.g. Israel)**
        2. **total_cases_for_every_country**
            * For the 10 countries with the largest number of total cases, shows the total number of cases for each
              country since the epidemic started
            * Run function with: `make total_cases_for_every_country`
        3. **covid-infec-measurement** -
            * My added stat. - say one wants to fly abroad while taking into consideration the chance of being infected
            * with Covid-19, for that I have calculated a naive measurement as follows:
              The current possibility-rate for getting infected with Covid-19 for a given country:

              `new_cases_smoothed_per_million(country) * population_density(country) / MAX(population_density)`

            * Run function with: `make country=<country_name> country_naive_possibility_to_covid`, when country_name is the
              country name you would like to get the stat. for. **country_name - should be capitalized (e.g. Israel)**
            * The bigger the measurement the bigger the chances, one can compare the (naive) risk between different
              countries.
              
        - Relevant plots will be saved into the `stat/` directory
