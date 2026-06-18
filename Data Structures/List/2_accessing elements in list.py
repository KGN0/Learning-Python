# Accessing Elements of a list
'''
- List index: index operator [] can be used to access an element in a list and by default index starts from 0.
- If the user tries to access an element outside index then this will raise an IndexError.
- The index must be an integer and usage of float or other types will raise a TypeError
- There are two types of indexing i.e. 1. Positive indexing, 2. Negative indexing'''

# Positive indexing: It starts from left. First item index is 0, last element of list of n item is (n - 1)

list_name = ['P', 'y', 't', 'h', 'o', 'n']
print('list_name =', list_name)
print('list_name[0] =', list_name[0])
print('list_name[3] =', list_name[3])
print('list_name[5] =', list_name[5])
# print('list_name[10] =' list_name[10])  - IndexError: list index out of range

# Negative indexing: It begin from right i.e., from the end -1 refers to the last item, -2 refers to the second last item etc
print("\nlist_name =", list_name)
print('list_name[-1] =', list_name[-1])
print('list_name[-5] =', list_name[-5])
print('list_name[-6] =', list_name[-6])

