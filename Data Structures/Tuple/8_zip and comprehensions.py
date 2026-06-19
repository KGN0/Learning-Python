# The range() function
'''The range function represents an immutable sequence of numbers and is commonly used for looping a specific numbers of items in for loops'''
# Example
print(tuple(range(10)))
print(tuple(range(1, 11)))
print(tuple(range(1, 11, 2)))

# zip() function
'''
zip() is a built in function that takes two or more sequences and zips them into a list of tuples 
The tuples thus, formed has one element from each sequence'''
# Example 1
tup1 = (1,2,3,4,5)
lst1 = [i for i in 'abcde']
print(list(zip(tup1, lst1)))

# if length of sequence is different then the result has the length of shorter one
# Example 2
tup = (1,2,3)
lst = ['a', 'b', 'c', 'd', 'e']
print(list(zip(tup, lst)))


# comprehension in Tuples
'''
we use the same concept of the list comprehension to manipulate the values in one tuple to create a new tuple
'''
def double(Tup):
    return tuple([i * 2 for i in Tup])

Tup = 1,2,3,4,5
print('Original tuple:', Tup)
print('Double values:', double(Tup))