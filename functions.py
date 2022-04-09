# Python function arguments are very important to understand
# In Python, we can pass a variable number of arguments to a function using special symbols. There are two special symbols:
#
#     *args (Non Keyword Arguments)
#     **kwargs (Keyword Arguments)
#
# We use *args and **kwargs as an argument when we are unsure about the number of arguments to pass in the functions.


# *args:: The arguments are passed as a tuple.
def fn(*args):
    print(type(args))
    for i in args:
        print(i)


fn(1,2,3,4,5,6)
# <class 'tuple'>
# 1
# 2
# 3
# 4
# 5
# 6

try:
    fn(234, 45, a=1)
except TypeError:
    print("*args takes positional arguments, while when we say a=1;a becomes a keyword argument")
# Traceback (most recent call last):
#   File "/Users/arkchauhan/Documents/Python/functions.py", line 22, in <module>
#     fn(234, 45, a=1 )
# TypeError: fn() got an unexpected keyword argument 'a'

# Now comes the question what is a positional and keyword argument?
"""
Positional argument: are arguments that can be called by their position in the function call.

Keyword arguments: are arguments that can be called by their name. Also known as named arguments

E.g. Here using the "keyword argument" feature (where the argument is named rather than relying on its position). 
Without that, values are bound to names based on order alone. So, in this example, the two calls below are equivalent:

def process_a_and_b(a, b):
   # blah code

process_a_and_b(1, 2) # positional arguments
process_a_and_b(b=2, a=1) # keyword arguments

*args, **kwargs allow us to send many parameters (even if we don;t know how many the caller is sending)
*args relies on positional arguments:
    when positional arguments(that rely on position, and have no nae given to them) are sent to *args, it becomes a tuple
**kwargs relies on keyword arguments:
    when keyword arguments are sent to **kwargs, it basically becomes/is accessible as a dict
    where we can access data via key and its value
"""

# **kwargs
def fn_k(**data):
    print(type(data))
    for k, v in data.items():
        print("{0}: {1}".format(k, v))


fn_k(a=32, b=44, c=56) # a b c are keyword arguments
# or we can send a dict
data_to_pass = {"a": 100, "b": 400}
fn_k(**data_to_pass)
# <class 'dict'>
# a: 32
# b: 44
# c: 56
# <class 'dict'>
# a: 100
# b: 400

# ----------------------------------------------------------------------------------------------------------------------
# More kwargs, args examples
def func(var1, var2=None, **kwargs):
    print(var1)
    print(var2)
    print(kwargs)


#  in this example all the parameters in function call are independent: 2,None sent for 2nd, kwargs(dict)
kwargs = {"priority": None, "alarm1": "Bear Alarm", "service": "cloud watch"}
func(2, **kwargs)  # 2 is a positional argument, that means var1 will be assigned 2 bec of its position
# 2
# None
# {'priority': None, 'alarm1': 'Bear Alarm', 'service': 'cloud watch'}


# This a very practical of code that can be used in code
# in this example the keys of the dict correspond to the function arguments
# Here we make all arguments as keyword arguments, when passed
kwargs1 = {"var1": None, "var2": "Bear Alarm", "service": "cloud watch"}
func(**kwargs1)
# None
# Bear Alarm
# {'service': 'cloud watch'}

# ----------------------------------------------------------------------------------------------------------------------
# **dict contain keyword arguments, *name contain positional arguments
# *name must occur before **dict
# This means positional arguments must be specified before keyword arguments in function call
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop(
    "Lollipops",  # positional arg -> assigned to kind
    "My name is the Great Ark!",  # positional arg -> arguments
    "I am an aspirant for life!",  # positional arg -> arguments
    "Engineer at work,---",  # positional arg -> arguments
    key1="Hello value1 for kwargs",  # keyword argument -> assigned to keywords
    key2="value2 for kwargs"  # keyword argument -> assigned to keywords
)
# -- Do you have any Lollipops ?
# My name is the Great Ark!
# I am an aspirant for life!
# Engineer at work,---
# ----------------------------------------
# key1 : Hello value1 for kwargs
# key2 : value2 for kwargs

# ----------------------------------------------------------------------------------------------------------------------
# Sending a dict as argument to a fn, not same as keyword arguments
# sending normal dictionary
def func2(dict1):
    for key, val in dict1.items():
        print(f"{key}, : {val}")


D = {'a': 2, 'b': 4}
func2(D)
# a, : 2
# b, : 4

# ----------------------------------------------------------------------------------------------------------------------
# Sending multiple data types in kwargs and args
def fn(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


d1 = {"s": 3, "t": 44}
d2 = {"o": 13, "p": 23}
kargs = {
    "g": "fakir",
    "mellow": d2,
}

# fn(1, 2, d1, **kargs)
# 1
# 2
# ({'s': 3, 't': 44},) <- notice the d1 dict is inside a tuple
# {'g': 'fakir', 'mellow': {'o': 13, 'p': 23}}

try:
    fn("hello kitty", a=23, b=66, j="HI there", l=d2, )
except TypeError:
    print("Not allowed here")
# Traceback (most recent call last):
#   File "/Users/arkchauhan/Documents/Python/functions.py", line 169, in <module>
#     fn("hello kitty",a=23, b=66, j="HI there", l=d2, )
# TypeError: fn() got multiple values for argument 'a'

# my intention her was that "hello kitty" would be assigned to *args, but it dosen't seem to work
# see how keyword args are assigned here


# ----------------------------------------------------------------------------------------------------------------------
