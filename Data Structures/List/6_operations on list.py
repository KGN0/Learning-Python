# Operations on list
# slice operation on a list
'''Slice operation is used to access a range of elements from the list.
Colon (:) operator is used to perform slice operation.
A range of indices are used to specify where to start and where to end the range
Syntax: list_name[start:end:step]'''

# Example
lst = [50, 60, 20 ,30, 10, 90]
print('lst=',lst)
print('lst[1:4]=', lst[1:4])
print('lst[:]=', lst[:])
print('lst[:5]=', lst[:5])
print('lst[2:]=', lst[2:])
print('lst[-4:-1]=', lst[-4:-1])
print('lst[::2]=', lst[::2])
print('lst[::-1]=', lst[::-1])

# Note
'''
1. Starting index is 0
2. In the range of indices, start index is included whereas end index is excluded
3. If start index is not mentioned, the range will start at the first item
4. If End index is not mentioned, the range will end at the last item
5. Negative indices are used to start the search from the end of the list
6. In negative indexing also, start index is included and end index is excluded
'''

# concatenation
'''Concatenation operation performs joining of two lists into a single list.
Concatenation can be done using different ways'''
# 1. Using + operator
'''The use of + operator can easily and the whole of one list behind the other list and hence perfom the concatenation'''
list1 = [2, 4, 6, 8]
list2 = ['hello', 'python']
list3 = list1 + list2
print('list1=', list1)
print('list2=', list2)
print('concatinated list(list1 + list2)=', list3)

# 2. using * operator

list1 = [1, 4, 5, 6, 5]
list2 = [3, 5, 7, 2, 5]
print('list1=', list1)
print('list2=', list2)
print('*list1 , *list2=',*list1, *list2)

# 3. using append()
list1 = [1, 4, 5, 6, 5]
list2 = [3, 5, 7, 2, 5]
for i in range(len(list2)):
    list1.append(list2[i])

print('Concatinated list using append=', list1)

# 4. using extend()
list1 = [1, 4, 5, 6, 5]
list2 = [3, 5, 7, 2, 5]
list1.extend(list2)
print('concatinated list using list1.extend(list2):', list1)

# membership operators in list
'''This operation is used to test if an item exists in a list or not. "in" and "not in" operators are used to perform this membership operator
"in": is used to find whether an item is in a list. It returns True if the specified item is find in the list. False if an item is not in the list
"not in": is use to find whether an item is not in a list. It returns True if the specified item is not in the list. False if an item is in the list'''
# Example
list1 = ['p', 'y', 't', 'h', 'o', 'n']
print(list1)
print("'p' in list1", 'p' in list1)
print("'b' in list1", 'b' in list1)
print("'p' not in list1", 'p' not in list1)
print("'b' not in list1", 'b' not in list1)

# identity operators in list
'''"is" operator - Evaluates to true if the variables on ither side of the operator point to the same object and false otherwise'''
# Example 
x = ["xyznw", "college"]
y = ["xyznw", "college"]
z = x
print('x is z', x is z)
print('x is y:', x is y)