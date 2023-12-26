#!/usr/bin/env python3
from enum import Enum, auto
from typing import TypeVar
from uuid import uuid4

"""
Bank Account Management:
Create a Python class representing a bank account. 
Include methods for deposit, withdrawal, and balance inquiry. 
Implement error handling for insufficient funds and invalid inputs.
"""

class Transaction(Enum):
    DEPOSIT = auto()
    WITHDRAWL = auto()
    BALANCE_INQ = auto()

class InsufficientFundError(Exception):
    """Raise when funds are low"""

class Account:
    def __init__(self, id: str, balance: float):
        self.id = id
        self.balance = balance
        # EDGE-CASE: Make default balance 0, for new accounts

    def deposit(self, amount: float) -> None:
        self.balance += amount
        print(f"Amount deposit: {amount}. Balance: {self.balance}")
        # EDGE-CASE: amount should be float; else raise
        # amount cannot be less than 0; else raise

    def withdraw(self, amount: float) -> None:
        if self.balance <= amount:
            # if the balance in your account is less than the amount you want to withdraw
            # throw exception
            raise InsufficientFundError(f"Balance: {self.balance}")
        self.balance -= amount
        print(f"Amount withdrawn: {amount}. Balance: {self.balance}")

    def balance_inq(self) -> None:
        print(f"Balance: {self.balance}")



a = Account(uuid4(), 5200)
a.deposit(100)
a.withdraw(1000)
a.balance_inq()


# Case 2
b = Account(uuid4(), 5200)
b.deposit(100)
try:    
    b.withdraw(6000)
except InsufficientFundError:
    raise
b.balance_inq()