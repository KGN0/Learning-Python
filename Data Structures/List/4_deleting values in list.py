# Deleting values in list
'''The del statement is mainly useful to delete the elements in the list
or to delete specified elements in list or to delete entire list'''

# To delete single element
list1 = [1, 2, 3, 4, 5]
print('Original list:\n', list1)
del list1[1]
print('After deleting element at index 1 is:\n', list1, '\n')

# Using remove() method:- removes the first matching element from the list, it throws error if element is not in list
prime_nums = [2, 3, 5, 7, 9, 11]
print(prime_nums)
prime_nums.remove(9)
print('after removing 9 from the list:\n',prime_nums, sep="" )