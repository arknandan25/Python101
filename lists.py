numbers = [1, 4, 9, 16, 25]
numbers2 = [10, 100, 200, 300, 400, 500]
print(numbers[0])
print(numbers[-1])
print(numbers[-3:])  # slicing returns a new list: return a list with last 3 characters
print(numbers[:])  # entire list
# list concatenation
print(numbers + numbers2)
# lists are mutable: means their content can change
numbers2[0] = 5
print(numbers2)
# Add a new item to the end of list: append()
numbers.append(49)
# Replace values within the list
temp = [5, 6, 7]
numbers[1:4] = temp
print(numbers)
# remove the elements of the list
numbers[1:4] = []
print(numbers)
# empty list
numbers[:] = []

# length of the list
print(len(numbers))

# Nested Lists
l1 = [1, 2, 3]
l2 = [5, 6, 7]
l3 = [l1, l2]
print(l3)
# List Comprehension
l4 = [x for x in l1 if x % 2 == 0]
print(l4)
l5 = [x ** 2 for x in l1]
print(l5)
# return the item if it is not 2, if it is 2 return 69
l6 = [x if x != 2 else 69 for x in l1 ]
print(l6)

# Loop through list
# 1.for loop
for i in range(len(l1)):
    print(l1[i])
# 2. while loop
while i < len(l1):
    print(l1[i])
    i = i + 1
# 3. list comprehension
print("List Comprehension")
[print(x) for x in l1]

# List METHODS
#  del() TO DELETE ITEMS FROM THE LIST
del l1[0]
del l1[0:1]
print(l1)
del l1
print(l1)  # NameError: name 'l1' is not defined



#
# 1
# 25
# [9, 16, 25]
# [1, 4, 9, 16, 25]
# [1, 4, 9, 16, 25, 10, 100, 200, 300, 400, 500]
# [5, 100, 200, 300, 400, 500]
# [1, 5, 6, 7, 25, 49]
# [1, 25, 49]
# 0
# [[1, 2, 3], [5, 6, 7]]
# [2]
# [1, 4, 9]
# [1, 69, 3]
# 1
# 2
# 3
# 3
# List Comprehension
# 1
# 2
# 3
# [3]
