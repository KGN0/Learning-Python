# Sets Methods

set_A = {10, 20, 30, 40, 50}
set_B = {30, 20, 60, 80}
print('set_A=', set_A)
print('set_B=', set_B)
# 1. set union: union of A and B is a set of all elements from both sets.
#    Union is performed using | operator or union() method
print('set_A.union(set_B):',set_A.union(set_B))

# 2. set intersection: intersection of A and B is a set of elements that are common in both the sets.
#    intersection is performed using & operator or interesection() method
print('set_A.intersection(set_B):', set_A.intersection(set_B))

# 3. set difference: difference of the set B from set A(A - B) is a set of elements that are only A but not in B
#    difference is performed using - operator or difference() method
print('set_A.difference(set_B):', set_A.difference(set_B))

# 4. set symmetric difference: symmetric difference of A and B is a set of elements in A and B but not in both
#    it is performed ^ operator or symmetric_difference() method
print('set_A.symmetric_difference(set_B):', set_A.symmetric_difference(set_B))

# 5. issubset(): this method returns True if another set contians this set
print('set_A.issubset(set_B):',set_A.issubset(set_B))

# 6. issuperset(): this method return True if this set contains another set
print('set_A.issuperset(set_B):',set_A.issuperset(set_B))

# 7. isdisjoint(): this method returns True if two sets have a null intersection
print('set_A.isdisjoint(set_B):',set_A.isdisjoint(set_B))

# 8. set membership test: this method is used to test if an itme exist in a set or not using set membership operator in.
print('10 in set_A:', 10 in set_A )
print('100 in set_A:', 100 in set_A )



# Other set methods
# 1. add and update()
'''The add() method is used to add an element to a set. Multiple data elements can be added by using update() method
    The update() method can take tuples, lists, strings or sets as its argument. But in all cases duplicates are avoided'''
my_set = {10, 20, 30, 40, 30, 20}
print('Original set:', my_set)
my_set.add(50)
print('After adding single element:', my_set)
my_set.update({60, 70, 80})
print('After adding multiple elements:')
print(my_set)


# 2. remove(), discard(), pop(), and clear()
'''Both the remove() and discard() methods used to remove a particular item from a set
    - remove() method will raise an error if element is not present in the set. while discard() is not

   pop() method can also remove and return an item which is arbitary
   clear() method is used to remove all the elements from a set'''

# Example
my_set = {10, 20, 30, 40, 50}
print('original set:', my_set)
my_set.remove(10)
print('After removing element 10:', my_set)
my_set.discard(30)
print('After discard element 30:', my_set)
my_set.discard(10)
print('After discard element 10:', my_set)
# my_set.remove(10)         # raise KeyError
# print('After removing element 10:', my_set)

p = my_set.pop()
print('After removing arbitary element:', p)

my_set.clear()
print('After removing all elements:',my_set)

# 3. copy() 
'''This method returns a copy of the set'''
set_A = {10, 20, 30, 40, 50}
set_B = set_A.copy()
print(set_B)