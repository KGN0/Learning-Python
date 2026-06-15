# Strings
'''
The python string data type is a sequence made up of one or more individual characters characters, 
where a character could be a letter, digit, whitespace, or any other symbol.
Python treats strings as contigous series of characters delimited by single, double or even triple quotes'''

# Working with strings
# Example (create strings in three different ways - using single, double and triple quotes)
s1 = 'Hello'
print(s1)
s2 = "Python"
print(s2)
s3 = '''
Welcome 
to python
programming'''
print(s3)

# Example (display single and double quotes in string)
print('Hello Mr.John')
print("How are you \"Mr.Shyam\"")
print('I am "Loving it"')

# Strings are immutable
'''Python strings are immutable which means that once created they cannot be changed
Whenever you try to modify an existing string variable, a new string is created'''

# Example (program to demonstrate string references using the id() function)
str1 = "Hello"
print("Str1 is:", str1)
print("ID of str1 is:", id(str1))
str2 = "World"
print("Str2 is:", str2)
print("ID of str2:", id(str2))
str1 += str2
print("Str1 after concatenation is:", str1)
print("ID of str1 is:", id(str1))
str3 = str1
print("Str3=",str3)
print("Id of str3 is:", id(str3))

# Indexing
''' Individual characters in a string are accessed using the subscript([]) operator
    The expression in brackets is called an index.
    Index starts from 0 and that of the last character is n-1 where n is the no of characters in the string'''
# Example
sample = 'Hello, this is a sample string'
print("Character at index 5 is: ",sample[5])

# we can also access the character in string using negative indexing i.e
# string[-1] will return the last character of string
# string[-2] will return the second last character of string

print("Last character in string:", sample[-1])
print('Second last character in string:', sample[-2])

# Modifying characters in string using []
'''Python strings are immutable, therefore we can not change content of string using[] operator.
    if we try to modify the string with [] then it will return error '''
# Example
sample  = 'hello, this is a sample string'
# sample[5] = 's' returns typeError

# Accessing out of range character in python string
# Example
# sample[50]  raise Index: Out of range error

# Updating or Deleting a String  in Python
# Example
string1 = 'Python Programming'
print('original string:')
print(string1)
string1 = 'Welcome to Python'
print("Updated String:")
print(string1)

# Example (python code to delete an entire string)
string1 = 'Python Programming'
print(string1)
del string1
# print(string1) Raise NameError name string1 is not defined

