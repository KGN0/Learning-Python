# The string module
''' The string module consists of a number of useful constants, classes, and functions(some of which are deprecated). 
    These functions are used to manipulate strings'''

import string

# string.ascii_letters
'''Combination of ascii_lower and ascii_uppercase constants'''
print('string.ascii_letters =', string.ascii_letters)
#print(" ".join(string.ascii_letters) )

# string.ascii_lowercase
'''Refers to all lowercase letters from a-z'''
print('string.ascii_lowercase =', string.ascii_lowercase)

# string.ascii_uppercase
'''Refers to all uppercase letters A-Z'''
print('string.ascii_uppercase =', string.ascii_uppercase)

# string.digits
'''Refers to digits from 0-9'''
print('string.digits = ', string.digits)

# string.hexdigits
'''Refers to hexadecimal digits, 0-9, a-f and A-F'''
print('string.hexdigits =', string.hexdigits)

# string.octdigits
'''Refers to octal digits, 0-7'''
print('string.octdigits = ', string.octdigits)

# string.punctuation
'''String of ASCII characters that are considered to be punction chracters'''
print("string.punctuation = ", string.punctuation)

# string.printable
'''String of printable characters which include digits, letters, punctuation and whitespace'''
print('string.printable = ', string.printable)

# string.whitespace
'''A string that has all the characters that are considered whitespace like space, tab linefeed, return, form, form-feed, and vertical tab'''
print('string.whitespace =', "-".join(string.whitespace))

print('Available methods in string module')
for i, item in enumerate(dir(string)):
    print(item.ljust(22), end = "")
    if (i + 1) % 8 == 0:
        print()

print("\n\n",string.__builtins__.__doc__)