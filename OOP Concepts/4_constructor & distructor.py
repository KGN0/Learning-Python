# Constructor
''' Constructors are mainly useful to initialize all the vairables in the class
    when we create a class without constructor in python, the interpreter automatically creates default constructor
    Constructor also take one argument, "that argument can be called as self".
    The main aim of constructor is to assign values to instance variables that the object need when it starts.
    Constructors are the first statements that are executed in the class
Syntax: def __init__(self [, argument1, argument2,..]):'''
# Example
class Abc:
    def __init__(self):
        print("I'm constructor\n")
    
Abc()

# Types of constructors
# 1. Default constructor: The constructor that does not contain any arguments are called as default constructor
# Example
class Constuctor:
    def __init__(self):
        print("I am constructor")
        print("I am default constructor.\n")

Constuctor()

# 2. Parameterized constructor: These are used to take variables that initializes and to use in the class
# Example
class Parameterized:
    def __init__(self, val:int, name:str, age:int):
        self.val = val
        self.name = name
        self.age = age
        print('The value is:', self.val)
        print('The name is:', self.name)
        print('The age is:', self.age)
Parameterized(1, 'Akhil', 22)


# Distructor
'''A distructor is another member function that is invoked when the object is deleted explicitly using del command.
Syntax: def __del__(self)'''
# Example
class Employee:
    def __init__(self, name = "", earning = 0, bonus = 0):
        self.name = name
        self.earning = earning
        self.bonus = bonus
    def input_data(self):
        self.name = input('\nEnter name of employee: ')
        self.earning = int(input('Enter earning(rounded): '))
    def compute_bonus(self):
        if (self.earning <= 100000):
            temp_bonus = 0
        elif (self.earning <= 200000):
            temp_bonus = 1000 + (self.earning - 100000) * 0.01
        elif (self.earning <= 300000):
            temp_bonus = 2000 + (self.earning - 200000) * 0.02
        else:
            temp_bonus = 4000 + (self.earning - 300000) * 0.03
        self.bonus = temp_bonus
    def output_data(self):
        print('\nName of the employee: ', self.name)
        print('Bonus to be paid: %.2f' %(self.bonus))

emp = Employee()
emp.input_data()
emp.compute_bonus()
emp.output_data()