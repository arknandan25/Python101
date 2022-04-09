# dict() constructor is used to build dictionaries
zip_codes = dict(ark=12345, jack=23456, tom=88765)
zip2 = dict([('dublin', 'ireland'), ('washington dc', 'USA'), ('new delhi', 'india')])
print(zip_codes)
print(zip2)
print(zip_codes['jack'])

# list all keys of the dictionary
print(list(zip_codes))

# dict.keys() return an iterable view of the dictionary's keys without converting to a list
for x in zip_codes.keys():
    print(x)
# ark
# jack
# tom

# dict.values() : list all values of the dictionary
for x in zip_codes.values():
    print(x)
# 12345
# 23456
# 88765

# dict.items() returns tuples for each key:value entries
for x in zip_codes.items():  # or for x,y in zip_codes.items()  to access key:value separately
    print(x)
# ('ark', 12345)
# ('jack', 23456)
# ('tom', 88765)

# sorted keys (by name) of the dictionary
print(sorted(zip2))

# conditional expressions, searching for key in dict
print('ark' in zip_codes)  # True
print('new jersey' in zip2)  # False

# print all keys corresponding to a particular value from a dict:
value = 10
dict_search = {'Ark': 10, 'Jack': 232, 'YoYo': 10}
for name, val in dict_search.items():
    if val == value:
        print(name)
# Ark
# YoYo

# Updating the dict
# How to update a value corresponding to a key in dict?
t = {}
t['A'] = 1
t['B'] = 5
t['C'] = 2
print("This is an example of updating the dict; before updating:", t)
t['B'] = 3
print("This is an example of updating the dict; after updating:", t)
# This is an example of updating the dict; before updating: {'A': 1, 'B': 5, 'C': 2}
# This is an example of updating the dict; after updating: {'A': 1, 'B': 3, 'C': 2}

# Another way is using the update() method
# The update() method adds element(s) to the dictionary if the key is not in the dict
# If the key is in the dictionary, it updates the key with the new value.
# works with another dict as input or tuples
t1 = {'D': 44}
t2 = {'D': 69}
t.update(t1)
print("Adding new key:value using update:", t)
t.update(t2)
print("Updating  existing key 'D' to a new value using update:", t)
t.update(E=490, F=333, D=7777)
print("Adding and Updating  the dict 't' using update:", t)
t.update()
print("Empty update on a dict will do nothing", t)
# Adding new key:value using update: {'A': 1, 'B': 3, 'C': 2, 'D': 44}
# Updating  existing key 'D' to a new value using update: {'A': 1, 'B': 3, 'C': 2, 'D': 69}
# Adding and Updating  the dict 't' using update: {'A': 1, 'B': 3, 'C': 2, 'D': 7777, 'E': 490, 'F': 333}
# Empty update on a dict will do nothing {'A': 1, 'B': 3, 'C': 2, 'D': 7777, 'E': 490, 'F': 333}

# Deleting stuff from dict and deleting the dict complete!
# delete key:value pair completely from dictionary
# can be done via del dict['key'] or dict.pop('key')
# Understanding what pop() returns can get a bit tricky:
# If key is found - the value corresponding the removed key from the dictionary
# If key is not found and default argument is not specified - KeyError exception is raised
# If key is not found and default argument is specified- value specified as the second argument (default)

del zip2['dublin']
print(zip2)
# {'washington dc': 'USA', 'new delhi': 'india'} <- dublin:value has been deleted

print("The default return type of pop is the value it removes, if key is found:", zip2.pop("new delhi"))
# The default return type of pop is the key:vale it removes, if key is found: india

print(zip2)
# {'washington dc': 'USA'}

k = zip2.pop("jharkhand", "This is an optional value returned as jharkhand is not a key of zip2")
print("We can specify what pop returns, if key is not found:", k)
# We can specify what pop returns, if key is not found: This is an optional value returned as jharkhand is not a key of zip2

# [ERROR]
# k = zip2.pop("jharkhand")
# print("When an undefined key is given to pop for removal, it returns KeyError:", k)
# Traceback (most recent call last):
#   File "/Users/arkchauhan/Documents/Python/dictionary.py", line 90, in <module>
#     k = zip2.pop("jharkhand")
# KeyError: 'jharkhand'

# [ERROR] Delete entire Whole dict
# del zip2
print("Just deleted dict 'zip2', thus getting error:", zip2)
# Traceback (most recent call last):
#   File "/Users/arkchauhan/Documents/Python/dictionary.py", line 105, in <module>
#     print("Just deleted dict 'zip2', thus getting error:", zip2)
# NameError: name 'zip2' is not defined

# ----------------------------------------------------------------------------------------------------------------------
# dict.get() is another way of retrieving data from a dict
# get method returns the value for the specified key if the key is in the dictionary.
# get(key, value) method takes maximum of two parameters:
# key - key to be searched in the dictionary
# value (optional) - Value to be returned if the key is not found. The default value is None.
dict_abc = {"yellow_key": "yellow_value", "green_key": "green_value"}
print("Using get() method here:", dict_abc.get("yellow_key"))
print("Using get() method when key not found, returns None:", dict_abc.get("blue_key"))
print("Using get() method undefined key, with optional value:", dict_abc.get("blue_key", "blue_value"))
print("Using get() method defined key, with optional value, return the original dict value not optional!:", dict_abc.get("green_key", "red_value"))
# Using get() method here: yellow_value
# Using get() method when key not found, returns None: None
# Using get() method undefined key, with optional value: blue_value
# Using get() method defined key, with optional value, return the original dict value not optional!: green_value

# Difference between dict[key] and dict.get()
# print("dict[key] raises KeyError if key not found:", dict_abc["blue_key"])
print("dict.get() returns default value None if key not found:", dict_abc.get("blue_key"))
# Traceback (most recent call last):
#   File "/Users/arkchauhan/Documents/Python/dictionary.py", line 67, in <module>
#     print("dict[key] raises KeyError if key not found:", dict_abc["blue_key"])
# KeyError: 'blue_key'
# dict.get() returns default value None if key not found: None

# ----------------------------------------------------------------------------------------------------------------------
# dict comprehension: used to create dictionaries from arbitrary key:value expressions
# {key: value for (key, value) in dict.items()}
zip3 = {x: x ** 2 for x in range(1, 11)}
print(zip3)
# new dict from another dict
zip4 = {key: value * 5 for (key, value) in zip3.items()}
print(zip4)
#  Always try to replace simple loops and lambdas with comprehensions based on the type of o/p needed
#  If list needed use list comp, else dict comprehension

# ----------------------------------------------------------------------------------------------------------------------
# deep and shallow copy
test_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1988
}
import copy

test_dict_deep_copy = copy.deepcopy(test_dict)
test_dict_shallow_copy = copy.copy(test_dict)
# changes made on the copy object via deep copy will not reflect on the original object
test_dict_deep_copy.pop("year")
print(test_dict_deep_copy)
print(test_dict)
# changes made on the copy object via shallow copy will reflect on the original object
test_dict_shallow_copy.pop("model")
print(test_dict_shallow_copy)
print(test_dict)


# ----------------------------------------------------------------------------------------------------------------------










# Output

# {'ark': 12345, 'jack': 23456, 'tom': 88765}
# {'dublin': 'ireland', 'washington dc': 'USA', 'new delhi': 'india'}
# 23456
# ['ark', 'jack', 'tom']
# ark
# jack
# tom
# 12345
# 23456
# 88765
# ('ark', 12345)
# ('jack', 23456)
# ('tom', 88765)
# ['dublin', 'new delhi', 'washington dc']
# True
# False
# {'washington dc': 'USA', 'new delhi': 'india'}
# {'washington dc': 'USA'}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
# {1: 5, 2: 20, 3: 45, 4: 80, 5: 125, 6: 180, 7: 245, 8: 320, 9: 405, 10: 500}
# {'brand': 'Ford', 'model': 'Mustang'}
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1988}
# {'brand': 'Ford', 'year': 1988}
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1988}
# 2
# None
# {'priority': None, 'alarm1': 'Bear Alarm', 'service': 'cloud watch'}
# None
# Bear Alarm
# {'service': 'cloud watch'}
# a
# b
# -- Do you have any Lollipops ?
# My name is the Great Ark!
# I am an aspirant for life!
# Engineer at work,---
# ----------------------------------------
# key1 : Hello value1 for kwargs
# key2 : value2 for kwargs
