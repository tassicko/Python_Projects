import pandas as pd

data = {"Name": ["Spongebob", "Patrick", "Squidward"],
        "Age": [30, 35, 50]
        }

dataFrame = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])

print(dataFrame)
#print(dataFrame.loc["Employee 2"])
#_________________________________________
#slicing
#print(dataFrame.iloc[0, 0:])
#_________________________________________
# # ADD a new column
dataFrame["Job"] = ["Cook", "N/A", "Cashier"]
# print(dataFrame)
# print(data)
#__________________________________________
#Add a new Row : create a new dataFrame and concatinate it

new_row = pd.DataFrame([{"Name": "Sandy",
                        "Age": 28,
                        "Job": "Engineer"}])
#df = pd.concat([dataFrame, new_row])
print(new_row)
