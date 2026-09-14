di = {
    "name" : ["tasik", "hamim", "ruti"],
    "subjects" : {
        "phy": 2011,
        "chem": 2021,
        "bio": 2024
    }
}

di["subjects"]["phy"] = 33
di["name"][0]= "lamia"
di["name"].append("hotel")
print(di["name"])
print(di["subjects"]["phy"])

#using dictionary methods : .keys and showing how to type cast
#                           dictionary keys into a list format

keys = list(di.keys())
print("""this is a list of all keys inside this dictionary: 
""".join(keys))#namethis is a list of all keys inside this dictionary: subjects
print(keys)#['name', 'subjects']

pairs = list(di.items())
print(type(pairs))#<class 'list'>
print(pairs[1])#('subjects', {'phy': 33, 'chem': 2021, 'bio': 2024})

#how to print values of keys of dictionary
#method 1
print(di["name"])#['lamia', 'hamim', 'ruti', 'hotel']
#method 2
print(di.get("name"))#['lamia', 'hamim', 'ruti', 'hotel']
#now lets see the type of return of .get() function
print(type(di.get("name")))#<class 'list'>
#the difference between these two are:
# using di["name2"] gives error but .git("names2)) doesn't give any errors
