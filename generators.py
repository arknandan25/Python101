# A simple generator
def multiply(n):
    while True:
        state = n * 3
        yield state

x = multiply(4)
import ipdb
ipdb.set_trace()
print(next(x))
# <generator object multiply at 0x7fa1bc854620>
