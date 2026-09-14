import pandas as pd
#1

df = pd.read_csv("/pandas/Exercise/House_pricing.csv")

# print(df.columns)
# print(f"info:\n{df.info()}\n"
#       f"Desciption:\n{df.describe()}\n")

#print(df.isna().sum().to_string())

# print((df.loc[: , df.isna().any()]).isna().sum())
#print( df.isna().sum()[df.isna().sum() > 0])
a = df.isna()
print((df.isna().loc[:,:]))