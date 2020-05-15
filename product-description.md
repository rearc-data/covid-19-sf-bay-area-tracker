# San Francisco Bay Area COVID-19 Tracker

The source code outlining how this product gathers, transforms, revises and publishes its datasets is available at [https://github.com/rearc-data/covid-19-sf-bay-area-tracker](https://github.com/rearc-data/covid-19-sf-bay-area-tracker).

## Main Overview
Daily data of the total number of COVID-19 cases in the six San Francisco Bay Area counties under "shelter in place" orders.

IMPORTANT: confirmed cases is an unreliable metric right now due to significant issues in getting tests, and delays in processing and receiving test results. Tests appear to be reserved for healthcare workers and the very sick. Different healthcare systems also have different testing abilities and turnaround times. Death rates would be a more reliable (if morbid) measure, but lag reality by 2-6 weeks. Hospitalizations would be good but this data is not currently provided by most counties. Please draw any conclusions from this data carefully.

#### Data Source
The dataset included with this resource features the following columns:

`day,date,notes,santa_clara_cases, san_francisco_cases, san_mateo_cases, alameda_cases, contra_costa_cases, marin_cases, sonoma_cases, solano_cases, city_of_berkeley, napa_cases, sf_bay_area_total_cases, daily_growth_rate_in_cases, doubling_time_of_latest_daily_growth, compounding_average_daily_growth_rate_in_cases, doubling_time_of_compoounding_average_(days), last_7_days_growth_rate_in_total_cases, doubling_time_based_on_last_7_days_of_growth, new_cases_in_sf_bay_area, growth_factor, santa_clara_deaths, san_francisco_deaths, san_mateo_deaths, alameda_deaths, contra_costa_deaths, marin_deaths, sonoma_deaths, solano_deaths, city_of_berkeley_deaths, napa_deaths, days_above_10_deaths, total_fatalities_in_sf_bay_area, new_fatalities_in_the_bay_area, growth_in_fatalities_(since_10), last_7_days_growth_rate_in_fatalities, compound_growth_rate, case_fatality_rate, hospitalizations_-_santa_clara, hospitalizations_in_marin, hospitalizations_-_sonoma, hospitalizations_in_solano_(cumulative), confirmed_cases_per_100k_residents_in_santa_clara, confirmed_cases_per_100k_residents_in_san_francisco, confirmed_cases_per_100k_residents_in_san_mateo_county, confirmed_cases_per_100k_residents_in_alameda, confirmed_cases_per_100k_residents_in_contra_costa, confirmed_cases_per_100k_residents_in_marin, confirmed_cases_per_100k_residents_in_sonoma, confirmed_cases_per_100k_residents_in_solana, confirmed_cases_per_100k_residents_in_napa, confirmed_cases_per_100k_residents_in_sf_bay_area, tests_in_santa_clara, tests_in_contra_costa_county, tests_in_marin, test_in_sonoma_county, tests_in_napa_county, test_positivity_rate_in_marin, test_positivity_rate_in_sonoma_county, test_positivity_rate_in_napa_county, santa_clara_new_cases, san_francisco_new_cases, san_mateo_new_cases, alameda_new_cases, contra_costa_new_cases, marin_new_cases, sonoma_new_cases, solano_new_cases, city_of_berkeley_new_cases, napa_new_cases, tests_in_contra_costa_county`

## More Information
- Source: [SF Bay Area COVID-19 Tracker](https://docs.google.com/spreadsheets/d/1l0xahMRiLlom-7R1bHh1nWWU4DdOafShL3-8scceC3o/edit?pli=1#gid=1354523822)         
- [Dataset License](https://docs.google.com/spreadsheets/d/1l0xahMRiLlom-7R1bHh1nWWU4DdOafShL3-8scceC3o/edit?pli=1#gid=1354523822)  
- Frequency: Daily
- Format: CSV

## Contact Details
- If you find any issues with or have enhancement ideas for this product, open up a GitHub [issue](https://github.com/rearc-data/covid-19-sf-bay-area-tracker/issues) and we will gladly take a look at it. Better yet, submit a pull request. Any contributions you make are greatly appreciated :heart:.
- If you are looking for specific open datasets currently not available on ADX, please submit a request on our project board [here](https://github.com/rearc-data/covid-datasets-aws-data-exchange/projects/1).
- If you have questions about the source data, please contact the author [Andrew Roberts](https://twitter.com/andrew_roberts/).
- If you have any other questions or feedback, send us an email at data@rearc.io.

## About Rearc
Rearc is a cloud, software and services company. We believe that empowering engineers drives innovation. Cloud-native architectures, modern software and data practices, and the ability to safely experiment can enable engineers to realize their full potential. We have partnered with several enterprises and startups to help them achieve agility. Our approach is simple — empower engineers with the best tools possible to make an impact within their industry.
