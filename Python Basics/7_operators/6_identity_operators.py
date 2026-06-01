# Identity operators
'''
The operators are used to compare the memory locations of two objects
Therefore it is possible to verify two objects are same or not
There are two identity operators'''

# is operator
'''
it is used to check the memory locations of two objects if they are same it return true otherwise false
'''
a = 100
b = 200
print(f'The id number of a is {id(a)}')
print(f"The id number of b is {id(b)}")
print(f'a is b: {a is b}')

# is not operator
'''
it is used to check the memory locations of two objects if they are same it return flase otherwise true
'''

print(f'a is not b: { a is not b}')

x = 1
y = 1
print(f'The id number of x is {id(x)}')
print(f"The id number of y is {id(y)}")
print(f'x is y: {x is y}')
print(f'x is not y: { x is not y}')
