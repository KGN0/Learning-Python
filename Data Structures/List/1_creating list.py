# List
''' Lists are one of the most powerful and frequently used data type in python.
    It is the most versatile data type available in python, we can be written as
    a list of comma-seperated values between square brackets.
    List need not contain homegenous elements
Syntax: List_variable = [var1, var2, var3,....]'''

# Creation of list
'''There are different methods to create list'''
# creating an empty list
a = []
print(a)

# creating empty list using list()
b = list()
print(b)

# creating list with given elements
c = [1, 2, 3, 4, 5]
print(c)

d = [1, 'one', 2, 'two', 3, 'three']
print(d)

# creating list from another sequence
e = list('Python')
print(e)

f = list((1, 2, 'True', 3.14))
print(f)

g = list(f)
print(f)