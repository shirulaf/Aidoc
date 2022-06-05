

class CountryStatInterface:

    def country_daily_new_cases(self, country_name, limit=14):
        # for a given country name print a list of the last 14 days and the number of daily new cases in that country
        pass

    def total_cases_for_every_country(self, limit=10):
        # For the 10 countries with the largest number of total cases, shows the total number of cases for each country since the epidemic started
        pass

    def country_naive_possibility_to_covid(self, country_name):
        # A naive measurement to estimate the chance for getting infected with Covid19 in a given country in the last
        # days
        # The used naive-measurement:
        # population_density(country) * new_cases_smoothed_per_million(country) / MAX(population_density)
        # the bigger the result the bigger are the chance to get infected
        pass