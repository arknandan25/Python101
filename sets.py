# A set is a collection which is both unordered, un-indexed, unchangeable, dosen't allow duplicates.
# Sets are used to store multiple items in a single variable.
# Sets are written with curly brackets.
new_set = {'hello', True, 12132342}
print(len(new_set))  # 3
print(type(new_set))  # <class 'set'>
print(new_set)  # {'hello', True, 12132342}

# Empty Set Initialization
s = set()

#  Set Constructor
set2 = set((True, False, "Hello World"))
print(set2)  # {False, True, 'Hello World'}

#  iterate
for i in set2:
    print(i)
# False
# True
# Hello World

# check availability
print("Hello World" in set2)  # True

#  add 1 item to set
set2.add("This is the developer Ark")
print(set2)
# {False, True, 'This is the developer Ark', 'Hello World'}


