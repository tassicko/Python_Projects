import pandas as pd
#in series we cant name the column so the following
#way does not give any series
series = pd.Series({
    "Name": ["Tasik", "Tarik", "Mugdha"]
})


series = pd.Series({
    "Name": "Tasik",
    "Age": 23
})
print(series)

data = [100, 200, 123, True, 23.2]
series = pd.Series(data)
print(series)