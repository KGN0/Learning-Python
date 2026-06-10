# Nested loops
'''
The loop within the loop is called nested loop
In nested while/ for loops, two or more while/for statemetns are included in the body of the body of the loop
The number of iterations in this type of structure will be equal to the number of iterations in the outer loop multiplied by the number of iterations in the inner loop
'''

# Nested for loops
'''
Syntax:
for iterating_var in sequence:
    for iterating_var in sequence:
        statements
    statements
'''

# Example 1
adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'mango']
for ad in adj:
    for fruit in fruits:
        print(ad, fruit)

# Exampole 2
for i in range(1, 5):
    for j in range( i):
        print("*", end= " ")
    print()

# Nested while loops
'''
while condition 1:
    statement
    statement
    while condition 2:
        statement
        break
    break
'''

# Example 1
n = int(input("Enter a value: "))
i = 2
while i <= n:
    print(i,"Table")
    j = 1
    while True:
        print(i * j, end = ' ')
        j += 1
        if j > 10:
            break
    print("\n")
    i += 1
