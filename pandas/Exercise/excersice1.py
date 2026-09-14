import pandas as pd
#task1: Load the dataset
df = pd.read_csv("Z:/codes/python/pandas/Exercise/titanictrain.csv")

#task2: shape, collumn, datatype, describe
#print(df.to_string())
#print(df.columns)

#task3: find missing value
#a = df.isna().any()
#print(a)
# print(df.isna().sum())
# print()
# print((df.loc[:, df.isna().any()]).isna().sum())


#task4: find duplicate rows
#print(df.index.duplicated().sum())

#print(df[df["Survived"] == 1][["Survived"]].count())

#task5: find missing values
print(df.to_string())
