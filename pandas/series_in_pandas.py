import  pandas as pd

#print(pd.__version__)


# data = [100, 200, 123, True, 23.2]
# series = pd.Series(data)
# print(series)
# # 0    100
# # 1    200
# # 2    123
# # dtype: int64
#
# data = [100, 200, 123, True, 23.2]
# series = pd.Series(data)
# print(series)
# # 0     100
# # 1     200
# # 2     123
# # 3    True
# # 4    23.2
# # dtype: object

# data = [100, 200, 123]
# series = pd.Series(data, index=['a', 'b', 'c'])
# print(series)
# a    100
# b    200
# c    123
# dtype: int64


# data = [100, 200, 123]
# series = pd.Series(data)
# print(series.loc[0])
# # 0    100
# # 1    200
# # 2    123
# # dtype: int64

# data = [100, 200, 123, 299, 399, 388]
# a = pd.Series(data)
# print(a[(a > 200) & (a < 300)])


#python dictionary
# calories = {"Day 1": 1750,
#             "Day 2": 2100,
#             "Day 3": 1800}
# series = pd.Series(calories)
# print(series)

# print(series.loc["Day 1"])
# series.loc["Day 1"] += 500
# print(series.loc["Day 1"])

#print(series[series < 2000])





