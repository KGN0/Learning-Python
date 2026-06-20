# Set
''' Set is an unordered collection of data like numbers, words, alphabets, other sets etc
    and it is based on a data structure called hash table
    The concept of set is a replica of mathematical notation of a set
    The set elements are placed within a pair of curly braces
    There are two types of sets 1. Normal sets 2. Frozen sets'''

# Creating set using set()

x = set('Python')
print('x=', x)
y = set([10, 20, 'hello', 'hai', 10, 'x', 'y', 'z'])
print('y=', y)
z = set((10, 20, 30, 20, 10))
print('z=', z)

# Accessing the Elements of a set

print('Elements in set:')
for elmt in y:
    print(elmt)
else:
    print()

# Modifing a set 

# sets are mutable. However, since they are unordered, indexing has no meaning
# We can add a single element using the add() method, and
# multiple elements using the update(), which takes takes tuples, list, strings or other sets as it argumets
# Note we cannot access or change an element of a set using indexing or slicing
# Example
my_set = {1, 3}
print('my_set=',my_set)
# my_set[0] # TypeError: 'set' object does not support indexing
my_set.add(2) # Adding element to the set
print('After adding element')
print('my_set=',my_set)

# Removing an element from a set

# A particular element is removed from a set using the methods discard() and remove()
# Example
my_set = {1,7, 13, 5,4,9}
print('my_set=', my_set)
my_set.discard(1)
my_set.discard(1) # don't raise error
print('my_set=', my_set)
my_set.remove(7)
print('my_set=', my_set)
# my_set.remove(7) # Raise error
print('my_set=', my_set)
