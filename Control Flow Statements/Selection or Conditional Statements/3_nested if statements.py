# Nested if statements
'''
A statement that contains other statements is called a compound statement.
To perfom operations if statements can be nested, that can be placed inside the other

Syntax:
if test_expression 1:
    if test_expression 2:
        true statement block 2
    else:
        false statement block 3
else:
    false statement block 1
statement n

'''

# Example 1 (is number positive or negative)

num = int(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print('Number is zero.')
    else:
        print("Positive Number.")
else:
    print("Negative number.")

# Example 2

num = int(input("Enter a number: "))
if num < 20:
    if num < 15:
        print('Number is smaller than 15')
    if num < 12:
        print('Number is smaller than 12 too')
else:
    print("Number is greater than 15")