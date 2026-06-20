# Dictionary
'''
A dictionary is a Non-linear data structure where all the elements are not arranged in the sequenced order.
The dictionary stores the elements in the form of key and value pairs
- Each key in dictionary is separated with colon(:)
- A dictionary can hold different data types elements.
- Dictionaries are represented with flower brackets{}
Syntax: dict1 = {'key1':'value1', 'key2':'value2', 'key3':'value3',..., 'keyn':'valun'}

properties of dictionary keys
- dictionary values have no restrictions.
- They can be any arbitary python object, either standard objects or user-defined objects
- However, same is not true for the keys. There are two points to remember about dictionary keys
'''
# creating dictionary
# Example
d1 = {}         # creates an empty dictionary
d2 = dict()     # another way to create empty dictionary
print('d1=', d1)
print('d2=', d2)

d1['A'] = 'Apple'
d1['B'] = 'Ball'
d1['C'] = 'Cat'

print('d1=', d1)

print('d1.keys()=', d1.keys())       # prints only keys
print('d1.values()=', d1.values())   # prints only values

print("'A' in d1:", 'A' in d1)       # check if a key exists in dictionary
print("'D' in d1:", 'D' in d1)

del d1['B']
print("'B' in d1:", 'B' in d1) 