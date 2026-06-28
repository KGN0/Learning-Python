''' The main aim of inheritence is a re-usability in python supports the concepts of re-using existing classes
    So, the technique of creating a new classes a new class from an existing class is called inheritance
    The existing class is called the base class and the new class is known as derived class.
Syntax:
class BaseClass:
    #Body of the base class
class DerivedClass:
    #Body of the derived class'''

# Example
class Parent:
    def __init__(self, name, age, behaviour ):
        self.name = name
        self.age = age
        self.behaviour = behaviour
    def parentMethod(self):
        print(self.name)
        print(self.age)
class Child(Parent):
    def __init__(self, name, age, gender, behaviour):
        Parent.__init__(self, name, age, behaviour )
        # self.name = name
        # self.age = age
        self.gender = gender
        
    def childMethod(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.behaviour)

obj = Child('Akhil', 22, 'Male', 'Good')
obj.childMethod()
obj.parentMethod()
print(obj.behaviour)