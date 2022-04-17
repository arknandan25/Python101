"""
Class: The class is a user-defined data structure that binds the data members and methods into a single unit.
Class is a blueprint or code template for object creation. Using a class, you can create as many objects as you want.

Object: An object is an instance of a class. It is a collection of attributes (variables) and methods.
We use the object of a class to perform actions.


"""


class Person:
    def __init__(self, name, sex, profession):
        # data members (instance variables)
        self.name = name
        self.sex = sex
        self.profession = profession

    # we can override the __new__ method as well, read here: https://howto.lintel.in/python-__new__-magic-method-explained/
    # not very useful, but can be done
    # def __new__(cls, *args, **kwargs):
    #     print("You are initializing your object rn")
    #     return object.__new__(cls, *args, **kwargs)
    #     object = super(Person, cls); try Person.__bases__ to view the classes Person inherits from

    # Behavior (instance methods)
    def show(self):
        print('Name:', self.name, 'Sex:', self.sex, 'Profession:', self.profession)

    # Behavior (instance methods)
    def work(self):
        print(self.name, 'working as a', self.profession)

"""
Constructors
A constructor is a special method used to create and initialize an object of a class. This method is defined in the class.

In Python, Object creation is divided into two parts in Object Creation and Object initialization

    Internally, the __new__ is the method that creates the object
    And, using the __init__() method we can implement constructor to initialize the object.
    Init == Constructor

"""
# create object of a class
jessa = Person('Jessa', 'Female', 'Software Engineer')
jessa.show()
jessa.work()
# Name: Jessa Sex: Female Profession: Software Engineer
# Jessa working as a Software Engineer

# **********************************************************************************************************************

"""
Vars and Methods::
Instance variables: The instance variables are attributes attached to an instance of a class. We define instance variables in the constructor ( the __init__() method of a class).
Class Variables: A class variable is a variable that is declared inside of class, but outside of any instance method or __init__() method.

Instance method: Used to access or modify the object state. If we use instance variables inside a method, such methods are called instance methods.
Class method: Used to access or modify the class state. In method implementation, if we use only class variables, then such type of methods we should declare as a class method.
Static method: It is a general utility method that performs a task in isolation. 
Inside this method, we don’t use instance or class variable because this static method doesn’t have access to the class attributes.
"""


# class methods demo
class Student:
    # class variable
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    # instance method
    def show(self):
        # access instance variables and class variables
        print('Student:', self.name, self.age, Student.school_name)

    # instance method
    def change_age(self, new_age):
        # modify instance variable
        self.age = new_age

    # class method
    @classmethod
    def modify_school_name(cls, new_name):
        # modify class variable
        cls.school_name = new_name


s1 = Student("Harry", 12)
# call instance methods
s1.show()
s1.change_age(14)

# call class method
Student.modify_school_name('XYZ School')
# call instance methods
s1.show()
# Student: Harry 12 ABC School
# Student: Harry 14 XYZ School


# **********************************************************************************************************************
"""
Delete object properties/ Modify Object Properties

Obj.PROPERTY = value
del Obj.PROPERTY

Ok one thing to remember:
class
instance = object
class has static, instance, class methods
class has class and instance variables
objects/instances have properties which are the instance variables defined in init
"""


class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show(self):
        print("Fruit is", self.name, "and Color is", self.color)


# creating object of the class
obj = Fruit("Apple", "red")

# Deleting Object Properties
del obj.name

# Accessing object properties after deleting
try:
    print(obj.name)
except AttributeError:
    print("We have deleted name for obj")
# Output: AttributeError: 'Fruit' object has no attribute 'name'
obj1 = Fruit("mango", "orange")
print(obj1.name)
# We have deleted name for obj
# mango
