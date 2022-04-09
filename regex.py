# Regular Expressions
import re
"""
Meta and special characters:
[]  set of characters
\   escape special characters
.   any character except newline
^   starts with
$   ends with
*   zero or more occurrences
+   one or more occurrences
{}  exactly specified number of occurrences
|   either or
()  capture and group

\b  returns a match where the specified characters are present at the beginning or the end of the string
\s  returns a match where string contians a white space character
\S  returns a match where string doesnot contian a white space character
\w
\W  returns anything except letters and numbers i.e only spaces & period
\D  returns anything except numbers i.e letters, spaces and punctuations

findall()   returns a list of all matches
search()    returns a match object, if there is any match within the string, else returns None
match()
compile()
"""

# Need to heavily improve this guide here

str1 = "The ship set sail on the ocean"
str2 = "Ships set sail on the ocean to go places"

regex1 = '^[Tt]he'
regex2 = 'ocean$'
print(re.findall(regex1, str1))
print(re.findall(regex1, str2))
print(re.findall(regex2, str1))
# ['The']
# []
# ['ocean']

print(re.findall('\S', str2))
print(re.findall('\s', str2))
# ['S', 'h', 'i', 'p', 's', 's', 'e', 't', 's', 'a', 'i', 'l', 'o', 'n', 't', 'h', 'e', 'o', 'c', 'e', 'a', 'n', 't', 'o', 'g', 'o', 'p', 'l', 'a', 'c', 'e', 's']
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


print(re.findall('\W', str2))
print(re.findall('\D', str2))
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
['S', 'h', 'i', 'p', 's', ' ', 's', 'e', 't', ' ', 's', 'a', 'i', 'l', ' ', 'o', 'n', ' ', 't', 'h', 'e', ' ', 'o', 'c', 'e', 'a', 'n', ' ', 't', 'o', ' ', 'g', 'o', ' ', 'p', 'l', 'a', 'c', 'e', 's']

regex3 = '^The.*ocean$'
print(re.findall(regex3, str1))
# ['The ship set sail on the ocean']

# \b
x1 = re.findall(r'\bThe', str1)
x2 = re.findall(r'ocean\b', str1)
if x1:
    print("'The' is present at the beginning: ", x1)
else:
    print("'The' is not present at the beginning")
# 'The' is present at the beginning:  ['The']

if x2:
    print("'ocean' is present at the end: ", x2)
else:
    print("'ocean' is not present at the end")
# 'ocean' is present at the end:  ['ocean']

# search the string for this regex
# search all words starting with 'f' followed by any number (*) of characters from 'a to z'
print(re.findall(r'\bf[a-z]*', 'here is a foot of the fastest sandwich'))
# ['foot', 'fastest']








# ['The']
# []
# ['ocean']
# ['S', 'h', 'i', 'p', 's', 's', 'e', 't', 's', 'a', 'i', 'l', 'o', 'n', 't', 'h', 'e', 'o', 'c', 'e', 'a', 'n', 't', 'o', 'g', 'o', 'p', 'l', 'a', 'c', 'e', 's']
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# ['S', 'h', 'i', 'p', 's', ' ', 's', 'e', 't', ' ', 's', 'a', 'i', 'l', ' ', 'o', 'n', ' ', 't', 'h', 'e', ' ', 'o', 'c', 'e', 'a', 'n', ' ', 't', 'o', ' ', 'g', 'o', ' ', 'p', 'l', 'a', 'c', 'e', 's']
# ['The ship set sail on the ocean']
# 'The' is present at the beginning:  ['The']
# 'ocean' is present at the end:  ['ocean']
# ['foot', 'fastest']
