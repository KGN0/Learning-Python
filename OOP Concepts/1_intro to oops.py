# Procedural programming
'''Procedural programming can be defined as a programming model which is derived from structure programming, based upon the concept of calling procedure.
Procedures, also konwn as routines, subroutines or functions, simply consist of a series of computational steps to be carried out. During program's execution,
any given procedure might be called at any point, including by other procedures or itself'''

# Object Oriented Language
'''OOPs is a method of structuring a program by bundling related properties and behaviors into individual objects.
It means directed towards objects. In other words, it means functionality directed towards modeling objects.
This is one of the many techniques used for modeling complex systems by describing a collection of interacting objects via their data and behavior.'''

# Defing a class
'''A class is the main concept of object-oriented programming, infact a class is the basic building block of python
    Also define a class as a blueprint for creating objects'''
# Specifing a class
class className:
    # <docstrings>
    # statements
    pass

# Example 
class NewClass:
    a = 10
    b = 20
print(NewClass.a)
print(NewClass.b)

# Creating objects
'''An object is an instance of a class. We can create number of objects in a program. Every object contians some data and functions.
    After class creation the next job is to create an object. The object then access class variables and class methods by using the dot(.) operator.
Syntax: objectName = ClassName([parameter1[,parameter2,...]])
'''
# Example
class NewObject:
    a = 10
    b = 20
    def display(self, c = 0, d = 0):
        print('c=', c)
        print('d=', d)

obj = NewObject()
print(obj.a)
print(obj.b)
obj.display()
obj.display(14, 3)

# Accessing members of class
'''Once an object of a class is created, its members can be accessed/invoked using dot notation
Syntax: objectName.methodName([parameter1 [, parameter2, ..]])'''
# Example
class Addition:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a + b

obj2 = Addition()
print('a is:', obj2.a)
print('b is:', obj2.b)
print('a + b is:', obj2.c)
