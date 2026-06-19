# Updating values of tupel
'''As we know typles are immutable in nature. So if we want to update the values,
    or if you want to change the values in tuples, we cannot able to change the values  in tuple 
    and also there is no way of updating values in tuple'''

# Example
x = (10, 20, 3, 5)
#x[1] = 15  # TypeError: 'tuple' object does not support item assignment
print(x)

# Alternative solution: 1. change the tuple into list, 2. update the list, 3. change back list to tuple
tuple1 = (5, 3, 3, 2, 6)
print(tuple1)
list1 = list(tuple1)
list1[3] = 8
tuple1 = tuple(list1)
print(tuple1)