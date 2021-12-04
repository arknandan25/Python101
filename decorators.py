#!/usr/bin/env python3
def func(a, b):
    return a + b


def func1():
    print("Hello")


def caller(f):
    # sample f = func(3, 10)
    return f


print(func(2, 10))
print(func)
print(func1)
print(caller(func(3, 10)))
print(caller(func1))
# 12
# <function func at 0x105c3c0d0>
# <function func1 at 0x105df7280>
# 13
# <function func1 at 0x10f8ec280>


# Writing a sample decorator
def woah(f):
    import ipdb
    ipdb.set_trace()
    def inner_woah(*args, **kwargs):
        import ipdb
        ipdb.set_trace()
        response = f(*args, **kwargs)
        import ipdb
        ipdb.set_trace()
        return response
    return inner_woah


@woah
def hello_kitty(a, b):
    print("In function")
    import ipdb
    ipdb.set_trace()
    return a + b


hello_kitty(2, 50)
# It is imp to understand this execution ->
# when hello_kitty(2, 50) is executed hello_kitty triggers the decorator woah
# When we return inner_woah we don't call inner_woah(), we return a reference to inner_woah method
# this reference is then called with 2, 50 -> hello_kitty(2, 50) becomes -> inner_woah(2, 50)

#  ➜ ./decorators.py
# 12
# <function func at 0x1066f20d0>
# <function func1 at 0x1068ac280>
# 13
# <function func1 at 0x1068ac280>
# > /Users/arkchauhan/Documents/Python/decorators.py(31)woah()
#      30     ipdb.set_trace()
# ---> 31     def inner_woah(*args, **kwargs):
#      32         import ipdb
#
# ipdb> f
# <function hello_kitty at 0x1068ac310>
# ipdb> n
# > /Users/arkchauhan/Documents/Python/decorators.py(38)woah()
#      37         return response
# ---> 38     return inner_woah
#      39
#
# ipdb> n
# --Return--
# <function woa...t 0x1085ae8b0>
# > /Users/arkchauhan/Documents/Python/decorators.py(38)woah()
#      37         return response
# ---> 38     return inner_woah
#      39
#
# ipdb> n
# > /Users/arkchauhan/Documents/Python/decorators.py(49)<module>()
#      47
#      48
# ---> 49 hello_kitty(2, 50)
#
# ipdb> n
# > /Users/arkchauhan/Documents/Python/decorators.py(34)inner_woah()
#      33         ipdb.set_trace()
# ---> 34         response = f(*args, **kwargs)
#      35         import ipdb
#
# ipdb> args
# args = (2, 50)
# kwargs = {}
# ipdb> n
# In function
# > /Users/arkchauhan/Documents/Python/decorators.py(46)hello_kitty()
#      45     ipdb.set_trace()
# ---> 46     return a + b
#      47
#
# ipdb> a, b
# a = 2
# b = 50
# ipdb> n
# --Return--
# 52
# > /Users/arkchauhan/Documents/Python/decorators.py(46)hello_kitty()
#      45     ipdb.set_trace()
# ---> 46     return a + b
#      47
#
# ipdb> n
# > /Users/arkchauhan/Documents/Python/decorators.py(35)inner_woah()
#      34         response = f(*args, **kwargs)
# ---> 35         import ipdb
#      36         ipdb.set_trace()
#
# ipdb> n
# > /Users/arkchauhan/Documents/Python/decorators.py(36)inner_woah()
#      35         import ipdb
# ---> 36         ipdb.set_trace()
#      37         return response
#
# ipdb> response
# 52
# ipdb> c
# > /Users/arkchauhan/Documents/Python/decorators.py(37)inner_woah()
#      36         ipdb.set_trace()
# ---> 37         return response
#      38     return inner_woah
