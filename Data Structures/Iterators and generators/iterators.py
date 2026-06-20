# Iterables
''' An iterable is something that can be looped over.
    The process of looping over something, of taking each item of it, one after another, is iteration.'''

# Example
num_list = [1,2,3,4,5]
for num in num_list:
    print(num)
# To be an iterable, an object will have an iter() method. So if an object has an iter() method, then it is an iterable
# to check iter() method is supoort or not write dir(num_list or variable name)
print(dir(num_list))
if '__iter__' in dir(num_list):
    print(True)
else:
    print(False)

# calling iter() function on an iterable gives us an iterator
# calling the next() function on iterator gives us the next element
# if the iterator is exhausted(if it has no more elements), calling next() raises the StopIteration exception

# Iterators
# iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets
# 1. __iter(iterable)__ method that is called for initialization of an iterator this method returns an iterator object
# 2. next() the next method returns the next value for the iterable. when we use for loop to traverse any iterable object, 
#    internally it user the iter() method

# Example
list1 = [1,2,3,4,5,6]
number_iterator  = iter(list1)
print(type(number_iterator))
print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))