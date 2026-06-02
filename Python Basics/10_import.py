# import
'''
When our program grows bigger, it is a good idea break it into different modules
A module is a file containg python definations and statemetns
pyton modules have a filename and endswith .py extension

syntax: import module1, module2, moduleN'''

# Example
# we can import math module by typing import math
import math
n = math.sqrt(25)  # sqrt() method finds the square root of a number
print('The square root of 25 is: ', n)

# another way to import is
import math as m
n = m.sqrt(81)
print('The square root of 81 is',n)

# if we want to use specific method only then
from math import sqrt, factorial
n = sqrt(100)
print('The square root of 100 is', n)

m = factorial(5)
print('The factorial of 5 is', m)