list1 = []
list2 = []
def make_list():
    for i in range(5):
        list1.append(input())
        list2.append(input())

def display():
    for i in range(5):
        print(list1[i], end=" ")
        print(list2[i])


make_list()
display()

# for i, j in (list1, list2):
#     print(i, end = " ")
#     print(j)


