# Methods in dictionary
# len(dict_name)
'''Display the length of a dictionary'''
d1 = {x:x * x for x in range(1, 11)}
print('d1=', d1)
print('length of d1=', len(d1),'\n')

# str(dict_name)
'''Display the string representation of a dictionary'''
d2 = {x:x**3 for x in range(1, 11)}
print('d2=', d2)
print('str(d2)=', d2)

# type(dict_name)
# Gives the type of the variable
print('type(d2)=', type(d2),'\n')

# clear()
# Clears all elements of a dictionary
d3 = {x:y for x, y in d2.items() if x % 2== 0}
print('d3=', d3)
d3.clear()
print('After clearing d3=', d3,'\n')
del d3

# copy()
# creates a copy of existing dictionary
d3 = d1.copy()
print('After coping d1 to d3=', d3,'\n')

# fromkeys()
# creates a new dictionary with keys from the existing dictionary or sequence
d4 = dict.fromkeys(d1)  # default None
print('d4=', d4)
d4 = dict.fromkeys(d1, 'x')
print('d4=', d4)
d4 = dict.fromkeys('hello', 1)
print('d4=', d4)

# items()
# Returns a list of key, value pairs from the dictionary
print('\nd2=',d2.items())

# get()
# returns the value for a given key, otherwise returns False
print()
print('d3=', d3)
print('d3.get(5):', d3.get(5))

# keys()
# Returns only the keys from the dictionary
print('\nd3=', d3.keys())

# setdefault()
# Sets the default value for a key if it is not there in the dictionary
d1.setdefault(11,121)
print(d1)

# update()
# Updates a dictionary by taking key-values from an existing dictionary
d3.update(d2)
print('\nAfter updating d3.update(d2):')
print(d3)

# values()
# Returns a list of values existing in the dictionary
print('\nd1=',d1.values())