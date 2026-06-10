# Range function
'''
The range() is a built in function in python that is used to iterate over a sequence of numbers

Syntax:
range(beg, end, [step])

By default range is increment by 1. But if we want to specify different increment using step'''

# Example 1
print('range(1, 5 + 1)')
for number in range(1, 5 + 1):
    print(number, end = " ")