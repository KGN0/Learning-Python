# Function Basics
# Example 1 (Program demonstrating python funtion)
def average(a, b, c):
    avg = (a + b + c) / 3
    print("Average: ", round(avg, 2))

average(1, 32, 8)

# Example 2 (funtion to display string repeatedly)
def func():
    for i in range(5):
        print("Hello Python Function")

func()

# Example 3 (sum of two integers using functions)
def sum_of_nums(a, b):
    add = a + b
    return add

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
result = sum_of_nums(a, b)
print("Sum = ", result)

# Calling a funtion
'''
Defining a function means specifying its name, parameters that are expected and the set of instructions.
Once the structure is finalized it can be executed by calling it
'''

def callexample():                      # function defination
    print("This is function call")      # function body

callexample()                           # calling a function

# return statement
'''
Return statement is used in a function to return the control back to the caller or return one or more values to the caller.
A return statement would include return keyword and a return value or return values
As python treats everything as an a object, we can return different types of values.
The types of values we can return are int, float, lists, dictionaries, or set of objects, or classes or funtions
return statement not mandatory in a function
One can skip writing return in a funtion.
Or write a plain return with out any return value.
None is returned when we don't write  any return or write just return statement
None is not zero or undefined value
'''
# Example 1 (Function with no return statement)
def expReturn():
    print('no return statement.')
expReturn()

# Example 2 (Explicit return statement)
def expReturn():
    return 10
res = expReturn() # returned value is stored in res variable
print(res)

# Example 3
def expReturn():
    return  # here None is returned because no vlaue is specified
res = expReturn() # returned value is stored in res variable 
print(res)

# Returning Multiple values
'''
In python we can return multiple values from a function'''

# Example
def exp_multi_vlaue_return(x):
    a = x * x
    b = x * x * x
    c = x * 4
    return a, b, c    # it returns tuple
res = exp_multi_vlaue_return(5)
print(res)

# Returning differnt data types
# Example 
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Example
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)