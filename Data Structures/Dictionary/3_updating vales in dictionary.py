# Updating values in dictionary
# 1. Adding an item using subscript notation
'''To add a new entry or a key-value pair. In a dictionary, just specify the key value pair with out any existing key in dictionary
Syntax: dict_var[key] = val 
'''
# Example
dict1 = {'name': 'Swetha', 'course': 'M.Tech'}
print(dict1)
dict1['year'] = '2021'
print('After adding key-value pair:\n',dict1, sep="")

# 2. update() method
'''It will update the dictionay with the items from a given arguments 
If the item does not exist, the item will be added
The argument must be a dictionary, or an iterable object with key: value pairs
'''
# Example
dict1.update({'city':'Hyd'})
print('After adding key-value pair:\n',dict1, sep="")

# 3. using * operator
'''Using this method we can merge old dictionary and new key/value pair in anothe dictionary'''
dict2 = {'a':1, 'b':2}
new_dict = {**dict2, **{'c':3}}
print('dict2=', dict2)
print('dict2 after updating:', new_dict)

# changing a value in dictionary
dict3 = {'name':'Krishna', 'age':39}
print(dict3)
dict3['age'] = 40
print(dict3)

# changing the values and keys using zip() in dictionary
dict4 = {'hari':1, 'geeta':2}
print('original dictionary:',dict4)
list1 = [3, 4]
list2 = ['navya', 'gopi']
dict5 = dict(zip(list(dict4.keys()), list1))
print(dict5)
dict6 = dict(zip(list(dict4.values()), list2))
print(dict6)

a = (list(dict4.keys()))
a.extend(list2)
b = (list(dict4.values()))
b.extend(list1)
c = dict(zip(a,b))
print(c)