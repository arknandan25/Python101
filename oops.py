# 1st example is the basic, Just to get familiarized with Python OOP (No complications here)
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class
class House:
    def __init__(self, cost, bills, room_type, hours):
        self.cost = cost
        self.room_bills = bills
        self.room_type = room_type
        self.hours = hours

    def electric_cost(macOS):
        # self can be replaced by anything in each method you make in the class
        if 10 < macOS.hours < 25:
            return macOS.hours * 7.5
        elif 25 < macOS.hours < 44:
            return macOS.hours * 5.5
        else:
            return 1000


# Object = Instance
# There are 2 types of variables: instance variables(all instantiated in __init__) and class variables
# object of class House
h1 = House(1100, 120, "Master", 35)  # This statement calls the __init__ method which works as a constructor
# for defining the properties and setting their values [cost, room_type are all properties/instance variables]
print(h1.room_bills)  # 120

# calling electric_cost
print(h1.electric_cost())  # 192.5

# object
print(h1)  # <__main__.House object at 0x7fb4c97ac5c0>

# object value
print(h1.hours)  # 35
print(h1.room_bills)  # 120
print(h1.room_type)  # Master
print(h1.cost)  # 1100

# modify the object property value
h1.hours = 66
print(h1.hours)  # 66


#  There are 3 types of methods - Instance, Class, and Static
class SampleClass:
    def instance_method(self):
        # can modify both object and class state[access to class variables via special tricks not directly]
        return "This is an instance method, most common type", self

    @classmethod
    def class_method(cls):
        # can only modify the class state, not the object state
        return "This is a  class method", cls

    @staticmethod
    def static_method():
        # can neither modify the object state or the class state
        return "This is a static method"


# Lets view the call: all the methods return a tuple
obj = SampleClass()
print(obj.instance_method())
# ('This is an instance method, most common type', <__main__.SampleClass object at 0x7fc067a13c18>)
# Another way of calling the method by passing the object manually (o/p exactly same):
print(SampleClass.instance_method(obj))
# ('This is an instance method, most common type', <__main__.SampleClass object at 0x7f7f7c0f8c50>)

print(obj.class_method())
# ('This is a  class method', <class '__main__.SampleClass'>)

print(obj.static_method())
# This is a static method

# calling methods without creating an object
print(SampleClass.class_method())  # ('This is a  class method', <class '__main__.SampleClass'>)
print(SampleClass.static_method())  # This is a static method
# print(SampleClass.instance_method())  # Type Error: instance_method() missing 1 required positional argument: 'self'


# **********************************************************************************************************************
# Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        print("Your name is:" + self.name)
        print("Your age is:" + str(self.age))


class Student(Person):
    pass
    # If no __init__ is defined in the child class, it inherits the __init__ of the parent
    # The child's __init__() function overrides the inheritance of the parent's __init__() function


s1 = Student("Ark", 22)
s1.print_details()
# Your name is:Ark
# Your age is:22

# super()
# The Python super() method lets you access methods from a parent class from within a child class.
# This helps reduce repetition in your code. super() does not accept any arguments.


class Student2(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender

    def print_details(self):
        print("Details printed in the Student 2 class. This method is overridden since same belongs to parent class as well.")


s2 = Student2("James", 33, "M")
s2.print_details()  # Details printed in the Student 2 class. This method is overridden since same belongs to parent class as well.


# inherited all the properties and methods of the Person class



# **********************************************************************************************************************
