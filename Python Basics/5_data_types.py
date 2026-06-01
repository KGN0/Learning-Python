# Numbers
'''
- Number data types stores numeric values.
- A number also an immutable type, meaning that changing or updating its value results in a newly allocated object.
'''
# * Integers
''' Integers can be unlimited size'''
# Normal integers
print(-23)

# Octal literals
'''
A number prefixed by 0 and 'o' or 'O' will be interpreted as an' octal number
'''
a = 0o10
print(a) # a = 8

b = 0o123
print(b) # b = 83

# Hexadecimal Literals
'''
Hexadecimal literals have to be prefixed by 0x or 0X
'''
a = 0xA0F
print(a) # a = 2575

# Binary Literals
'''
Binary literals can be prefixed with 0b or 0B'''

x = 0b111
print(x) # x = 7

# conversions

y = hex(19)
print('y =',y) # 0x13

z = oct(8)
print('z =',z) # 0o10

x = bin(4)
print('x =',x) # 0b100


# Floating point numbers
''' A float is a real number that mean it can be rational and irrational'''
f = 17.3
print(f, 'is',type(f))

# Complex Numbers
'''
In python complex literals are written as real part + imaginary part
where the imaginary part is terminated with a j or J.
'''

# example
x = 3 + 4j
print('The variable x =', x, 'data type of x is', type(x))

# Boolean
'''
True and False are Boolean literals used in python 
we often need to know if an expression  is True or False.'''

x = True
print('the variable x =',x,'type of x is', type(x))

# None
'''
In python NOne keyword is an object which is equivalent to Null
'''

var = None
print('The variable var =', var, 'data type of var is', type(var))

# Strings
'''
- Strings are identified as group of characters represented in quotation marks
- Python allows both a pair of single and double quotes for writing strings
- Strings written in tripple quotes can span multiple lines of text
'''
print("Strings concepts")
# Example
s1 = 'Hello Python'
print('The string is', s1)

print('s1[0] output will be first character:',s1[0])
print('s1[0:5] output will be first five characters:', s1[0:5])

# identify data type of a variable
sname = "krishna"
print('type of "krishna"', type(sname))
print('type of "9.7"', type(9.7))

# Tuple 
'''
- A tuple contains a heterogeneous list of items separated by commas 
  and enclosed in parentheses.
- it can be best for records
- tuple objects are immutable means once created it can't be modified
'''
print("Tuple concepts")
tuple1 = (100, 200, 'hello', 456.789)
tuple2 = ('Hello', 'World')
print('Tuple1: ', tuple1)
print('Tuple2:',tuple2)
print('tuple1[0]:',tuple1[0]) # gives first value in the tuple1
print('tuple1 + tuple2:', tuple1 + tuple2)  # combines both tuples
# tuple1[0] = 30 gives error it not support assignment

# List
'''
A list contains item separated by commas and enclosed within square brackets 
A list in python can contain heterogeneous data types
List objects are mutable objects'''
print("List concepts")
list1 = [100, 'happy', 123.456, 'A']
print('list1: ', list1)
print('list1[0:2] ', list1[0:2]) # gives first two elements
print('list1 * 2 :', list1 * 2)


# Sets
'''
In python sets are unordered collections of objects enclosed in parenthesis and there are basically two types of sets'''

# Normal set: These are mutable and can be updated with new elements once sets are defined. duplicates are not allowed

print("Sets concepts")
flowers = {'Rose', 'Jasmine', 'Rose', 'Lilly', 'Rose'}
print('flowers set is:', flowers)
print('set(welcome) is', set('welcome')) # prints unique elements
set1 = set('welcome')
print("set1.add('z')", set1.add('z'))

# Frozen set: These set is immuatable and cannot be updated with new elements once frozenset sets are created

set2 = frozenset('Frozenset')
print('Frozenset: ', set2)
# set2.add('hhe') gives error because it is immutable


# Dictionary
'''
Dictrionary data type consists of key value pairs and it is enclosed in curly braces 
values ca be assigned and accessed using square brackets'''

print("Dictionary concepts")
capitals = {'india': 'new delhi', 'BA': 'washington DC'}
print(capitals)
print("capitals['BA']",capitals['BA'])