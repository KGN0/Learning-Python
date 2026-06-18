# Methods in List
# list_name.append(element)
'''Adds an item to the end of the list'''
# Example
list1 = ['welcome', 'to']
list1.append('python')
print(list1)

list2 = [2, 4, 9.0, 32, 23]
list2.append(49)
print(list2)

list1.append(list2)
print(list1)

# list_name.insert(index, element)
'''This method is used to insert an elements at specified position. But the position mentioned should be within the range of list
    otherwise it would throw IndexError
Syntax: list_name.insert(position, element)'''
# Example
lst = ['Apple', 'Cherry', 'Banana', 'Mango']
lst.insert(2, 'Watermelon')
print(lst)

# list1_name.extend(list2_name)
'''this method is used to extend the contents of list1 by adding the contents of list2 at the end of list1 
Syntax: list1.extend(list2)'''
# Example 
lst1 = ['Apple', 'Cherry', 'Banana', 'Mango']
lst2 = [10, 20, 30, 40]
lst1.extend(lst2)
print(lst1)

# list_name.index(element)
'''This method returns the index of first occurrence of element. One can also mention the start and end, but not mandatory parameters
Syntax: List.index(element[,start[,end]])'''
# Example
lst1 = [5, 15, 25, 5, 15, 55, 15, 5, 25]
print(lst1.index(15))
print(lst1.index(15, 2, 6))

# list_name.sort()
'''This method is used to sort the list elements in ascending order.
The parameters key and reverse_flag are not necessary parameter and if nothing is passed through sorted()
method then reverse_flag is set to False
Syntax: sorted(list_name, key= myfunc, reverse = true/false)
        list_name.sort(reverse = true/false, key= myfunc)'''

# Example
lst1 = [5.5, 55.5, 14.32, 242,24, 20]
lst1.sort()
print(lst1)
lst1.sort(reverse=True)
print(lst1)

lst2 = [4, 2,56, 24, 63,90]
print(sorted(lst2))

# pop(index)
'''This method is used to pop or remove an element from a list. Here parameter index is not a nexessary parameter 
    but if it is not mentioned, it takes the last index. The index number must be in range of the list, otherwise it shows IndexError
Syntax: list.pop([index])'''

# Example
lst1 = [55.5, 100, 87, 92, 'Ram', 'Abdul', 35, 75.75, 12.65]
print(lst1)
print('poped element:',lst1.pop())

print('poped element at second index:',lst1.pop(2))

# del(index)
'''This method is used to deleter an element from a list at a particular index
Syntax: del list_name[index]'''
# Example
lst1 = [55.5, 100, 87, 92, 'Ram', 'Abdul', 35, 75.75, 12.65]
del lst1[5]
print(lst1)

# list_name.remove(element)
'''This method is used to remove an element by mentioning the element in the list
Syntax: list_name.remove(element)'''
# Example
lst1 = [55.5, 100, 87, 92, 'Ram', 'Abdul', 35, 75.75, 12.65]
lst1.remove('Ram')
print(lst1)

# list_name.clear()
'''This method is used to clears all items from the list
Syntax: List.clear()'''
# Example
lst1 = [10, 20, 30, 40, 50]
lst1.clear()
print('cleared list:',lst1)

# list_name.count(element)
'''This method is used to calculate the total occurrence of given element in a list
Syntax: list_name.count(element)'''
# Example: 

lst1 = [10, 30, 20, 40, 10, 30, 70, 10]
print(lst1)
print('lst1.count(10)=', lst1.count(10))

# len(list_name)
'''This method is used to calculate the length of the list
Syntax: len(list_name)'''
# Example
lst1 = ['Hello', 'world', 'these', 'are', 'the', 'python', 'methods']
print(lst1)
print('len(lst1)=', len(lst1))

# list_name.copy()
'''This method is used to create a copy of the existing list
Syntax: copy(list_name)'''

# Example
lst1 = [10, 'ten', 20, 'twenty']
lst2 = lst1.copy()
print('copied list:',lst2)

# sum(list_name)
'''This method is used to calculate the sum of all the elements of a list. 
Sum is calculated only for numeric values, otherwise it throws TypeError
Syntax: sum(list_name)'''
# Example
lst1 = [10, 30, 20, 40, 10, 30, 70, 10]
print(lst1)
print('sum(lst1)=', sum(lst1))

lst2 = [10, 'ten', 20, 'twenty']
# print(sum(lst2)) throws error

# min(list_name)
'''This method is used to calculate the minimum of all the elements in a list
Syntax: min(list_name)'''
# Example
lst1 = [25,364,75,35,86,24,121]
print(lst1)
print('min(lst1)=', min(lst1))

# max(list_name)
'''This method is used to calculate the maxmimum of all the elements in a list
Syntax: max(list_name)'''
print('max(lst1)=',max(lst1))