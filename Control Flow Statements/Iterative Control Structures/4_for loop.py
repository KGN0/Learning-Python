# for loop
'''
It can be used to iterate over a list/ string/dictionary or iterate over a range of number
    If a sequence contains an expression list, it is evaluated first. Then, the first item in the sequence is assigned to the iterating variable iterating_var.
Next, the statement block is executed.

Syntax:
for variable in range(starting_num, ending_num + 1, step_size):
    statements

    or

for loop_control_var in sequence:
    statement block

'''

# Example 1: (print each character in the string)
string = "Python programming"
for char in string:
    print(char)

# Example 2: (print weekdays )
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for weekday in weekdays:
    print()
