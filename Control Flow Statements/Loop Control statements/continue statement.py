# continue statement
'''
The continue statement instructs a loop to continue to the next iteration
Any code that follows the continue statemtn is not executed
Unlike a break statement, a continue statement does not completely halt the loop

Syntax: continue
'''

# Example 1
students = ['praveen', 'kumar', 'palla']
for student in range(0,len(students)):
    if students == 2:
        continue
    else:
        print(students[student])
        