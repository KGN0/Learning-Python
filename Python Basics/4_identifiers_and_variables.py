# Identifiers
'''
An identify is basically a name in a program, identifiers can be used to denote variables, objects, classes, functions, lists, tuples, and dictionaries.

Rules for naming an identifier
1. The first character must be an alphabet or an underscore
2. Must consist of letters, digits or underscore only.
2. Cannot use a keyword.
4. Cannot contain a white space
'''

# Variables
'''
A variable is a name that refers to a value.
Variables are also called as identifiers.

'''

# Syntax
# Variable_name = value
# Example 
a = 10

# Multiple assignments
x = 5 # x is a variable
print("x = " , x)
x = 10
print("x = ", x)
x = 15
print("x = ", x)

# Simultaneous Assignments
n, m = 5, 10
print("n = ",n, "m = ", m)

# we can change of variables value and type within an executing program
# example
x = 100
print("variables value = ", x, 'and type = ', type(x))
x = 'Test'
print("variables value = ", x, 'and type = ', type(x))

# Bound and Unbound variable
'''
- A variable that has been assigned a variable is called a bound variable
- otherwise it is called an unbound or undefined variable.
'''

# deleting variable
'''
del keyword is used to delete multiple variables
'''
# example
del a  # if you print a then an error occurs
