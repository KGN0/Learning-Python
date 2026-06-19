# Methods in tuple
# tuple_name.count(element)
'''Count the occurrence of a particular element in a tuple'''
# Example
t1 = (12, 1, 2, 3, 1, 4, 1, 3, 9, 4, 3, 1)
print('t1=', t1)
print('count of 1:', t1.count(1))
print('count of 3:', t1.count(3))

# len(tuple_name)
'''Gives the length of the tuple'''
print('length of t1:', len(t1))

# max(tuple_name)
'''Returns the element with maximum value from tuple'''
print('maximum element from t1:', max(t1))

t2 = ('f', 'g', 'd', 'n')
print('t2=', t2)
print('maximum of t2:', max(t2))

# min(tuple_name)
'''Returns the element with minimum value from tuple'''
print('minimum element from t1:', min(t1))

t2 = ('f', 'g', 'd', 'n')
print('t2=', t2)
print('minimum of t2:', min(t2))

# tuple_name.index(element)
'''Returns the index of the element in a tuple'''
print('index of 9 in t1:', t1.index(9))

# any(iterable)
'''Returns True if any element of an iterable is True'''
print('any(t1):', any(t1))
t3 = ()
print('any(t2):', any(t2))
print('any(t3):', any(t3))

# all(iterable)
'''Returns True if all elements in a given iterable are True, otherwise returns False'''
print('all(t1):', all(t1))
print('all(t2):', all(t2))
print('all(t3):', all(t3))
t4 = ('0', 0, False, True, 23, 89)
print('t4=', t4)
print('all(t4):', all(t4))

# sorted(tuple_name)
# gives a sorted list from a given tuple
print('Sorted list of t1:', sorted(t1))

# sum(tuple_name)
# Returns the sum of elements of a tuple
print('Sum of elements of t1:', sum(t1))

# tuple()
'''Creates a tuple from a list, string and a dictionary'''
t5 = tuple()
print('t5=', t5)

t6 = tuple('Python')
print('t6=', t6)

t7 = tuple({'A':'Apple', 'B':'Banana'})
print('t7=', t7)

# reversed(tuple_name)
'''Retrns a list after reversing the sequence of a tuple'''
print('reversed list of t1:', reversed(t1))

# bool(tuple_name)
'''Returns True if the tuple is not empty, otherwise returns False'''
print('bool(t3):', bool(t3))
print('bool(t4):', bool(t4))

