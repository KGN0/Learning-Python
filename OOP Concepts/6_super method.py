# Super() Method
''' super keyword acts like a built-in-functions in python. The super built-in-function returns a proxy object that allows us to parent class.
    Instead of calling the super class constructor and super class method names with the classname they are also called with a built-in-function
    called super() in the childclass
syntax: super().__init__(argument1, argument2,..)
            or
        super().methodName()'''
# Example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("I am superclass variable:", self.name)
        print("I am superclass variable:", self.age)
    def personMethod(self):
        print("I am superclass method:", self.name)
        print("I am superclass method:", self.age)

class Man(Person):
    def __init__(self, name, age, height, weight):
        super().__init__(name, age)
        self.height = height
        self.weight = weight
        print("I am sub class variable:", self.height)
        print("I am sub class variable:", self.weight)
    def mankind(self):
        super().personMethod()
        print("I am child method")

obj = Man('Ravi', 23, 166, 65)
obj.mankind()