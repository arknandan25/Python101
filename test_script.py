#!/usr/bin/env python3

from enum import Enum
from hashlib import md5

from more_itertools import divide


class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    BALANCE = "balance"


class Transaction:

    t_id: int
    t_type: TransactionType


# x = Transaction(1, "1")
# print(x.t_type)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_details(self):
#         print("Your name is:" + self.name)
#         print("Your age is:" + str(self.age))
#
#
# class Student2(Person):
#     def __init__(self, gender):
#         super().__init__()
#         self.gender = gender
#
# print(Student2("asas", "SDsd", "sdsd"))

URL_ID_LENGTH=7
def base_encode(num, base=62):
    digits = []
    while num > 0:
      remainder = num % base
      digits.append(remainder)
      num = num // base
    print(digits) # digits will be base64 hash digits, we now need to map these hash digits to abse62 characters
    # digits = digits.reverse
    # print(digits)
    print(digits[:URL_ID_LENGTH])
    return digits



s = "asadsdsadasdasd"
g = "".join(str(ord(i)) for i in s)
x = base_encode(int(g))


