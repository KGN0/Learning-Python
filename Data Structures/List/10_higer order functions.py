# Accessing elements in list
# enumerate(list_name)
'''
This is used when you want to print both index as well as an item in the list
The enumerate() function returns an enumerate object which contains the index and value of all the items of the list as a tuple'''

# Example
num_list = [i for i in range(2, 21, 2)]
for item in enumerate(num_list):
    print(item)
# or
for i, value in enumerate(num_list):
    print(f'{value} at index {i}')

# range()
'''The range() function represents an immutable sequence of numbers and is commonly used for looping a specific numbers of times in for loops'''
print(list(range(1, 10)))
print(list(range(10)))
print(list(range(1, 11, 2)))
print(list(range(2, 11, 2)))

# using iter()
it = iter(num_list)
for i in range(len(num_list)):
    print(f'element at index {i} is: {next(it)}')

# Higher order functions
# map()
'''
map() function returns a list of the results after applying the given function to each item of a given iterable(list, tuple etc)
Syntax: map(function, iterable)
function: It is a function to which map passes each element of given iterable
iterable: It is a iterable(list, tuple etc) which is to be mapped
returns an iterator of map class'''

# Example:- return double of num
def double(n):
    return 2*n
numbers = (1,2,3,4,5)
result = list(map(double, numbers))
print(result)

# using lambda function
numbers = [i for i in range(1, 11)]
double_list = list(map(lambda x: 2*x, numbers))
print(double_list)

# Example:- list of strings
l = ['bat', 'cat', 'mat', 'rat', 'sat']
test = list(map(list, l))
print(test)

# filter()
'''
The filter() method filters the given sequence with the loop of a function that tests each element in the sequence to be true or not
Syntax: filter(function, sequence)'''
# Example

def check_even(number):
    if number % 2 == 0:
        return True
    return False
numbers = tuple([num for num in range(1, 21)])
filtered_list = list(filter(check_even, numbers))
print(filtered_list)

# using lambda funtion
filtered_list2 = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered_list2)


# reduce()
'''
Python's reduce() implements a mathematical technique commonly known as folding or reduction i.e reduce a list into single cumulative value
it perfoms the following steps
-Apply a function(or callable ) to the first two items in the iterable and generate a partial result
-Use that partial result, together with the third item in the iterable, to generate another partial result
-Repeat the process until the iterable is exhausted and then return a single cumulative value

Syntax: reduce(function, sequence)'''

# Example
# if we want to use reduce function then we have to import functools module
import functools
def add(x, y):
    return x+y
num_list = [1,2,3,4,5]
print(num_list)
print("Sum of values in list: ")
print(functools.reduce(add, num_list))