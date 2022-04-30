import pandas as pd

# read csv file
DataFrame=pd.read_csv("Datasets/lifestyle.csv")
# print dataframe
print(DataFrame)
# print first 5 rows in dataframe
print(DataFrame.head(5))
# print datatypes of columns
print(DataFrame.dtypes)
# technical summary
print(f"technical summary:\n {DataFrame.info()}")

# excel spread sheet
q  
'''
functions:
    read_*  : used to read data to pandas,
    to_*    : used to store data
    to_excel method: method stores the data as an excel file


'''
# save file to excel file
# DataFrame.to_excel("lifetysle.xlsx",sheet_name="lifestyle",index=False)