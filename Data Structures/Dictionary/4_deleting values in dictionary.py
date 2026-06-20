# Deleting items in dictionary
'''
- An item can be removed from a dictionary using pop() method and this method removes a particular values  based on the key provided
- There is another method called popitem() which can be used to remove an item and it returns an arbitary item or key:value pair from the dictionary'''

# Example
d1 = {1:'Apple', 2:'Ball', 3:'Cat', 4:'Dog', 5:'Eagle'}
print('d1=', d1)
print('d1.pop(4):', d1.pop(4))
print('d1=', d1)

# using popitem()
print('d1.popitem()=', d1.popitem())
print(d1)

# using del keyword it used to remove individual elements or the entire dictionary
del d1[1] # delete a particular item
print(d1)

# using clear() this removes all items in the dictionary
d1.clear()
print(d1)

del d1
# print(d1) # raise NameError name d1 is not defined

