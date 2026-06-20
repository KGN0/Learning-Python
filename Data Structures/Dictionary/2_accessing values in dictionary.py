# Accessing values in dictionary
'''To access values in dictionary square brackets are used along with the key to obtain its value'''
# 1. to print entire dictionary elements
dict1 = {'name':'Swetha', 'course':'M.Tech'}
print('dict1=', dict1)

# 2. To access specified elements in the dictionary by using key value
print("dict1['name']=", dict1['name'])

# 3. using get() method to access
print(dict1.get('course'))

# 4. if we try to access the element which is not present dictionary it throws error
# print(dict1['adress']) # throws KeyError

# 5. keys() method will return a list of all the keys in the dictionary
print('dict1.keys()=', dict1.keys())
print(list(dict1.keys()))
# 6. values() method will return a list of all the values in the dictionary
print('dict1.values()=', dict1.values())
print(list(dict1.values()))

# 7. items() method will return each item in a dictionary, as tuples in a list.
print('dict.items()=', dict1.items())
print(list(dict1.items()))