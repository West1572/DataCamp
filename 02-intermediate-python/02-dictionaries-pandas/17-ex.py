# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
print(cars)
# Print out observation for Japan
print(cars.iloc[2])
print(cars.loc['JPN'])


# Print out observations for Australia and Egypt
print(cars.loc[['AUS','ED']])
print(cars.iloc[[1,6]])