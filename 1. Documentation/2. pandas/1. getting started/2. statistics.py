import pandas as pd
# create data frame
# data frame
# titanic dataframe
# dictionary
TitanicDataframe=pd.DataFrame(
    {
        # passengers details
        # name
        "Name":[
            "Sajal Tiwari",
            "Pankaj Mishra",
            "Sanjana Dixit"
        ],
        # age
        "Age":[
            25,35,50
        ],
        # gender
        "Gender":[
            "male","male","female"
        ]
    }
)

# print
# series
print(f"Data Frame:\n {TitanicDataframe}\n")
# specific column
print("Age Column:\n", TitanicDataframe["Age"], "\n")
# maximum value
print(f"Maximum Value:\n {TitanicDataframe.max()}\n")
# minimum value
print(f" Mimimum Value: \n {TitanicDataframe.min()}\n")
# description
print(f" Description:\n{TitanicDataframe.describe()}\n")
