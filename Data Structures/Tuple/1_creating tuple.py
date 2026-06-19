# Tuple
'''
A tuple is a linear data structure in python, the elements in tuple can be stored in sequence order.
A tuple is a collection of objects which are ordered and immutable
Properties of a Tuple
- The list is immutable, ie., not changeable.
- It allows duplicate members
- It can have any number of items
- There may be of differnt types like integer, float, string etc.,
- Index of list start at 0
- The elements in a list are ordered

Syntax: tup = (val1, val2, val3,...)'''

# Creating a tuple
'''Items are separated by commas. These comma-separated values can be between parentheses also(optional)'''
t1 = () # empty tuple
print('t1=',t1)

t2 = 'Python', 'programming'    # without using paranthesis
print('t2=',t2)

t3 = ('Rama', 'Hari', 'John', 2018, 234.5) # with using paranthesis
print('t3=',t3)

t4, t5 = (12, 32, 'abc'), ('xyz', 45, 68)  # creating multiple tuples in a single line
print('t4=', t4, '\nt5=', t5)