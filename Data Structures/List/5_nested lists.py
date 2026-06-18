# Nested lists
'''Nested lists means a list with in another list
list has elements of different data types which can even include a list in the list'''
# Example
nested_list = [1,2,3, [1,2,3,4],0]
print('nested_list:', nested_list)
print('nested_list[3]:', nested_list[3])

# program to illustrate nested list
list1 = [1, 'b', 'abc', [2, 3, 4], 8.5]
print('list1=', list1)
i = 0
while i < len(list1):
    print('list1[', i,']=',list1[i])
    i += 1


# Cloning a list
'''If we want to modify a list and also keep a copy of the original list, then we should create a sperate copy of th elist
This process is called cloning'''

list1 = list(range(10))
list2 = list1
print('list1=', list1)
print('list2=', list2)
list3 = list1[2:7]
print('list3=', list3)