# if else statement
'''
The two way decision making statements and always used in conjuction with condition
It is used to control flow execution and used to carry out the logical test  and 
then pickup the two possible actions depending on the logical test.

Syntax:
if test_expression:
    true statement block 1
else:
    false statement block 2
statement x
'''

# Example 1 (print even or odd number)
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Example 2 (Eligible for vote or not)
age = int(input("Enter your age: "))
if age >= 18:
    print("You are egilible for vote.")
else:
    print("You are not eligible for vote.")