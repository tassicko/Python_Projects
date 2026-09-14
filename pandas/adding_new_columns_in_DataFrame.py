import pandas as pd

data = {"Name": ["Tasik", "Tarik", "Mohsin"],
        "Desk": ["A1", "B2", "A2"]}
df = pd.DataFrame(data)


# 0. While creating DataFrame
# df = pd.DataFrame({
#     "Name": ["A", "B", "C"],
#     "Age": [20, 21, 22]
# })


# 1. Dictionary-style assignment
df["Age"] = [20, 21, 22]

# 2. update()
df.update({"Height": [20, 21, 22]})

# 3. insert()
df.insert(1, "Marks", [20, 21, 22])

# 4. assign()
df = df.assign(Age=[20, 21, 22])

# 5. Using another column
df["Bonus"] = df["Marks"] + 5

# 6. loc[]
df.loc[:, "Merits"] = [20, 21, 22]

# 7. concat()
new_column = pd.Series([20, 21, 22], name="City")
df = pd.concat([df, new_column], axis=1)



print(df)