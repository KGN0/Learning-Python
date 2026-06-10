# Selection / Conditional Statements
'''
The selection control flow usually jumps from one part of the code to another depending on whether a particular condition is satisfied or not
'''
'''
1. if statement
2. if ... else statement
3. nested if ... else statement
4. if-elif-else ladder
'''
# if statement
'''
The if statement is the simplest form of decision control statement
that is frequently used in decision making.
The general form of simple if statement is as follows

Syntax:
if test_expression:
    true statement 1
    statement n
statement x

'''

# Example 1
temp = 5
if temp < 10:
    print("Its cold")

# Example 2 (swapping two numbers)
a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
if a > b:
    temp = a
    a = b
    b = temp
print("The swapped numbers are:", a, b)