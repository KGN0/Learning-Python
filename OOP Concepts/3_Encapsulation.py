''' Encapsulation in python is the process of wrapping up variables and methods into a single entity. 
    In programming, a class is an example that wraps all the variables and methods defined inside it.
    This puts restrictions on accessing variables and methods directly and can prevent the accidnetal modification of data.
    Encapsulation can be done using private and protected data members'''
# Public Data Members Declaration
# Example: Program to demonstrate handling of public data members
class Employee:
    def __init__(self, name, salary):
        self.name = name                # public data members
        self.salary = salary            # public data members
emp = Employee('Veerababu', 10000)
print("\nEmployee salary =", emp.salary)
emp.salary = 20000
print('Employee modified salary =', emp.salary)

# Protected Data Members Declaration
class Employee:
    def __init__(self, name, salary):
        self._name = name               # protected data members
        self._salary = salary           # protected data members
emp = Employee("Mahi", 1000)
print('\nEmployee salary =', emp._salary)
emp._salary = 2000
print('Employee modified salary =', emp._salary)

# Hence, the responsible programmer would refrain from accessing and modifying instance variables prefixed with -(single underscore) from outside its class

# Private Data Members Declaration
class Employee:
    def __init__(self, name, salary):
        self.__name = name               # private data members
        self.__salary = salary           # private data members
emp = Employee("Mahi", 1000)
# print('\nEmployee salary =', emp.__salary)   # It raises attribute error. to see error remove from commenting
emp._salary = 2000
# print('Employee modified salary =', emp.__salary)
print('\nEmployee salary =', emp._Employee__salary)
# Handling of private attributes indirectly
emp._Employee__salary = 3000
print('Employee modified salary =', emp._Employee__salary)