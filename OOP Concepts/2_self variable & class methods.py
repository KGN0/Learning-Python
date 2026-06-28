'''Class methods are noting but functions. The functions which are written in the class can be called as class methods.
    Class methods start with the keyword called def and mathod name followed by paranthesis by colon(:) operators
Syntax: def methodName()'''
# Example 1
class ABC:
    var = 10
    def display():
        print('I am the class method')
obj = ABC()
print(obj.var)
# obj.display() # it raise an error 

'''So to avoid errors class methods must have the default and first argument with the name as "self" in the class method parameters list.
    The self is the first argument variable that is added to the beginning of the parameters list.
    So the class method uses self, they require an object. For this reason they are after referred as 'instance methods.
    In class, all methods have self as their first parameter. Self refers to the instance calling the method'''
# Example 2
class Abc:
    def display(self):
        print('Hello This is class method.')

obj1 = Abc()
obj1.display()

# Example 3
class Create:
    def createName(self, name):
        self.name = name
        print('name is created=', self.name)
obj2 = Create()
obj2.createName('Pavan')


# __int__:
''' The method init is the most important method in the class. This is a built in method which needs no initialization.
    This is called when an instance(object) of the class is created, using the class name as function.
    The __init__ method is called constructor'''
# Example
class Book:
    def __init__(self, bookname):
        self.bookn = bookname
    def cost(self, cost):
        print('cost of', self.bookn, 'is', cost)
b = Book('Wings on Fire')
b.cost(300)

# Types of methods in python
# 1. Instance method
'''An instance method is nothing but an ordinary method written with in the class. These instance method will take self as an argument in the parameters.'''
# Example
class Animals:
    cat = 'meow'
    def sound(self):
        print('I am Instance method of animals')
obj3 = Animals()
print(obj3.cat)
obj3.sound()


# 2. Class method
'''Class methods are little different from these ordinary methods. The class method take first argument in the parameters as "cls" but not the "self".
    We can use classmethod decorator "@classmethod" for class defination. 
Syntax: @classmethod
def fun(cls, arguments,..):
    statements
'''
# Example 1
class Person:
    @classmethod
    def age(cls):
        print("I am class method age")
Person.age()

# Example 2
class Persons:
    def val(self, name, age):
        self.name = name
        self.age = age
        print("Name is:", self.name)
        print("Age is: ", self.age)
    @classmethod
    def volume(cls, name, age):
        cls.name = name
        cls.age = age
        print('Classmate name is: ', cls.name)
        print('Classmate age is: ',cls.age)
obj4 = Persons()
obj4.val('Hari', 20)
Persons.volume('Pavan', 21)

# Static methods
'''Static methods are special case of methods in python. Static methods belongs to class
    But static methods knows nothing about the class and they just deals with its parameters static methods take arguments as "self" or "cls".
    They can be called with classname or objectname'''
# Example
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        are = self.length * self.breadth
        print('area of reactange:', are)
    @staticmethod
    def perimeter(length, breadth):
        peri = 2 * length * breadth
        print("Perimeter of the rectangle:", peri)
    
obj5 = Rectangle(5, 6)
obj5.area()
Rectangle.perimeter(5, 6)