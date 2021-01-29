# lambda arguments: expression

add10 = lambda x: x+10
print(add10(50)) #60

# above lambda function is equivalent to this function

def add10_func(x):
    return x+10


mult = lambda x,y: x*y
print(mult(3,7)) #21

# next example:: sorted function
points2D = [(1,2), (15,1), (5,-1), (10,4)]
print(points2D[0])
print(points2D[0][0])
print(points2D[0][1])
# (1, 2)
# 1
# 2


points_2Dsorted = sorted(points2D)

print(points2D)
print(points_2Dsorted)
# output sorted by x coordinate
# [(1, 2), (15, 1), (5, -1), (10, 4)]
# [(1, 2), (5, -1), (10, 4), (15, 1)]

# sort by y index:
points_2Dsorted_y = sorted(points2D, key= lambda x: x[1])
print(points_2Dsorted_y)
# [(5, -1), (15, 1), (1, 2), (10, 4)]

points_2Dsorted_other = sorted(points2D, key= lambda x: x[0] + x[1])
print(points_2Dsorted_other)
# [(1, 2), (5, -1), (10, 4), (15, 1)]
# [3, 4, 14, 16] ^^



# ----------------------------------
a =[1,2,3,4,5]

print(a)
# print(a+5)
print(a*5)

# [1, 2, 3, 4, 5]
#     print(a+5)
# TypeError: can only concatenate list (not "int") to list
# [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# ----------------------------------
# next example :: map function
# map(func, iterable seq)
# aim: is to get a list with *2 values of a
b= map(lambda x:x*2, a)
print(b)
print(list(b))
# <map object at 0x100827bb0>
# [2, 4, 6, 8, 10]

# same functionaliy can be achieved via list comprehension
c = [x*2 for x in a ]  
print("double c:", c)


# ----------------------------------
# next example :: filter
# filter(func, iterable seq)
# aim: is to find only the even numbers in the list a
b= filter(lambda x: x%2 == 0, a)
print(b)
print(list(b))

#  the same functionality can be achieved by the list comprehension
c = [x for x in a if x%2 == 0]
print(c) 
# ----------------------------------
