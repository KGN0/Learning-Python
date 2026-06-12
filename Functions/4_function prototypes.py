# Function prototypes
'''
There are four types
- Function with no argumetns and no return value
- Function with arguments and no return value
- Function with arguments and with return value
- Function with no arguments and with return value
'''

# 1. Funcion with no arguments and no return value
'''
In this prototype, no data transfer takes place between the calling function and the called function.
The called program does not receive any data from the calling program and does not send back any value to the calling program
'''

# Example
def add():
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = a + b
    print("Sum:",c)

add()   # function calling with no arguments

# 2. Function with arguments and no return value
'''
In this prototype, data is transferred from calling function to called function.
The called program receives some data from the calling program and does not send back any values to calling program
'''

# Example
def add(a, b):
    c = a + b
    print("Sum:", c)

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
add(a, b)   # function calling with arguments

# 3. Function with arguments and with return value
'''
The data is transferred between the calling function and called function.
The called program receives some data from the calling function and send back a value return to the calling function
'''

# Example
def add(a, b):
    c = a + b
    return c

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
total = add(a, b) # function calling with arguments and with return value
print('Sum:',total)

# 4. Function with no arguments and with return value
'''
The calling program can not pass any arguments to the called program but the called program may send some return value to the calling program
'''

# Example
def add():
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = a + b
    return c

total = add()   # function calling with no arguments and with return value
print("Sum:", total)