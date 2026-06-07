# Type conversion
'''
This process of converting values for one type to another type is known as type conversion
Types of type conversion
1. Implicit type conversion = automatically performed by the python interpreter without programmer;s intervention
2. Explicit type conversion = this conversion is user defined
'''
# example for implicit type conversion
a = True
print(type(a))

b = 5
print(type(b))

c = a + b
print(type(c))

# example 2
a = 15
print(type(a))

b = 17.5
print(type(b))

c = a + b
print(type(5))

# examples for explicit type conversion
m = float(35)  # int to float
print(type(m))

o = float('7') # string to float 
print(type(o))

s = str(99)    # int to string
print(type(s))
# type conversion functions
'''
- int()
- str()
- float()
- bool()
'''