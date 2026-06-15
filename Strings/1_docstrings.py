# Python Docstrings
'''Python documentation strings (or docstrings) provide a convenient way of associating documentation with Python modules, functions, classes and methods'''
# Declaring docstrings
'''These docstrings are declared using triple single quotes or triple double quotes just below the class, method or fucntion declaration.
All functions should have a docstring'''
# Accessing docstrings
'''The docstrings can be accessed using the __doc__ method of the object or using the help function'''
# Example
# Demonstrates how to declare and access a docstring
def func():
    '''The program just prints a message,
        It will display hello world!!!'''
    print("Hello World!!!")

print(func.__doc__)
