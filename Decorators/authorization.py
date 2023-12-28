#!/usr/bin/env python3
import secrets
from enum import Enum, auto
import functools
"""
Authorization Decorator:
Write a decorator that checks if a user has the necessary permissions to execute a function. 
Apply this decorator to functions that require authorization.
Covers multiple decorator hierarchy: Come first execute first
passing arguments to decorators
"""

class AccessDenied(Exception):
    """Raise when no access"""

class Permissions(Enum):
    DRY_RUN = auto()
    EXECUTE = auto()


PERMISSION_MAPPING = {
    "ark": [Permissions.EXECUTE, Permissions.DRY_RUN],
    "coolBoY": [Permissions.DRY_RUN],
}

class User:
    def __init__(self, name):
        self.name = name

    def has_permission(self, permission):
        execution_permissions = PERMISSION_MAPPING.get(self.name)
        if execution_permissions is None:
            # user does not exist in DB
            raise AccessDenied(f"User {self.name} does not exist in DB")
        if permission in execution_permissions:
            print(f"{self.name} is allowed for: {permission}")
            return True
        # user exists in DB but does not have the apt permissions
        raise AccessDenied(f"User {self.name} has no execution permissions")
    
    def __repr__(self):
        return self.name


def debug(func):
    """debug decorator logs all fn args and return values"""
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        args_list = [repr(a) for a in args]
        kwargs_list = [f"{k}={v!r}" for k, v in kwargs.items()] 
        # repr -> !r of value 
        signature = ", ".join(args_list + kwargs_list)
        print(f"Calling function: {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"You key has been generated!")
        return result
    return wrap


def authorization_checker(func):
    """Authorization decorator"""
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        if kwargs["user"].has_permission(kwargs["execution_mode"]):
            return func(*args, **kwargs)
    return wrap



@authorization_checker
@debug
def secret_key(*args, **kwargs):
    if kwargs.get("execution_mode") == Permissions.DRY_RUN:
        # dry run mode
        return "dummy_key"
    print("Fetching the secret key for you...")
    print(args[0])
    return secrets.token_hex(args[0] // 2) # random hex token


user_ark = User("ark")
user_cool = User("coolBoY")
user_no_acc = User("FlyingDragon")

try:    
    # we are passing these args to secret_key here
    # if we dont want to pass them further, we can pop them from kwargs in the decorator
    key = secret_key(32, user=user_ark, execution_mode=Permissions.EXECUTE)
    print(f"Your key: {key}... Bye {repr(user_ark)}")

    key = secret_key(48, user=user_cool, execution_mode=Permissions.DRY_RUN)
    print(f"Your key: {key}... Bye {repr(user_ark)}")

    key = secret_key(32, user=user_no_acc, execution_mode=Permissions.EXECUTE)
    print(f"Your key: {key}... Bye {repr(user_ark)}")
except AccessDenied:
    raise
finally:
    try:
        key = secret_key(48, user=user_cool, execution_mode=Permissions.EXECUTE)
        print(f"Your key: {key}... Bye {repr(user_ark)}")
        pass
    except AccessDenied:
        raise
