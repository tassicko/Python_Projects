str1 = "strings"
str2 = """this is a test
for multi line strings
this is another line for testing"""

str3 = "this is a string for the word multiple's"
str4 = 'this is a string for the word multiple"s'
str5 = "escape \n sequence \n character "

#print(str2)
#print(len(str1))
print(len(str1[0:len(str1)]))#out: 7
ch = str1[:3]
print(ch) #out: str

print(str2.endswith("ing"))
print(str1.capitalize())
print(str2.replace("a", "t"))
print(str2.find("l"))
print(str2.count("a"))