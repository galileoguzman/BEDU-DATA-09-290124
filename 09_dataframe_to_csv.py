import pandas as pd

# Objeto a convertir
dataframe = pd.DataFrame({
    'Columna1': [1, 2, 3],
    'Columna2': ['A', 'B', 'C'],
    'Columna3': [True, False, True]
})

filename = 'datasets/new_csv_from_pd.csv'

print(dataframe.head())

# Conversion
dataframe.to_csv(filename, index=False)

print('XD')