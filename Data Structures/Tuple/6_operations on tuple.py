# Operations on tuple
# slice operation on a tuple
'''Slice operation is used to access a range of elements from the tuple.
Colon (:) operator is used to perform slice operation.
A range of indices are used to specify where to start and where to end the range
Syntax: tuple_name[start:end:step]'''

# Example
tuple1 = (50, 60, 20 ,30, 10, 90)
print('tuple1=',tuple1)
print('tuple1[1:4]=', tuple1[1:4])
print('tuple1[:]=', tuple1[:])
print('tuple1[:5]=', tuple1[:5])
print('tuple1[2:]=', tuple1[2:])
print('tuple1[-4:-1]=', tuple1[-4:-1])
print('tuple1[::2]=', tuple1[::2])
print('tuple1[::-1]=', tuple1[::-1])

# Note
'''
1. Starting index is 0
2. In the range of indices, start index is included whereas end index is excluded
3. If start index is not mentioned, the range will start at the first item
4. If End index is not mentioned, the range will end at the last item
5. Negative indices are used to start the search from the end of the tuple
6. In negative indexing also, start index is included and end index is excluded
'''

# concatenation
'''Concatenation operation performs joining of two tuples into a single tuple.
Concatenation can be done using different ways'''
# 1. Using + operator
'''The use of + operator can easily and the whole of one tuple behind the other tuple and hence perfom the concatenation'''
tuple1 = (2, 4, 6, 8)
tuple2 = ('hello', 'python')
tuple3 = tuple1 + tuple2
print('tuple1=', tuple1)
print('tuple2=', tuple2)
print('concatinated tuple(tuple1 + tuple2)=', tuple3)

# 2. using * operator
tuple1 = (1, 4, 5, 6, 5)
tuple2 = (3, 5, 7, 2, 5)
print('tuple1=', tuple1)
print('tuple2=', tuple2)
print('*tuple1 , *tuple2=',(*tuple1, *tuple2, 99))

# 3. using sum()
print(sum((tuple1, tuple2), ()))

# 4. repetition of a tuple
# Example
t1 = (10, 20, 30)
print(2*t1)

# membership operators in tuple
'''This operation is used to test if an item exists in a tuple or not. "in" and "not in" operators are used to perform this membership operator
"in": is used to find whether an item is in a tuple. It returns True if the specified item is find in the tuple. False if an item is not in the tuple
"not in": is use to find whether an item is not in a tuple. It returns True if the specified item is not in the tuple. False if an item is in the tuple'''
# Example
tuple1 = ('p', 'y', 't', 'h', 'o', 'n')
print(tuple1)
print("'p' in tuple1", 'p' in tuple1)
print("'b' in tuple1", 'b' in tuple1)
print("'p' not in tuple1", 'p' not in tuple1)
print("'b' not in tuple1", 'b' not in tuple1)

# identity operators in tuple
'''"is" operator - Evaluates to true if the variables on ither side of the operator point to the same object and false otherwise'''
# Example 
x = ("xyznw", "college")
y = ("xyznw", "college")
z = x
print('x is z', x is z)
print('x is y:', x is y)

# Tuple assignment
# Tuple assignment is very popular feature in python. 
# It allows a type of variable on the left side of the assignment operator to be assigned values from a tuple given on the right side
# Tuple packing
a = ('python', 29, 'cs')
# Tuple unpacking
(name, age, subject) = a
print(name)

# Assigning multiple values
(a, b, c) = (10, 20, 30)
print(b)

# swapping values
a = 1
b = 3
print('a=', a, '\nb=', b)
a, b = b, a
print('a=', a, '\nb=', b)