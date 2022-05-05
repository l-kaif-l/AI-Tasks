import pandas as pd
import numpy as np

print("Retrieving data from the .csv File:\n The data is,")
data = pd.read_csv("Q4-Dataset.csv")
print(data)

print("\nCreating array using Numpy: \n")
array_data = np.array(data)
print(array_data)

print("\nSorting w.r.t Ratings:\n")
array_data.sort(axis=0)
print(array_data)
