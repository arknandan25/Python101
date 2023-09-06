#!/usr/bin/env python3
# Queue implemetation as List
# FIFO
queue = []

queue.append("a")
queue.append("b")
queue.append("c")
queue.append("d")
queue.append("e")

# 0 1 2 3 4
# a b c d e
# in queue popping happens at the front - dequeue

print(f"Original queue: {queue}")

queue.pop(0) # at front
print(f"Popped queue: {queue}")

queue.pop(0)
print(f"Popped queue: {queue}")

# Original queue: ['a', 'b', 'c', 'd', 'e']
# Popped queue: ['b', 'c', 'd', 'e']
# Popped queue: ['c', 'd', 'e']


# Enqueue will happen with queue.append(val) <- at the end



# Stack + Queue implemetation with Deque (Deck) ~ Double ended Queue Library
# Deque can perfrom operation on both left (front) and right (rear)
# means as a stack it can append and pop elements from rear (end)
# as a queue it can popleft -> remove first element from itself
from collections import deque

queue2 = deque()

queue2.append(1)
queue2.append(2)
queue2.append(3)

print(f"Original queue2: {queue2}")

queue2.popleft() # at front
print(f"Popped queue2: {queue2}")


stack2 = deque()

stack2.append(1)
stack2.append(2)
stack2.append(3)

print(f"Original stack2: {stack2}")

stack2.pop() # at end
print(f"Popped stack2: {stack2}")

# Original queue2: deque([1, 2, 3])
# Popped queue2: deque([2, 3])
# Original stack2: deque([1, 2, 3])
# Popped stack2: deque([1, 2])