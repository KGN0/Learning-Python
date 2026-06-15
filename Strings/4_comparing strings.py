# Comparing strings
'''Python allows to compare strings using relational (or comparison) operators such as >, =>, <, <=, ==, != 
These operators compare the strings by using the lexicographical order i.e. using ASCII value of the characters.
The ASCII value of A-Z is 65-90 and ASCII code for a-z is 97-122
Eg: This means that book is greater than Book because the ASCII value of b is 98 and B is 66'''

# Example
s1 = 'Box'
s2 = 'Boy'
print(s1, s2)
if s1 == s2:
    print('Both the strings are same')
else:
    print("Both the strings are not same")

# Example
s1 = 'Bomb'
s2 = 'Bore'
print(s1, s2)
if s1 < s2: 
    print('s1 is less than s2')
else:
    print('s1 is greater than s2 or equal to s2')


# Iterating Strings
'''Strings is a sequence type(sequence of characters). You can iterate through the string using for loop as shown in the code given below'''
# Example: Program to iterate a givne string using loop
string = 'Welcome to python programming'
for char in string:
    print(char, end = " ")
print()

# Example: Program to iterate using while loop
string = 'Welcome to python programming'
i = 0
while i < len(string):
    print(string[i], end = " ")
    i += 1
print()

# Example (copy string uses character to iterate)
def copy(str1):
    new_str = ""
    for char in str1:
        new_str += char
    return new_str

str1 = input("\nEnter a string: ")
print('The copied string is:', copy(str1))

# The for statement can iterate over the items of a sequence:

lst = ['Joe', 'Hari', 'Praveen', 'Ganesh', 'Abhisek', 'Teja', 'Pavan']
for parent in lst:
    invitation = 'Hi ' + parent + '. Welcome to Python!'