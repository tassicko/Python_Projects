collection = {1, 2, 2, 3, 4, 3, "t", "t", "a", "b", 9,(9.0,)}

try:
    collection.add(["tasik"])
except:
    collection.add(("1,2,3,4", "5,4,,4,4"))
    print("the set did not accepted the list ")

print(collection)
#the set did not accepted the list
#{'b', 1, 2, 3, 4, 'a', ('1,2,3,4', '5,4,,4,4'), 't'}

anotherOne = list(collection)
print(anotherOne)