# Run code on Pycharm via Control + R (^R)
# Edit/Re-format option + Enter

# printing style
print("aa" * 50)  # aaaaaaaa....50 times

# list of 40 zeroes
list1 = [0] * 40
print(list1)

# ----------------------------------------------------------------------------------------------------------------------
# range()
# range(start, stop, step)
# range(5) -> 0 to 5-1= 4

print(range(len(list1)))
# 0 to 39
for x in range(0, len(list1)):
    print(x)
# iterate through a list/array using range
for i in range(0, len(list1)):
    print(list1[i])

# ----------------------------------------------------------------------------------------------------------------------
# Doc Strings
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    print(my_function.__doc__)
    pass

# ----------------------------------------------------------------------------------------------------------------------
#  Function Annotations: optional metadata about types used by user-defined functions
def my_function2(ham: str, eggs: str = "eggs", x: int = 5, list1: list = []) -> str:
    """Do nothing, but document this function here.

    No, really, it doesn't do anything.
    :param ham: define ham usage
    :param eggs: "
    :param x: "
    :param list1: "
    :return: what are you returning
    :rtype: dict
    """
    print(my_function2.__annotations__)
    return "cc"


c = my_function2("test ham", "eggs fried", 99, [3,5,6])
print(c)

# ----------------------------------------------------------------------------------------------------------------------
# Conditional Statements
a = 89
b = 9
if 77 > 78:
    print("77 greater!")
elif 99 < 22:
    print("99 is smaller!")
else:
    print("You are in the matrix@@££$lol")
# You are in the matrix@@££$lol

# short hand operation- if
if a > b: print("a is greater")  # a is greater

# short hand operation- if:else [Ternary Operators/Conditional Expressions]
print("a is greater!!!") if a > b else print("b is greater")  # a is greater!!!

#  Logical Operators
# Both conditions should be true
if a > b and 88 < 100:
    print("Good")  # Good
# Either condition  true then true
if a < b or 88 < 100:
    print("Good OR")  # Good OR

# if with no content
if a > b:
    pass

# ----------------------------------------------------------------------------------------------------------------------
# Magic Methods/ Dunder Methods
# Magic methods in Python are the special methods that start and end with the double underscores
# Magic methods are not meant to be invoked directly by you, but the invocation happens internally from the class on a certain action.
# For example, when you add two numbers using the + operator, internally, the __add__() method will be called
# __new__() magic method is initiated before the __init__ method
# Just like new in languages like C, Java __new__() creates a new instance of the a class
# 45.__add__(5) is equivalent to 45 + 5
# ----------------------------------------------------------------------------------------------------------------------
# Python String Formatting
# The format() method allows you to format selected parts of a string.
txt = "When you put your mind to it, the {} feels jealous."
print(txt.format("world"))
# When you put your mind to it, the world feels jealous.

# Index Numbers
txt1 = "Live without {0} and {1}"
print(txt1.format("regret", "lies"))
# Live without regret and lies

# Named Index
txt2 = "Anyone can {para1} up, it's the {para2} thing in the world to do"
print(txt2.format(para1="give", para2="easiest"))
# Anyone can give up, it's the easiest thing in the world to do

#  f-strings
# Also called “formatted string literals,”
# f-strings are string literals that have an f at the beginning and curly braces containing expressions that will be replaced with their values
# The expressions are evaluated at runtime and then formatted using the __format__ protocol.
name = "f-string"
hello_var = f"Hey, this is an {name}. This is a new way of formatting in python"
print(hello_var)  # Hey, this is an f-string. This is a new way of formatting in python
print(f" {23 * 77} is the multiplication expression. Expression like {name.upper()} works!")
#  1771 is the multiplication expression. Expression like F-STRING works!
# ----------------------------------------------------------------------------------------------------------------------
# Passing functions as Arguments(Core for Decorators[Useless complicated concept])















# Output
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# {'ham': <class 'str'>, 'eggs': <class 'str'>, 'x': <class 'int'>, 'list1': <class 'list'>, 'return': <class 'str'>}
# cc
