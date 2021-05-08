# Run code on Pycharm via Control + R (^R)
# Edit/Re-format option + Enter

# printing style
print("aa" * 50)  # aaaaaaaa....50 times

# list of 40 zeroes
list1 = [0] * 40
print(list1)


# Doc Strings
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    print(my_function.__doc__)
    pass


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


# Output
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# {'ham': <class 'str'>, 'eggs': <class 'str'>, 'x': <class 'int'>, 'list1': <class 'list'>, 'return': <class 'str'>}
# cc
