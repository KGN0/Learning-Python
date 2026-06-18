# different ways to printing lists in python
# 1. Using loop
'''One can traverse the list from index 0 to len(list) and prints the items of the list using for loop'''
# Example
lst1 = [10, 20, 30, 40, 50]
for i in range(len(lst1)):
    print(lst1[i], end = " ")

# 2. without using loop
'''The symbol * is used to print the items of list in a single line separated by space. One can also use newline or comma to separate the list of items'''
list1 = [23, 45, 12, 65, 78, 92]
print(*list1, sep=',')
print(*list1, sep='\n')

# 3. converstion of list to a string for display
list1 = ['welcome', 'to', 'python']
list2 = " ".join(list1)
print(list2)