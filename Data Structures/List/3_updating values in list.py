# Updating values in the list
'''One or more elements of a list can be easily updated. In the updation we can add new values in the list and remove existing values from the list'''
# Example
x = [10, 20, 30, 50]
print('x =', x)
x[1] = 40
print('After updating x[1] = 40:', x)

# Using insert() method
# to insert a given element at given index
x.insert(3, 100)
print('After x.insert(3, 100):', x)

# Using append method
# add another element or list of element at end of the list
x.append(23)
print('After x.append(23):', x)

# Changing all values using loops
list_of_no = [10, 20, 30, 40, 50, 60]
print('Original list:\n', list_of_no) 
for i in range(len(list_of_no)):
    list_of_no[i] += 2

print('After incrementing each element of list by 2:\n', list_of_no)