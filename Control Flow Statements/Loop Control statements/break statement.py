# break
'''
The break statement terminates the loop containg it
control of the program flows to the statement immediately after the body of the loop
The break statement inside the nested loop, the break statement will terminate the innermost loop

Syntax:
 break
 '''
# Example 1
for letter in 'Python':
    if letter == 'h':
        break
    print('Current letter: ', letter)


# Example 2
var = 10
while var > 0:
    print('Current variable value: ',var)
    var -= 1
    if var == 5:
        break
