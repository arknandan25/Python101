#!/usr/bin/env python3
# Stack implemetation as List
# LIFO
stack = []

stack.append("a")
stack.append("b")
stack.append("c")
stack.append("d")
stack.append("e")

# 0 1 2 3 4
# a b c d e
# top=4 = len(stack) - 1
# push op will be after 4, pop op will be at 4

print(f"Original Stack: {stack}")

stack.pop()
print(f"Popped stack: {stack}")

# top=3
stack.pop()
print(f"Popped stack: {stack}")

# Original Stack: ['a', 'b', 'c', 'd', 'e']
# Popped stack: ['a', 'b', 'c', 'd']
# Popped stack: ['a', 'b', 'c']