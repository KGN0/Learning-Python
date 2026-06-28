# Single Inheritence
''' In Single inheritence a class can be derived from a single base class. This type of inheritence is called single inheritence.
    It contains only one base class'''
# Example
class Super:
    def __init__(self):
        pass
    def superMethod(self):
        print("I am super class method")
class Sub(Super):
    def subMethod(self):
        Super.superMethod(self)
        print("I am sub class method")

obj = Sub()
obj.subMethod()
obj.superMethod()
print()

# Multiple Inheritence
''' When a derived class inherits features from more than one base clas it is called "multiple" inheritence
    The derived class has all the features of both the base classes and also it can contain new features
Syntax:
class BaseClass1:
    # Block of stetements
class BaseClass2:
    # Block of statements
class Derived subclass(Baseclass1, Baseclass2):
    # Block of statements
'''
# Example
class Coral1:
    def coralmethod(self):
        print("I am coral method")
class Coral2:
    def coralmethod(self):
        print("I am second coral method")
class Animal(Coral1, Coral2):
    def animalmethod(self):
        print("I am sub class")

obj = Animal()
obj.coralmethod()


# Multiple Inheritence
'''The technique of deriving a class from already derived class is called multi-level-inheritence
Syntax:
class Base:
    # Statements
class Derived1(Base):
    # Statements
class Derived2(Derived1):
    # Statements
'''
# Example
class Person:
    def details(self):
        print("These are details")
class Teacher(Person):
    def qualify(self):
        print("I am a phd teacher")
class Hod(Teacher):
    def experience(self):
        print("I am an experienced teacher")

obj = Hod()
obj.experience()
obj.qualify()
obj.details()

# Multi-path Inheritance
''' Deriving a class from there derived classes that are these derived classes acts as a like base class. 
    These classes in term derives from other classes. This other class can be called as a Baseclass'''
# Example
class Student:
    def standard(self):
        print("I am this standard")
class Teacher(Student):
    def qualify(self):
        print("I am Phd")
class Hod(Teacher):
    def experience(self):
        print("I am experienced")
class Result(Hod):
    def eligible(self):
        self.experience()
        self.qualify()
        self.standard()
obj = Result()
obj.eligible()