#!/usr/bin/env python3
# List is a complex data type; Is Mutable (I.e you can make changes after it is created)
#         [0, 1, 2, 3, 4]    Index from left
numbers = [1, 4, 9, 16, 25]
#         [-5, -4, -3, -2, -1]    Index from right

numbers2 = [10, 100, 200, 300, 400, 500]
print(numbers[0])  # 1
print(numbers[-1])  # 25
print(numbers[-5])  # 1
print(numbers[-3])  # 9
# Slicing Lists:
# lst [start:end] # Items from index=start to index=end-1
# lst [start:]    # Items index=start through the rest of the array
# lst [:end]      # All items from the beginning through index=end-1
# lst [:]         # A copy of the whole array
print(numbers[2:4])  # [9, 16]
print(numbers[-3:])  # slicing returns a new list: return a list with last 3 characters : [9, 16, 25]
print(numbers[-5:-2])  # [1, 4, 9]
print(numbers[:])  # entire list: [1, 4, 9, 16, 25]
# list elements from beginning to third last
print(numbers[:-2])  # [1, 4, 9] i.e 0 to -2-1 = -3 -> 0 to -3
#  or
print(numbers[:len(numbers)-2])  # [1, 4, 9] as [0 to n-1] = [0 to 5-2-1] = [0 to 2] = index 0, 1, 2
# reverse list by slicing
print(numbers[::-1])  # [25, 16, 9, 4, 1]

# list concatenation
print(numbers + numbers2)  # [1, 4, 9, 16, 25, 10, 100, 200, 300, 400, 500]

# lists are mutable: means their content can change
numbers2[0] = 5
print(numbers2)  # [5, 100, 200, 300, 400, 500]

# Add a new item to the end of list: append()
numbers.append(49)  # [1, 4, 9, 16, 25, 49]

# Replace values within the list
temp = [5, 6, 7]
numbers[1:4] = temp  # means index 1 to 4-1=3 -> 1 to 3 replaced by temp
print(numbers)  # [1, 5, 6, 7, 25, 49]

# remove the elements of the list
numbers[1:4] = []
print(numbers)  # [1, 25, 49]
# empty list
numbers[:] = []

# length of the list
print(len(numbers))

# insert(index where element to be inserted, value)
# insert function allows us to add a specific element at a specified index
print(numbers2)  # [5, 100, 200, 300, 400, 500]
numbers2.insert(3, 'ark inserted at index 3 i.e before 300')
print(numbers2)  # [5, 100, 200, 'ark inserted at index 3 i.e before 300', 300, 400, 500]

# Nested Lists
l1 = [1, 2, 3]
l2 = [5, 6, 7]
l3 = [l1, l2]
print(l3)  # [[1, 2, 3], [5, 6, 7]]

# List Comprehension:
print("List Comprehension")
[print(x) for x in l1]
# List Comprehension
# 1
# 2
# 3
l4 = [x for x in l1 if x % 2 == 0]
print(l4)  # [2]
l5 = [x ** 2 for x in l1]
print(l5)  # [1, 4, 9]
# return the item if it is not 2, if it is 2 return 69
l6 = [x if x != 2 else 69 for x in l1]  # [1, 69, 3]
print(l6)
l7 = [('Hi ' + x) for x in ['Alice', 'Bob', 'Pete']]
print(l7)  # ['Hi Alice', 'Hi Bob', 'Hi Pete']
l8 = [x * y for x in l1 for y in range(3) if x != y]  # this is a nested loop with the if statement inside
print(l8)  # [0, 2, 0, 2, 0, 3, 6]
# [0, 1, 2, 0, 2, 4, 0, 3, 6] <- is the output if the if condition is not there (simple multiplication)
# 1 with [0, 1, 2] then 2 with [0, 1, 2] and then 3 with [0, 1, 2]

# Loop through list
# 1.for loop
for i in range(len(l1)):
    print(l1[i])
# 2. while loop
while i < len(l1):
    print(l1[i])
    i = i + 1
# iterating using enumerate(list) - index:value
for i, x in enumerate(l1):
    print("Index: " + str(i) + " Value: " + str(x))
# Index: 0 Value: 1
# Index: 1 Value: 2
# Index: 2 Value: 3

# check if the list contains an integer x
l9 = [3, 6, 7, 9, 34]
print(89 in l9)  # False

# Find duplicate elements in a list
l10 = [1, 1, 3, 4, 5, 5, 5, 5, 5, 7, 0]
duplicates, seen = set(), set()
for x in l10:
    if x in seen:
        duplicates.add(x)
    seen.add(x)

print("l10:" + str(l10))  # l10:[1, 1, 3, 4, 5, 5, 5, 5, 5, 7, 0]
print("Duplicates:" + str(duplicates))  # Duplicates:{1, 5}
print("Remaining:" + str(seen))  # Remaining:{0, 1, 3, 4, 5, 7}

#    seen: [1, 3, 4, 5, 7, 0]
#    duplicate: [1, 5]

# Important List Methods

# reverse list
print("Reversing List")
print(l1)  # [1, 2, 3]
l1.reverse()
print(l1)  # [3, 2, 1]

# sorting with O(nlog(n))
print("Sorting List")
l1.sort()
print(l1)  # [1, 2, 3]

# indexing: returns the index of an element in the list
print([5, 7, 9, 34, 25].index(34))  # 3

#  del() TO DELETE ITEMS FROM THE LIST (example below taken with l1 as [1, 2, 3])
print(l1)  # [1, 2, 3]
del l1[0]
print(l1)  # [2, 3]
del l1[0:1]  # 0 to 1-1=0
print(l1)  # [3]
del l1  # delete the entire list
print(l1)  # NameError: name 'l1' is not defined


