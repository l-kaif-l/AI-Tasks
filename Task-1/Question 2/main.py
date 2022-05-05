import pandas as pd
data = pd.read_csv("Q2-Dataset.csv")
print(data)
data.fillna(0)