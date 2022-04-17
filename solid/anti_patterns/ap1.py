"""
Assigning Mutable default values to function variables



TBD


"""





"""
Similar AP related to class variables


* Remember it fine to access class vars from class name or instances of class, but should only be updated from class name

This anti-pattern is a bit diff for class variables, from Ex2 you can see assigning mutable value to class var doesn't 
do much damage, as updating it, the updates value can be accessed from instances of the class and from class name.

But when we update the `name` class variable from instance of class:
t.name = "Rofl"
print(t.var)
print(Test.var)
print(t.name)
print(Test.name)
# ['100']
# ['100']
# Rofl
# Lol  <------ This is the anti-pattern

t creates a local attribute called name, which shadows the class variable when accessed.


As seen with `f`:
f.var = {"lol1": "lol2"}   # anti pattern again, on changing the data structure, f creates a local var
print(f.var)
t.var.extend([400, 500])
print(t.var)
print(Test.var)
print(f.__dict__)

g = Test(44)
print(g.var)
# {'lol1': 'lol2'}
# ['100', 400, 500]
# ['100', 400, 500]
# {'a': 45, 'var': {'lol1': 'lol2'}}
# ['100', 400, 500]

CONCLUSION::
This means we should not change the value of a class variable from a class instance(object) in general, appending/updating
a mutable value seems to work fine but chnagin gthe value completely creates a local instance copy that shadow the class variable.
"""

# Ex2
class Test:
    var = []
    name = "Lol"

    def __init__(self, a):
        self.a = a


t = Test(23)
print(t.var)
print(Test.var)
print(t.name)
print(Test.name)
# []
# []
# Lol
# Lol

# update var with instance t
t.var.append("100")
t.name = "Rofl"
print(t.var)
print(Test.var)
print(t.name)
print(Test.name)
# ['100']
# ['100']
# Rofl
# Lol  <------ This is the anti-pattern

print(t.__dict__)
print(Test.__dict__)
# {'a': 23, 'name': 'Rofl'}
# {'__module__': '__main__', 'var': ['100'], 'name': 'Lol', '__init__': <function Test.__init__ at 0x7fb60a70fd08>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None}

# assigning a non-existing var from instance variable
# surprisingly, it creates a new attr called addr for this instance t
t.addr = "3, Dublin"

print(t.__dict__)
print(Test.__dict__)
# {'a': 23, 'name': 'Rofl', 'addr': '3, Dublin'}
# {'__module__': '__main__', 'var': ['100'], 'name': 'Lol', '__init__': <function Test.__init__ at 0x7fb60a70fd08>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None}


# Creating another instance
f = Test(45)
print(f.var)
print(f.name)
# ['100']
# Lol


f.var = {"lol1": "lol2"}   # anti pattern again, on changing the data structure, f creates a local var
print(f.var)
t.var.extend([400, 500])
print(t.var)
print(Test.var)
print(f.__dict__)

g = Test(44)
print(g.var)
# {'lol1': 'lol2'}
# ['100', 400, 500]
# ['100', 400, 500]
# {'a': 45, 'var': {'lol1': 'lol2'}}
# ['100', 400, 500]
