# Functions
'''
Functions is a group of statements that perform a specific task
Functions may or may not take arguments and may or may not produce results
'''
# advantages of functions
'''
- Decomposing large programs in to smaller functions makes program easy to understand and maintain and debug.
- Functions developed for one program can be reused with or without modification when need
- Reduces program development time and cost
- It is easy to locate and isolate faulty functions
'''
# Types of functions
# Built in functions
'''These funtions are already built into python interpreter and readily available for use'''
print("Something")  # print objects to the stream
a = input("enter something")  # reads a line from input
c = abs(-43) # return absolute value of -43
le = len("Programmers") # return length of the string

#Example
c = input("Enter a character: ")
print('ASCII value of ',c, 'is', ord(c))

# User defined functions
"""
Functions defined using the def keyword by the users according to their requiremtns are called user defined functions
The users can modify the function according to their requirements"""
# Example
def add(a, b):
    return a + b

a = 5
b = 10
print(add(a, b))

# example
def greet(name):
    print(f"Hello {name}")

name = input("Enter your name: ")
greet(name)