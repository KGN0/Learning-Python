# Lambda functions
'''
Lambda or anonymous functions are so called because they are not declared as other functions using the def keyword
But these functions are created using the lambda keyword.
Syntax:
lambda argument(s): expression

lambda arguments contains a comma separated list of arguments and contain only one expression
here the expression contains the arithmetic expression that uses these arguments
    - lambda functions contain only a single line
    - lambda feature was added to python due to the demand from list programmers
'''
# Example
Sum = lambda x, y: x + y
print('Sum =:',Sum(5, 6))

# key pionts
'''
    - lambda function have no name
    - lambda function can take any no of arguments
    - lambda function can return just one value in the form of expression
    - lambda function doesn't have return statement
    - lambda functions are one time version and cannot contain multiple expression
    - they cannot access variables otherthan these in parameters list
    - we can pass lambda functions as arguments in other functions 
'''

# Example
def small(a, b):
    if a < b:
        return a
    else:
        return b

Sum = lambda x, y: x + y
Dif = lambda x, y: x - y

res = small(Sum(5, 1), Dif(4, 2))
print(res)

# lambda functions are used along with built in functions like filter(), map() and reduce()

# 1. filter()
'''The filter function in python takes in a function and a list as arguments that means the filter function is going to work only on list items
This function constructs a new list of items from those elements of the list for which function returns True

Syntax: filter(functioin, seq)
'''
# Example
# program to demonstrate filter() function with and without using lambda function
def func(a):
    if a % 2 == 0:
        return True
    False

list1 = [12, 5, 18, 22, 97, 44]
res = filter(func, list1)
print(list(res))

# with lambda
list1 = [12, 5, 18, 22, 97, 44]

res = list(filter(lambda x : ( x % 2 == 0), list1))
print(res)

# 2. map()
'''
map() function executes another user- defined function for each element in an iterator.
To do this it takes tow arguments. One is user-defined function and another is an iterator
'''

# program to demonstrate map() function with and without using lambda function
def func(a):
    return len(a)

list1 = ['python', 'programming']
res = map(func, list1)
print(list(res))

# with lambda function

list1 = ['Hello', 'python']
res = list(map(lambda x: len(x), list1))
print(res)

# reduce()
'''The reduce() function applies a function of two arguments cumulatively to the items of a sequence, reducing the entire sequence to a single value.'''
# Example
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Multiply cumulative results: ((1 * 2) * 3) * 4) * 5
product = reduce(lambda x, y: x * y, numbers)

print(product)  # Output: 120