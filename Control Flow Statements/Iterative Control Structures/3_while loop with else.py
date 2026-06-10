# Using else statement with while statement
'''
Python supports to have an else statement assocaited with a loop statement
If else statement is used with a while loop, the esle statement is executed when the condition becomes false
'''

# Example 1
count = 0
while count < 5:
    print(count, "is less than 5")
    count += 1
else:
    print(count, "is not less than 5")

# Example 2
''' 
In this example else part is not executed because loop is terminated using break statement
'''
count = 0
while count < 5:
    print(count, "is less than 5")
    count += 1
    if count == 3:
        break # it is used to exit from the loop
else:
    print(count, "is not less than 5")