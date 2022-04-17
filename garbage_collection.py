"""

Garbage collection

Base don reference count

"""
import weakref

b = 9  # creates an object like: obj(9) and b is a ref to this object, so ref_cnt for this obj =1
b = 7  # ref_cnt(obj(9)) = 0 as b is no longer pointing to it, garbage collection kicks in and that memory is freed up
#  ref_cnt(obj(7)) = 1
#  b is a reference or a pointer as called in C


class Car:
    def __init__(self, w):
        self.w = w


c1 = Car(44)  # ref_cnt(Car(44)) = 1
print(hex(id(c1)))
wr = weakref.ref(c1)  # GC doesn't keep count of such references, i.e ref_cnt(Car(44)) is still 1
print(hex(id(wr)))
print(wr)
c1 = None  # ref_cnt(Car(44)) = 0 <- GC is invoked
print("After GC invoked:", wr)
# 0x7f823acc17f0
# 0x7f823aa32c28
# <weakref at 0x7f823aa32c28; to 'Car' at 0x7f823acc17f0>
# After GC invoked: <weakref at 0x7f823aa32c28; dead> <- memory reclaimed by GC



c = 69
d = 69
print(id(c))
print(id(d))
print(id(c) == id(d))
# 4489915808
# 4489915808
# True

for i in range(0, 3):
    print("Id of 5:", id(5))
# Id of 5: 4467443104
# Id of 5: 4467443104
# Id of 5: 4467443104

"""
But when the same program is run next time the o/p is : 
Id of 5: 4478330272
Id of 5: 4478330272
Id of 5: 4478330272

this means id gives us the addr of an object in memory
basic data types like int, str will have the same addr assigned to it during one execution of a program
the memory addr assigned to it during next execution will change
"""


class Test:
    def __init__(self, a):
        self.a = a

    def pp(self):
        print(self)

#  t1 and t2 are 2 diff objects even though we send same value for a
t1 = Test(12)
t2 = Test(12)
t1.pp()
t2.pp()
print(t1 == t2)
# <__main__.Test object at 0x7f9774dc1780>
# <__main__.Test object at 0x7f9774dc17b8>
# False
t3 = t1
t3.pp()
print(t3 == t1)
# <__main__.Test object at 0x7fcca9bc1780>
# True
