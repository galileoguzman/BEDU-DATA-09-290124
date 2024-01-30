import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}

dataframe = pd.DataFrame(data)
print(dataframe.head())

print("-------------------")

dataframe.columns = ['X', 'Y']
print(dataframe.head())