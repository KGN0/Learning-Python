# if-elif-else statement
'''
Python supports if-elif-else statements to test additional conditions apart from the intial test expression
The if-elif-else works in the same way as if-else statement.
The if-elif-else also known as nested-if. But nested if statements can become quite complex if there are more than 3 alternatives. indentation is not consistent
if one condition is TRUE remaining is not executed.

Syntax:
if test_expression 1:
    statement-block 1
elif test_expression 2:
    statement-block 2
elif test_expression n:
    statement-block n
else:
    statement-block x
statement y

'''

# Example 1 (Is number positive or negative)
num = int(input("Enter a number: "))
if num == 0:
    print("Number is zero.")
elif num > 0:
    print("Number is positive.")
else:
    print("Number is negative.")

'''
If you want to test more than one condition in if statement, the logical operators are used they are used to combined the results of two or more conditions
'''

# Example
num = int(input("Enter a number: "))
if (num > 10 and num < 20):
    print("Number between 10 and 20")
else:
    print("Number is either < 10 or > 20")