db_up:
	docker-compose -f db/mongo/docker-compose.dev.yml build
	docker-compose -f db/mongo/docker-compose.dev.yml up -d

db_down:
	docker-compose -f db/mongo/docker-compose.dev.yml down

country_daily_new_cases:
	python3 -c 'from src.controllers.stats.country.country_stats import CountryStats; CountryStats().country_daily_new_cases("$(country)")'

total_cases_for_every_country:
	python3 -c 'from src.controllers.stats.country.country_stats import CountryStats; CountryStats().total_cases_for_every_country()'

country_naive_possibility_to_covid:
	python3 -c 'from src.controllers.stats.country.country_stats import CountryStats; CountryStats().country_naive_possibility_to_covid("$(country)")'

prepare_data:
	echo "RUNNING prepare_data"
	python3 -c 'from src.controllers.init.data_preparation import DataPreparation; DataPreparation().prepare_data()'