# 16. dict()
'''Creates a dictionary. Different forms of dict() constructors are
Syntax:
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
**kwarg: It takes an arbitary number of keyword arguments
'''
# Example
numbers = dict(x = 5, y = 0)
print('numbers =', numbers)
print(type(numbers))

empty = dict()
print('empty =', empty)
print(type(empty))

# 17. dir()
'''Without arguments, return the list of names in the current local scope.
With an argument, attempt to return a list of valid attributes of this object
Syntax: dir(object)
'''
# Example
numbers = [10, 20, 30]
print(dir(numbers))

print("\nReturn Value from empty dir()")
print(dir())
print()

class Person:
    name = 'Jule'
    age = 42
    country = 'America'
print(dir(Person))

# 18. divmod()
'''This method takes two (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division
Syntax:
divmod(dividend, divisor): dividend, divisor are non-complex numbers
'''
# Example
print('divmod(8, 3) =', divmod(8, 3))
print('divmod(3, 8) =', divmod(3, 8))
print('divmod(5, 5) =', divmod(5, 5))
print('divmod(8.0, 3) =', divmod(8.0, 3))
print('divmod(3.0, 8) =', divmod(3.0, 8))
print('divmod(7.5, 2.5) =', divmod(7.5, 2.5))

# 19. enumerate()
'''Return an enumerate object
Syntax: enumerate(iterable, start = 0)
iterable: a sequence, an iterator, or objects that supports iteration
start(optional)- enumerate() starts counting from this number. If start is omitted, 0 is taken as start
'''
# Example
grocery = ['rice', 'dal', 'bread']
enumerateGrocery = enumerate(grocery)
print(type(enumerateGrocery))
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))
print()

print('Using for loop')
for item in enumerate(grocery):
    print(item)

for i , j in enumerate(grocery):
    print(i, j)
print('Changing default start value')
for count, item in enumerate(grocery, 100):
    print(count, item)

# 20. eval()
'''The eval() function evaluates the specified expression, if the expression is a legal python statement it will be executed
Syntax: eval(expression, globals = None, locals = None)
expression: A string that will be evaluated as python code
globals(optional): A dictionary containing global parameters
'''
# Example
x = 'print(55)'
eval(x)

x = 1
print(eval('x + 1'))


# 21. exec()
'''The exec() method executes the dynamically created program, which is either a string or a code object
Syntax: exec(object, globals, locals)
object: Either a string or a code object
globals(optional): a dictionary
'''
# Example
program = 'a = 5\nb = 6\nsum = a + b\nprint("sum:", sum)'
exec(program)


# 22. filter()
'''The filter() function extracts elements from an iterable(list, tuple, etc) for which a function returns True
Syntax: filter(function, iterable)
The filter() function takes two arguemts
function: a function
iterable: an iterable like sets, lists, tuples, etc'''
# Example
letters = ['a', 'b', 'c', 'd','e', 'g', 'h', 'i']
def filter_vowels(letter):
    vowels = ['a','e','i','o','u']
    return True if letter in vowels else False

filtered_vowels = filter(filter_vowels, letters)
print(tuple(filtered_vowels))


# 23. float()
'''Returns a floating point numbers
It takes string which is compatable or int'''
# Example
a = '3.14'
print(type(a))
b = float(a)
print(b)
print(type(b))


# User defined functoins
'''In python we can write our own function(). These functions can be combined to form module which can be used in other programs by importing them.
To define a function, def keyword is used'''