'''Overriding and overloading are the best examples for the concept of polymorphism so polymorphism is the best from of oops'''
# Overloading
''' Overloading is the ability of a function or an operator to behave in different ways based on the parameters that are passed to function
    or the operands that the operator acts on.
    Overloading a method fosters reusability
    Overloading also imporves code clarity and eliminates complexity.
'''
# Method overloading in python
'''We can create a method that can be called in different ways. So we can have a method that has zero, one or more nuumber of parameters'''
# Example 1: 
'''we create a class with one method Hello(). The first parameter of this method is set to None.
 This will give us the option to call it with or without a parameter'''

class Person:
    def Hello(self, name = None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello')

obj = Person()
obj.Hello()
obj.Hello("Pavan")

# Example 2:
class Compute:
    def area(self, x = None, y = None):
        if x != None and y != None:
            return x * y
        elif x != None:
            return x * x
        else:
            return 0
obj1 = Compute()
print(obj1.area())
print(obj1.area(9))
print(obj1.area(2,7))

# Operator Overloading
'''Operator overloading means giving extended meaning beyond their predefined operational meaning 
For example operator + is used to add two integers as well as join two strings and merge two lists.
It is achievable because "+" Operator is overloaded by int class and str class. '''
# Example
# + operator for different purposes
print(10 + 15)
#  concatenate two strings
print('Well' + 'come')
# product two numbers
print(8 * 9)
# repeat the string
print('Welcome' * 4)

# When we use + operator the magic method __add__ is automatically invoked in which the operation for + operator is defined
# Example
class A:
    def __init__(self, a):
        self.a = a 
    def __add__(self, o):
        return self.a + o.a
obj1 = A(5)
obj2 = A(2)
obj3 = A("well")
obj4 = A("come")
print(obj1 + obj2)
print(obj3 + obj4)

# Overriding in python
''' Method overriding is a concept of object oriented programming that allows us to change 
    the implementation of a function in the child class that is defined in the parent class.
    It is the ability a child clas to change the implementation of any method which is already provided by one of its parent class'''
# Example
class Parent:
    def __init__(self):
        self.value = "Inside Parent"
    def show(self):
        print(self.value)
class Child:
    def __init__(self):
        self.value = "Inside Child"
    def show(self):
        print(self.value)
obj1 = Parent()
obj2 = Child()
obj1.show()
obj2.show()