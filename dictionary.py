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

# delete key:value from dictionary
del zip2['dublin']
print(zip2)
zip2.pop("new delhi")
print(zip2)

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
#  passing a dict as a dictionary to a function [highly used & causes problems lol]
# 1st way: Keyword Arguments (**dict) and Default Arguments in Function arguments
def func(var1, var2=None, **kwargs):
    print(var1)
    print(var2)
    print(kwargs)


#  in this example all the parameters in function call are independent: 2,None sent for 2nd, kwargs(dict)
kwargs = {"priority": None, "alarm1": "Bear Alarm", "service": "cloud watch"}
func(2, **kwargs)
# 2
# None
# {'priority': None, 'alarm1': 'Bear Alarm', 'service': 'cloud watch'}


# in this example the keys of the dict correspond to the function arguments
kwargs1 = {"var1": None, "var2": "Bear Alarm", "service": "cloud watch"}
func(**kwargs1)
# None
# Bear Alarm
# {'service': 'cloud watch'}


#  2nd way : sending normal dictionary
def func2(dict1):
    for key, val in dict1.items():
        print(key)


D = {'a': 2, 'b': 4}
func2(D)


# 3rd try : **dict contain keyword arguments, *name contain positional arguments
# *name must occur before **dict
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop(
    "Lollipops",
    "My name is the Great Ark!",
    "I am an aspirant for life!",
    "Engineer at work,---",
    key1="Hello value1 for kwargs",
    key2="value2 for kwargs"
)
# -- Do you have any Lollipops ?
# My name is the Great Ark!
# I am an aspirant for life!
# Engineer at work,---
# ----------------------------------------
# key1 : Hello value1 for kwargs
# key2 : value2 for kwargs


# 4th just more sample
def fruit_bowl(*fruits):
    print("Following fruits would make a mean fruit salad:")
    for f in fruits:
        print(f)


fruits = ['banana', 'apple', 'watermelon', 'mango', 'kiwi', 'orange', 'dragon fruit']
fruit_bowl(*fruits)
# in the above call, if you have * or ** in the function definition then *,** should be used in the call as well
# Following fruits would make a mean fruit salad:
# banana
# apple
# watermelon
# mango
# kiwi
# orange
# dragon fruit
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
