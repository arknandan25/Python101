"""
In Python, Object creation is divided into two parts in Object Creation and Object initialization

    Internally, the __new__ is the method that creates the object
    And, using the __init__() method we can implement constructor to initialize the object.

In Python, internally, the __new__ is the method that creates the object, and __del__ method is called to destroy the object when the reference count for that object becomes zero.
def __init__(self):
    # body of the constructor


self: The first argument self refers to the current object. We can name anything here, like abc but hen use that everywhere in class

In Python, we have the following three types of constructors.

    Default Constructor
    Non-parametrized constructor
    Parameterized constructor

[No need for examples, easy, view notion OOP pics]
"""

# **********************************************************************************************************************
import time

"""
Constructor Overloading
Constructor overloading is a concept of having more than one constructor with a different parameters list in such a way so that each constructor can perform different tasks.

For example, we can create a three constructor which accepts a different set of parameters

Python does not support constructor overloading. If we define multiple constructors then, 
the interpreter will considers only the last constructor and throws an error if the sequence of the arguments doesn’t match as per the last constructor. The following example shows the same.
"""
class Student:
    # one argument constructor
    def __init__(self, name):
        print("One arguments constructor")
        self.name = name

    # two argument constructor
    def __init__(self, name, age):
        print("Two arguments constructor")
        self.name = name
        self.age = age

# creating first object
# emma = Student('Emma')

# creating Second object
kelly = Student('Kelly', 13)
# Traceback (most recent call last):
#   File "/Users/arkchauhan/Documents/Python/OOP/constructors_destructors.py", line 46, in <module>
#     emma = Student('Emma')
# TypeError: __init__() missing 1 required positional argument: 'age'

# **********************************************************************************************************************

"""
Constructor Chaining

Constructors are used for instantiating an object. The task of the constructor is to assign value to data members when an object of the class is created.

Constructor chaining is the process of calling one constructor from another constructor. 
Constructor chaining is useful when you want to invoke multiple constructors, one after another, by initializing only one instance.

In Python, constructor chaining is convenient when we are dealing with inheritance. 
When an instance of a child class is initialized, the constructors of all the parent classes are first invoked and then, in the end, the constructor of the child class is invoked.

Using the super() method we can invoke the parent class constructor from a child class.
"""


class Vehicle:
    # Constructor of Vehicle
    def __init__(self, engine):
        print('Inside Vehicle Constructor')
        self.engine = engine


class Car(Vehicle):
    # Constructor of Car
    def __init__(self, engine, max_speed):
        super().__init__(engine)
        print('Inside Car Constructor')
        self.max_speed = max_speed


class Electric_Car(Car):
    # Constructor of Electric Car
    def __init__(self, engine, max_speed, km_range):
        super().__init__(engine, max_speed)
        print('Inside Electric Car Constructor')
        self.km_range = km_range


# Object of electric car
ev = Electric_Car('1500cc', 240, 750)
print(f'Engine={ev.engine}, Max Speed={ev.max_speed}, Km range={ev.km_range}')
# Inside Vehicle Constructor
# Inside Car Constructor
# Inside Electric Car Constructor
# Engine=1500cc, Max Speed=240, Km range=750

# **********************************************************************************************************************
"""
Counting the Number of objects of a Class

Use a class variable, always update a class variable via Class name
See AP1
"""
class Employee:
    count = 0
    def __init__(self):
        Employee.count = Employee.count + 1


# creating objects
e1 = Employee()
e2 = Employee()
e2 = Employee()
print("The number of Employee:", Employee.count)
# The number of Employee: 3

# **********************************************************************************************************************

"""
Constructor Return Value

In Python, the constructor does not return any value. Therefore, while declaring a constructor, we don’t have anything like return type. 
Instead, a constructor is implicitly called at the time of object instantiation. Thus, it has the sole purpose of initializing the instance variables.

The __init__() is required to return None. We can not return something else. If we try to return a non-None value from the __init__() method, it will raise TypeError.
"""
class Test:

    def __init__(self, i):
        self.id = i
        return True

# d = Test(10)
#   File "/Users/arkchauhan/Documents/Python/OOP/constructors_destructors.py", line 139, in <module>
#     d = Test(10)
# TypeError: __init__() should return None, not 'bool'

# **********************************************************************************************************************

"""
Destructors

In object-oriented programming, A destructor is called when an object is deleted or destroyed. 
Destructor is used to perform the clean-up activity before destroying the object, such as closing database connections or file handle.

Python has a garbage collector that handles memory management automatically. For example, it cleans up the memory when an object goes out of scope.

But it’s not just memory that has to be freed when an object is destroyed. 
We must release or close the other resources object were using, such as open files, database connections, cleaning up the buffer or cache. 
To perform all those cleanup tasks we use destructor in Python. 

In Python, destructor is not called manually but completely automatic. destructor gets called in the following two cases
    When an object goes out of scope (i.e the application execution ends) or
    The reference counter of the object reaches 0. (View notion): https://pynative.com/python-destructor/
The destructor will not invoke when we delete object reference. It will only invoke when all references to the objects get deleted.


The magic method __del__() is used as the destructor in Python. 
The __del__() method will be implicitly invoked when all references to the object have been deleted, i.e., is when an object is eligible for the garbage collector.
This method is automatically called by Python when the instance is about to be destroyed. It is also called a finalizer or (improperly) a destructor.
"""
# Very important example


class Student:

    # constructor
    def __init__(self, name):
        self.name = name
        print('Object initialized')

    def show(self):
        print('Hello, my name is', self.name)

    # destructor
    def __del__(self):
        #  The __del__() method id called automatically in python for garbage collection i.e destruction of objects
        #  The call is only made on
        print('Object destroyed')
        print(self)


# create object
s1 = Student('Emma')
s1.show()
s2 = s1  # this smt, makes 2 references to object Student('Emma'):: s1, s2, i.e the reference_count=2
# NOTE:: `del obj_name` does not delete the object, neither does it call the __del__() method we defined in the class
# `del obj_name` deletes the reference s1
# reference_count=1
del s1
print("Hello this is time wasting statement!!")
# Here the application execution comes to end, i.e object goes out of scope so __del__() gets called automatically as part of garbage collection
# That's why we see the 'Object destroyed' print after this print statement
# Note __del__() is called automatically under 2 circumstances only:
#     When an object goes out of scope (i.e the application execution ends) <This is the case in this example>
#     The reference counter of the object reaches 0. (View notion): https://pynative.com/python-destructor/

# Object initialized
# Hello, my name is Emma
# Hello this is time wasting statement!!
# Object destroyed
# <__main__.Student object at 0x7fdbb3df2b00>


"""
CASE2 demo:
To demo case 2 where ref count reches 0, performing in ipython as this file would not be useful
class Test:
    def __init__(lol, a):
        lol.a = a
    def pp(lol):
        print(lol.a)
    def __del__(lol):
        print(lol, "Deleted here")
t1 = Test(44)
del t1
print("Random line")

O/P:
# <__main__.Test object at 0x1026d1550> Deleted here
# Random line

Remember del t1 does not call __del__() in this case as well
as we do `del t1`, the ref_count for that  obj goes to 0 and __del__() gets called automatically 
"""


