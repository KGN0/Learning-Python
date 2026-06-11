# Scope of a variable
'''
In python access to any variable may not possible from any part of the program
This depends on where you have declared a variable

Scope of the variable:
Part of the program in which a variable is accessible is called it's scope
There are two types
- local variable
- global variable
'''

# Local and Global variables
'''
Global variable are the ones that are defined and declared ouside any function and are not specifed to any function
They can be used any part of the program and visible throughout the program file

A variable which is defined within a function is local to that function
Local variable can be accessed only inside the function in which they are declared
'''

# Example
a = 10
print("Value of global variable", a)
def test_fun(b):
    print("Inside function - local variable:", b)
    c = 30
    print("Inside function - local variable:", c)

test_fun(20)
print("Outside function - local variable:", a)
#print("Outside function - local variable:", b)  -return NameError name b is not found i.e can't be acessed


# Global Variable Declaration - using the Global Statement

a = 10 # global variable
print("Value of global variable", a)
def test_fun():
    global a
    b = 20
    print("Inside function - local variable:", b)
    c = a + b
    print("Inside function - local variable:", c)

test_fun()
print("Outside function - local variable:", a)

#print("Outside function - local variable b and c :", b, c)  -return NameError name b is not found

# Program to Modification of global variable
'''
if there is a global variable in the program and you create another global variable using global statement
then the changes made in the variable will be feflected everywhere in the program
 '''
a = 10 # global variable
print("Value of global variable", a)
def test_fun():
    global a
    a = 20
    print("Inside function - variable a:", a)
    
test_fun()
print("Outside function - variable a:", a)

a = 30
print("Outside function - variable a:", a)

# Program to demonstrate access of variable in outer and inner functions
def outer_fun():
    a = 10
    def inner_fun():
        b = 20
        print("Outer function variable;", a)
        print("Inner function variable:", b)
    inner_fun()
    print("Outer function variable;", a)
    # print("Inner function variable:", b) return NameError b value cannot acessed outside inner loop
outer_fun()
