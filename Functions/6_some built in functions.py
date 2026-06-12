# Library functions or Built in functions
'''
These functions are built into python and can be accessed by a user. For using these functions we need not import any module.
Python has a small set of built in functions as most of the functions are partitioned into modules
Some of them are expalined below
'''

# 1. abs(x) 
'''
Return the absolute value of a number. The argument x may be an integer or a floating point number.
If it is a complex number, then its magnitude is returned.
'''
# Example
print(abs(-5))
print(abs(5))
print(abs(5.25))
print(abs(-5.25))
print(abs(2 + 3j))

# 2. all(iterable)
'''
Return True if all elements of the iterable are True or if the iterable is empty
Syntax:
def all(iterable):
    if not element:
        return False
    return True
'''
# Example
lst1 = [True, True, True]
lst2 = [True, False, False]
x = all(lst1)
y = all(lst2)
print(x)
print(y)

# 3. any(iterable)
'''
Return True if any element of the iterable is true. It the iterable is empty, return False
Syntax:
def any(iterable):
    if not element:
        return False
    return True
'''
# Example
lst1 = [True, True, True]
lst2 = [True, False, False]
x = any(lst1)
y = any(lst2)
print(x)
print(y)

# 4. ascii(object)
'''
Returns a readable version of an object. Replaces non ascii characters with escape character
'''
x = ascii("Welcome to Python")
print(x)

# 5. bin(x)
'''
Convert an integer number to a binary string prefixed with "0b"
'''
# Example
print(bin(5))
print(bin(-8))

# 6. bool(x)
'''
Return a boolean value i.e. True or False.
This function will return True unless the object is an empty list or set or tuple
'''
# Example
print(bool(5))
print(bool(-8))
print(bool(0))
print(bool([]))
print(bool([1,2,3]))
print(bool({}))
print(bool({"x", "y", 2}))
print(bool(()))
print(bool((10, 20, 30)))

# 7. breakpoint()
'''
Python breakpoint() function calls sys.breakpointhook() function.
By default, sysbreakpointhook() calls pdb.set_trace() function.
So at the very least, using breakpoint() provide convenience in using a debugger
because we don't have to explicity import pdb module
'''
# Example
x = 10
y = 'Hi'
z = "Hello"
print(y)
# breakpoint()
print(z)

# 8. bytearray()
'''
Return a new array of bytes.
Syntax: bytearray(x, encoding, error)
x: a source to use when creating the bytearray object.
    x can be an integer, or string or an iterable object.
    If x is a string, then one needs to specify the encoding of  the source.
encoding: The encoding of the string
error: Specifies what to do if the encoding fails all the parameters are optional
'''
# Example
x = bytearray(5)
print(x)

y = bytearray("Welcome to python", 'utf-8')
print(y)

z = bytearray([10, 20, 30, 40, 50])
print(z)

# 9. bytes()
'''
Returns a bytes object
Syntax: bytes(x, encoding, error)
'''
x = bytes(5)
print(x)

y = bytes("Welcome to python", 'utf-8')
print(y)

z = bytes([10, 20, 30, 40, 50])
print(z)

# 10. callable(object)
'''
Returns True if the object argument is callable, otherwise returns False
'''
# Example
# A normal variable not callable
x = 5
print(callable(x))

# A function is callable
def x():
    a = 100
print(callable(x))

# 11. chr()
'''Returns a character from the specified Unicode code
Syntax: chr(number)'''
# Example
x = chr(65)
y = chr(97)
print(x)
print(y)

# 12. classmethod()
'''Converts a method into a class method. The class method can be called both by the class and object
Syntax:
class C:
    @classmethod
    def f(cls, arg1, arg2,...):
        pass

objname.classmethod()
or
class().classmethod()
'''
# Example
class employee:
    sal = 25000
    def printSalaray(cls):
        print('Employee salary is', cls.sal)

employee.printSalaray = classmethod(employee.printSalaray)
employee.printSalaray()

# compile()
'''Returns a python code object from the source
Syntax: compile(source, filename, mode, flags= 0, dont_inherit = False, optimize = -1)
Source: The source to compile, can be a String, a Byte object, or an AST object
mode: it is either exec or eval or single. The mode eval accepts only a single expression, where as exec takes a code block that has 
Python statements, class, functions and so on, 
If the mode is single then it consists of a single interactive statement
'''
# Example
codeInString = 'a = 5\nb = 6\nsum = a + b\nprint("sum =",sum)'
codeObject = compile(codeInString, 'sumstring', 'exec')
exec(codeObject)

# 14. complex()
'''Return a complex number with the value real + imag*1j or convert a string or number to a complex number
Syntax: complex([real [,imag]])
real: if real part is omitted then it takes default value 0
imag: if imag part is omitted then it takes default to 0
'''
# Example
c = complex(4, 5)
print(c)

c = complex(1)
print(c)

c = complex()
print(c)

c = complex('2-5j')
print(c)

# 15. delattr()
'''Deletes an attribute from the object
Syntax: delattr(object, name)
object: the object from which name attribute is to be removed
name: a string which must be the name of the attribute to be removed from the object
'''
# Example
class Coordinate:
    x = 2
    y = 3
    z = 0

p1 = Coordinate()
print("x=", p1.x)
print("y=", p1.y)
print("z=", p1.z)

delattr(Coordinate, 'z')
print("x=", p1.x)
print("y=", p1.y)
# print("z=", p1.z)  # raises error