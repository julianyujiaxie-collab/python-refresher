import my_utils

country = 'United States of America'
country_col = 0
fires_col = 3
file_name = 'Agrofood_co2_emission.csv'

fires = my_utils.get_column(file_name, country_col, country, fires_col)

print(fires)
