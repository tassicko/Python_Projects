import pandas as pd
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

df = pd.read_csv("Z:/codes/python/pandas/importing and Slection/pokemon.csv")

#drop irrelevant columns
# df = df.drop(columns=["Legendary"])
# df = df.drop(columns=["No"])
# print(df)

#Handle missing data : Drop not Available
#df = df.dropna(subset=["Type2"])

#Fill/Replace any not available values: replace any not available values
# within the column of Type2 with the following value:
#df = df.fillna({"Type2": "None"})


#fix any inconsistent values
#df["Type1"] = df["Type1"].replace({"Grass": "GRASS", "Fire": "FIRE", "Water": "WATER"})
#print(df[ df["Type1"] == "GRASS"] )
#print(df.to_string())

#Standardize text
# df["Name"] = df["Name"].str.lower()
# print(df.to_string())

#Fix or Change DataTypes
# df["Legendary"] = df["Legendary"].astype(bool)
# print(df[df["Legendary"]==True].to_string())

#Remove Duplicate Values
#df = df.drop_duplicates()

#print(df.head().to_string())
#print(df.describe())

a = df["Type1"].isin(["Water"]) #type--> series bool
b = df[ "Type2"] == "Water"

print(df[b])