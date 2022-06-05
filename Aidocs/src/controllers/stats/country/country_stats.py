import logging

import matplotlib.pyplot as plt

from datetime import datetime

from src.DB.db_source import DBSource
from .country_stats_interface import CountryStatInterface
from src.utils.pretty_print import *


class CountryStats(CountryStatInterface):
    queries = DBSource().queries

    @pretty_print_list
    def country_daily_new_cases(self, country_name, limit=14) -> list:
        # for a given country name print a list of the last 14 days and the number of daily new cases in that country
        stat = self.queries.country_daily_new_cases(country_name, limit)

        # TODO - refactor - make generic/extract
        x_axis = []
        y_axis = []
        for item in stat:
            x_axis.append(item["date"])
            y_axis.append(item["new_cases"] if item["new_cases"] != '' else None)

        plt.figure(figsize=(20, 10))
        plt.plot(x_axis, y_axis)
        fig_path = f"stats/country_daily_new_cases__{country_name}_{datetime.now()}.pdf"
        plt.savefig(fig_path)
        print(f"The result plot can be found in {fig_path}")

        return stat

    @pretty_print_list
    def total_cases_for_every_country(self, limit=10) -> list:
        # For the 10 countries with the largest number of total cases, shows the total number of cases for each country
        # since the epidemic started
        print("Getting stats: total_cases_for_every_country ")
        stat = self.queries.total_cases_for_every_country(limit)

        # TODO - refactor - make generic/extract
        x_axis = []
        y_axis = []
        for item in stat:
            x_axis.append(item["location"])
            y_axis.append(item["total_cases"] if item["total_cases"] != '' else None)

        plt.figure(figsize=(20, 10))
        plt.bar(x_axis, y_axis)
        fig_path=f"stats/total_cases_for_every_country__{datetime.now()}.pdf"
        plt.savefig(fig_path)
        print(f"The result plot can be found in {fig_path}")
        return stat

    @pretty_print_value
    def country_naive_possibility_to_covid(self, country_name):
        new_cases_smoothed_per_million, population_density, max_population_density = \
            self.queries.country_naive_possibility_to_covid(country_name)

        try:
            possib = new_cases_smoothed_per_million * population_density / max_population_density
        except Exception as e:
            logging.error(e)
            possib = f"Couldn't calc possibility - new_cases_smoothed_per_million * population_density / " \
                     f"max_population_density= ({new_cases_smoothed_per_million}*{population_density}/" \
                     f"{max_population_density})"

        return possib
