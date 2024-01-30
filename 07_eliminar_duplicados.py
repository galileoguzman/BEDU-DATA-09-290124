import pandas as pd

data = {'A': [1, 2, 2, 3, 4], 'B': ['x', 'y', 'y', 'z', 'z']}
dataframe = pd.DataFrame(data)

print(dataframe.head())
print("---------------")

print(dataframe.duplicated())
print("---------------")

duplicates = dataframe[dataframe.duplicated()]
print(duplicates)
print("---------------")

no_duplicates = dataframe.drop_duplicates()
print(no_duplicates)