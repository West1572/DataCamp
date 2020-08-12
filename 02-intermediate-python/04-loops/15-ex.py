# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
#print(cars)
# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab +": " +str(row['cars_per_cap']))
    print(row['country'] + ": " +str(row['cars_per_cap']))