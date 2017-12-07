"""
List Comprehension
  Take up less lines of code to compress a for-loop
"""
myList = [i*2 for i in range(10) if i % 2]
print(myList)

#what it would look like without list-comp
mylist = []
for i in range(10):
    if i % 2:
        mylist.append(i*2)
print(mylist)

"""
Creating a Matrix with list-comp
"""
matrix = [list(range(5)) for i in range(5)]
for i in matrix:
    print(i)
