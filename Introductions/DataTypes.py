# print(int(input("this is a test: ")))
# a = -15
# b = -2
# c = a//b



# age = int(input("age : " ))
# # print(("no", "yes") [age>=18])
# vote= ("yes", "no") [age<=18]
# print(vote)

# Ask how many times to run the loop
iterations = int(input())

for i in range(iterations):
    age = int(input(f"Person {i+1} age: "))
    vote = ("no", "yes")[age >= 18] 
    print(vote)