import pandas as pd
import numpy as np

# read data from csv file
data=pd.read_csv('data.csv')

# dataframe
df=pd.DataFrame(data)

print(df)

# retrieving row
print(data.iloc[1])
