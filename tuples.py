# Tuples are a collection of items which are ordered[indexed] and unchangeable, allowing duplicates
# Items cannot be changed, removed, added after a tuple is created
myTuple = ('ark', 'chauhan', 'great')
print(myTuple)  # ('ark', 'chauhan', 'great')
print(myTuple[0] + " " + myTuple[1])  # ark chauhan
print(len(myTuple))  # 3

#  If you want a tuple with a single item add a comma after the definition
tuple1 = ("hey",)
tuple2 = ("hey")
print(type(tuple1))  # <class 'tuple'>
print(type(tuple2))  # <class 'str'>

#  empty tuple
emptyTuple = ()
print(emptyTuple)  # ()

# iterating through tuple
for x in myTuple:
    print(x)
# ark
# chauhan
# great
