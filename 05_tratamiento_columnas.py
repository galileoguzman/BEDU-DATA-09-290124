import pandas as pd

ENCODING = 'ISO-8859-1'
dataframe = pd.read_csv('datasets/car_crashes.csv', encoding=ENCODING)

print(dataframe.head(1))

dataframe = dataframe.rename(columns={'Weekend?': 'fin_de_semana', 'Year': 'anio'})

print(dataframe.head(1))