# Deleting values in tuple
'''Since tuple is an immutable object we cannot delete values from it'''
# Example
x = ('python', 100, 34)
print(x)
# del x[2] # raise TypeError: tuple object doesn't support item deletion
del x
# print(x) # raise NameError: name x is not defined

# Alternative
tuple1 = (3,5,3,3,7,5,1,7,8)
print(tuple1)
list1 = list(tuple1)
list1.remove(3)
tuple1 = tuple(list1)
print(tuple1)

# Traversing tuple
my_tuple = tuple('python')
for item in my_tuple:
    print(item)
print()
# or
for i in range(len(my_tuple)):
    print(my_tuple[i])