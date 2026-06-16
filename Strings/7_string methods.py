# String methods
# string.find('string', beg, end)
'''Used to find the position of substring within a string. Returns -1 if string is not found, otherwise retuns first occurence of string if found'''
# Example
s1 = 'Hai Bye Bye'
s2 = 'Bye'
print('s1 =', s1)
print('s2 =', s2)
print()
print('s1.find(s2, 0) =', s1.find(s2, 0))
print('s1.find(s2, 5, 12) =', s1.find(s2, 5, 12))

# string.rfind('string', beg, end)
'''It works similar to find(), but it returns the position of the last occurence of string'''
print('s1.rfind(s2, 0) =', s1.rfind(s2, 0))

# string.startswith('string', beg, end)
'''Returns True if the function begins with the given string, otherwise returns False'''
print('s1.startswith(s2) =', s1.startswith(s2))

# string.endswith('string', beg, end)
'''Returns True if the function ends with the given string, otherwise returns False'''
print('s1.endswith(s2) =', s1.endswith(s2))

# string.islower()
'''Returns True if the string is in lowercase, otherwise returns False'''
print('s1.islower() =', s1.islower())

# string.isupper()
'''Returns True if the string is in uppercase, otherwise returns False'''
print('s1.isupper() =', s1.isupper())

# string.lower()
'''Converts the string into lower case'''
print('s1.lower() =', s1.lower())

# string.upper()
'''Converts the string into upper case'''
print('s1.upper() =', s1.upper())

# string.swapcase()
'''Swap the cases of string i.e. from upper case to lower case and vice versa'''
print('s1.swapcase =', s1.swapcase())

# string.title()
'''Converts the string into title case'''
print('s1.title() =', s1.title())

# string.capitalize()
'''Converts the string into capitalize case'''
print('s1.capitalize() =', s1.capitalize())

# len('string')
'''Returns the length of the string'''
print('len(s1) =', len(s1))

# string.count('string', beg, end)
'''Counts the occurence of substring in the main string'''
print('s1.count(s2) =', s1.count(s2))
print('s1.count(s2, 0) =', s1.count(s2, 0))
print('s1.count(s2, 5, 12) =', s1.count(s2, 5, 12))

# string.center(width, fillchar)
'''Surround the string, with a character repeated both sides of string multiple times'''
print('s1.center(30, "*") =', s1.center(30, "*"))

# string.ljust(width, fillchar)
'''Returns a new string by padding the character to the left'''
print('s1.ljust(30, "*") =', s1.ljust(30, "*"))

# string.rjust(width, fillchar)
'''Returns a new string by padding the character to the left'''
print('s1.rjust(30, "*") =', s1.rjust(30, "*"))

# string.isalpha()
'''Returns True when the string contains only alphabets'''
print('s1.isalpha() =', s1.isalpha())

# string.isalnum()
'''Returns True when the string contains alphabets or numbers, otherwise returns False'''
print('s1.isalnum() =', s1.isalnum())

# string.isspace()
'''Returns True when the string contains only space(s) otherwise returns False'''
print('s1.isspace() =', s1.isspace())

# string.join('string')
'''Joins a sequence of string mentioned in its argument with the string'''
print('"-".join(s1) =', "-".join(s1))

# string.strip('string')
'''Deletes all the leading and trailing characters given in its argument'''
s3 = '*********Hello World********'
print('s3 =', s3)
print('s3.strip("*") =', s3.strip("*"))

# string.lstrip('string')
'''Deletes all the leading  characters given in its argument'''
print('s3.lstrip("*") =', s3.lstrip("*"))

# string.rstrip('string')
'''Deletes all the  trailing characters given in its argument'''
print('s3.rstrip("*") =', s3.rstrip("*"))

# min(string)
'''Returns minimum ASCII value alphabet'''
print('min(s1) =', min(s1), 'ASCII value of min:', ord(min(s1)))

# max(string)
'''Returns maximum ASCII value alphabet'''
print('max(s1) =', max(s1), 'ASCII value of max:', ord(max(s1)))

# string.replace(sub_string, new_string)
'''Replace the substring with a new string in a given string'''
print('s1.replace(s2, \'Hello\') =', s1.replace(s2, "Hello"))

# string.split()
''' which breaks a single string into a list of smaller strings based on a specified delimiter.
    By default, it splits the string wherever it finds whitespace (spaces, tabs, or newlines) and automatically removes those spaces.'''
print('s1.split() =', s1.split(), '\n')

print("Available methods in str")

for i, item in enumerate(dir(str)):
    print(item.ljust(22), end = "")
    if (i + 1) % 8 == 0:
        print()


