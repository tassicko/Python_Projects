# count = 1
# while count <= 5:
#     print("nai")
#     count += 1
n = int(input())
for i in range(n):
    print( " " * (n-1-i)  ,"*" * (2*i+1))