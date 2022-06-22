import pandas as pd
# create dataset
# dataframe
# titanic dataset
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

print(TitanicDataframe)

# cretae series
# lists
usersAge=pd.Series([15,23,89],name="Users Age")

print(usersAge)

