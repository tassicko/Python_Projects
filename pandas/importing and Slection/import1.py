import pandas as pd

df = pd.read_csv("Z:/codes/python/pandas/importing and Slection/pokemon.csv", index_col="Name")
#df = pd.read_csv("pokemon.csv")
#print(df)
#print(df.to_string())


#---------------------------------------------
#Selction by Column

#print(df["Name"].to_string())
#print(df["Height"].to_string())
#print(df["Weight"].to_string())
#print(df[  [ "Weight", "Height"]  ].to_string())

#print(df[  [ "Weight", "Height"]  ])
#filter by value --> gives boolean output
#print((df[  ["Weight", "Height"]  ] == 20))
#print((df[df["Weight"] == 20]).count() )

#_______________________________________
#Selection by ROW

# pokemon = input("enter a Pokemon name: ")
# try:
#     print(df.loc[pokemon])
# except KeyError:
#     print(f"{pokemon} not found")

#print(df.iloc[ charizard , 2:-1])

#_____________________________________________
#Aggregate Functions using subscript [] operator and .loc
#print(df[["Legendary"]].count())

# print(df[["Height", "Type1"]].count(axis=0))
# print("\n\n\n\n")
# print((df.loc["Charizard":"Mewtwo", "Type1":"Height"]).count(axis=0))

# print(df[(df["Type1"] == "Water" ) & (df["Height"] > 1)
#       ][["Height", "Type2"]])
#
# charizard = df.index.get_loc("Charizard")
# print(df.iloc[charizard, 1:-1])

#aggregate the whole dataframe
# print(df.mean(numeric_only= True))
# print(df.max(numeric_only= True))
# print(df.min(numeric_only= True))
# print(df.count())
# print(df.sum(numeric_only= True))

#___________________________________________________
#groupby Function : it returns a series

group= df.groupby("Type1")
#
# print(group["Height"].mean())
# print(group["Height"].min())
# print(group["Height"].count())
# print(group["Height"].max())
