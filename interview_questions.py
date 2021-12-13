# Generic Python based interview questions for better understanding
# Not thinking of the TC/SC rn : just better python understanding
# For complexity based questions, refer to DSA directory

# Remove Duplicates from list
l1 = [1, 1, 1, 3, 5, 6, 5, 9, 45, 34, 2, 2]
print(set(l1))  # set only has  non-duplicate elements: {1, 34, 3, 2, 5, 6, 9, 45}
l1 = list(set(l1))
print(l1)  # [1, 34, 3, 2, 5, 6, 9, 45]


# Check if the string is a palindrome
string = "dad1"
reverse_string = string[len(string)::-1]  # or reverse by reverse_string = string[::-1]
print(reverse_string)   # 1dad
print(string == reverse_string)  # False

# Get Missing number in [1..100]



# Compute the first n fibonacci numbers
