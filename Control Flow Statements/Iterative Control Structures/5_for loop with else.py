# Using else with for loop
'''
If the else statement is used with a for loop, the else statement is executed when the loop has exhausted iterating the list
'''
# Example 1 (prime number)
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)