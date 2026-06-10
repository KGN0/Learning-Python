# While loops
'''
This is used whenever a set of statements should be repeated based on a condition
The while loop is entry control loop statements i.e. condition is evaluated first
if it is true then body of the loop is executed
The control comes out of the loop when the condition is false.
In while loop we must explicitly increment / decrement the loop variable

Syntax:
while condition:
    statement block
    increment / decrement
statement y

'''

# Example 1 (To display 1 - 10 numbers)
i = 1
while i <= 10:
    print(i, end = " ") # prints output in same line
    i += 1   # i = i + 1

# Example 2 (Addition of Natural numbers)

i = 1
total = 0  # to store the sum of the numbers one by one
while i <= 10:
    total = total + i
    i += 1
print(total)