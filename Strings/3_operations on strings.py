# Operations on Strings
'''The + operator is called concatenation and is used to join or combine the strings 
Simarly the * operator is called the repetition operator and is used to repeat the string for several times'''
# Example: Usage of + and * operator in string
s1 = 'Hello'
s2 = "World"
s3 = 'Welcome to python'
print('\n',s1, '\n', s2, '\n',s3)
print('concatenation of above 3 strings')
print(s1 + s2 + s3)
print('\nmultipling string1 with 3')
print(s1 * 3)

# Example: Usage of append += operator in string
str1 = "Hello,"
name = input("Enter your name: ")
str1 += name
str1 += ". Welcome to python programming."
print(str1)

# Slicing the strings
'''A substring of a string is called a slice.
The slice operation is used to refer to sub-parts of sequences.
We can take subset of a string from the original string by using [] operator also konwn as slicing operator
The syntax used for slicing is:
Stringname[start:stop:stepsize]
The start and stop indicates the starting and ending index of the string. If start and stop values are not specified, 
then it is 0 to n -1. Similarly if stepsize is not specified then it is taken to be 1'''

# Example
str1 = 'PYTHON'
print(str1)
print('str1[1:5] =', str1[1:5])
print('str1[:6] =', str1[:6])
print('str1[1:] =', str1[1:])
print('str1[:] =', str1[:])
print('str1[1:20] =', str1[1:20])

# Example; Program to understand how characters in a string are accessed using negative indexs
str2 = 'PYTHON'
print(str2)
print('str2[-1] =', str2[-1])
print('str2[-6] =', str2[-6])
print("str2[-2:] =", str2[-2:])
print("str2[:-2] =", str2[:-2])
print("str2[-5:-2] =", str2[-5:-2])

# Specifying stride while slicing string
'''Which refers to the number of character to move forward after the first character is retrieved from the string
The default value of stride is 1'''
# Example: Program to use slice operation with stride(step)
str3 = 'Welcome to the world of python'
print(str3)
print('str3[2:10] =', str3[2:10]) # default value is 1
print('str3[2:10:1] =', str3[2:10:1])
print('str3[2:10:2] =', str3[2:10:2])
print('str3[2:13:4] =', str3[2:13:4])

# Example: Program to demonstrate slice operation with just last (positive) argument
str1 = 'Welcome to the world of python'
print('str1[:: 3] =', str1[::3])

# Example: Program to demonstrate slice operation with just last (negative) argument
str1 = 'Welcome to the world of python'
print('str1[:: -1] =', str1[::-1])