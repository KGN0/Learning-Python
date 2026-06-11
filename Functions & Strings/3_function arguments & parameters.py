# Funtion Parameters
'''
A function can take parameters, which are values we supply to the function so that the function can do something utilizing those values
The names given in the function definition are called parameters, where as the values we supply in the function call are called arguments.'''

# Example 1 (find maximum in two numbers)
def find_max(a, b):  # a, b are parameters
    if a > b:
        print(a, "is max.")
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, "is max.")
find_max(8,3)       #  directly pass literal values

# if we pass variables as arguments
x = 34
y = 90
find_max(x, y)      # passing arguments


# Funtion Arguments
'''
An argument is an expression which is passed to a function by its caller in order for the function to perform its task.
It is an expression in the comma separated list bound b the parenthesis in a function call expression
There are two types of arguments in the function
1. Actual arguments
2. Formal arguments
'''
# Actual arguments & Formal arguments
'''
The arguments that are passed in a function call are called actual arguments
The formal arguments are arguments in a function declaration. These are belongs to the called function
'''
# Example 
def square(x):      # x is formal arguments
    print(x * x)
square(5)           # 5 is actual arguments

# Example
def greet(name, msg):
    print("Hello", name, msg)
greet('User', 'Good Morning')

# greet("Programmer")  returns type error missing 1 required positional argument: 'msg'

# greet("Boss", "Good evening", "Sweet dreams") return Type Error greet() takes exactly 2 arguments given 3

'''-----------------------------------------------------------------------------------------------------------------------------------------------'''

# Types of arguments
# 1. Positional arguments
'''
Positional arguments are assigned to the parameters of the function defination in sequential order
These types of arguments hould be passed in the correct order in which they are declared in the function defination 
'''
# Example 1 (prints the details of an employee)
def employee(name: str, age: int, salary: float): # Declaring data types of parameters
    print('Employee name:', name)
    print('Employee age:', age)
    print('Employee salary:', salary)
    print() # prints new empty line

employee('Abhi', 20, 100000)
employee('Teja', 20, 100000)

# 2. Keyword arguments
'''
These arguments are passed using the names of their corresponding parameter to avoid the confusion created by positional arguments
In this case the order of the arguments passed doesn't matter, aas the arguments matched by name and not position
'''
# Example (Using keyword arguments)
def employee(name: str, age: int, salary: float): # Declaring data types of parameters
    print('Employee name:', name)
    print('Employee age:', age)
    print('Employee salary:', salary)
    print() # prints new empty line

employee(name = 'Abhi', age = 20, salary = 100000)
employee(age = 20, salary = 100000, name = 'Teja')

# 3. Default arguments
'''
In python, we can initialize default arguments for the parameters while defining a function
These are used when arguments are not passed for the respective parameter during funciotn calling
'''
# Example (function defination with default arguments)
def employee(name: str, age: int = 30, salary: float = 110000): # Declaring data types of parameters
    print('Employee name:', name)
    print('Employee age:', age)
    print('Employee salary:', salary)
    print() # prints new empty line

employee(name = 'Abhi', age = 32 )
employee(name = 'Teja', salary = 100000)

# 5. Passing different data types
'''
You can send any data type as an argument to a function (string, number, list, dictionary, etc.).
The data type will be preserved inside the function:
'''
# Example
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

# Example
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

# 6.Positional-Only Arguments
'''
You can specify that a function can have ONLY positional arguments.
To specify positional-only arguments, add , / after the arguments:
'''
# Example
def my_function(name, /):
  print("Hello", name)

my_function("Emil")

# 7. Keyword-Only Arguments
'''
To specify that a function can have only keyword arguments, add *, before the arguments:
'''
# Example
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")

# 8. mixing positional and keyword arguments
'''
You can mix positional and keyword arguments in a function call.
However, positional arguments must come before keyword arguments:
'''
# Example
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

# 9. Variable-length arguments
'''
These arguments are used when the number of arguments to be passed to the function is not known beforehand.
There are two types of variable length arguments namely variable-length positional arguments and variable-length keyword arguments
'''
# i. Variable-length positional arguments (*args)
'''
When you prefix a parameter with an asterisk (*) symbol, it collects all the positional arguments and stores them in the form of a tuple.
'''
# Example
def var_args(*args):
    print(args)
var_args('Python', 'is', 'an', 'interpreted', 'language')

# ii. variable-length keyword arguments(**kwargs)
'''
**kwargs works only for keyword arguments.
It collects all the keyword arguments into a dicitonary, where the arguments names are the keys, and arguments are the corresponding dictionary values
'''
# Example
def var_args(**kwargs):
    print(kwargs)
var_args(str1 = 'Welcome', str2 = 'To', str3 = 'Python')

# 10.Using *args with Regular Arguments
'''You can combine regular parameters with *args.
Regular parameters must come before *args:
'''
# Example
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

# 11. Using **kwargs with Regular Arguments
'''You can combine regular parameters with **kwargs.
Regular parameters must come before **kwargs:
'''
# Example
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

# 12. Combining *args and **kwargs
'''You can use both *args and **kwargs in the same function.
The order must be:
1. regular parameters
2. *args
3. **kwargs
'''
# Example
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

# 13. Unpacking Lists with *
#If you have values stored in a list, you can use * to unpack them into individual arguments:

#Example
#Using * to unpack a list into arguments:

def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

# 14. Unpacking Dictionaries with **
#If you have keyword arguments stored in a dictionary, you can use ** to unpack them:

#Example
#Using ** to unpack a dictionary into keyword arguments:

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")