# Run code on Pycharm via Control + R (^R)

# Overview of the numbers, data types, arithmetic operations
print(2 + 2)
print(5 - 4 * 3)
print(8 / 5)  # division always return a floating point number
print(2 ** 7)  # two to the power seven
# \'  \"  \n: escape sequences
print('dosen\'t and' + " dosen't")
print("Welcome to Coding in Python.\n This is Great!")
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote means raw strings

# Character manipulation from String
word = "Tatte short"
print(word[0])  # T
print(word[6])  # s
print(word[-1])  # t (Last Character)
print(word[-4])  # h  (4th Last Character)
# slicing
print(word[0:2])  # characters from index 0 to 1 (0 to n-1)
print(word[3:6])  # characters from index 3 to 5: te_
# word[:i] + word[i:] = word [start is always included, end is always excluded]
print(word[:2] + word[2:])  # Tatte short
print(word[:4])  # Tatt [characters from beginning to index n-1=3]
print(word[5:])  #  short [characters from index 4(start always included) to end]
print(word[-3:])  # ort  [characters from third-last (included) to end]

# +---+---+---+---+---+---+--+
#  | P | y | t | h | o | n |
# +---+---+---+---+---+---+--+
#    0   1   2   3   4   5
#   -6  -5  -4  -3  -2  -1

print(len(word))  # length of the word is 11

# formatted string literals (F-strings): used to embed expressions inside string literals
print(f"This is a f-string, attaching the greatest string: {word}")
# str.format()
print("This is a f-string, attaching the greatest string: {} ".format("word"))
print("Test string {val1}, {val2} is here1".format(val1="sucker", val2="dumb"))


# Outputs for this python script
# 4
# -7
# 1.6
# 128
# dosen't and dosen't
# Welcome to Coding in Python.
#  This is Great!
# C:\some
# ame
# C:\some\name
# T
# s
# t
# h
# Ta
# te
# Tatte short
# Tatt
#  short
# ort
# 11
# This is a f-string, attaching the greatest string: Tatte short
# This is a f-string, attaching the greatest string: word
# Test string sucker, dumb is here1
