# Recursive Functions
'''
The functions calls itself to solve a task until a fianl call is made which does not require a call to itself
Every recursive solution has two major cases
1. Base case:
    In base case in which the problem is simple to enough to be solved directly without making any further calls to the same function
2. Recursive case:
    In which first the problem is divided into simple sub-parts, second the function call itself but with sub parts of the problem obtained in the first step
    third the result is obtained by combining the solutions of simpler sub-parts
'''
# Example (factorial function)
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

result = fact(5)
print('Factorial of 5 is:', result)

# Example (fibonocci series)
def fibonocci(n):
    if n <= 0 :
        return 0
    elif n == 1:
        return 1
    else:
        return fibonocci(n - 1) + fibonocci(n - 2)

num = 5
for i in range(num):
    print(fibonocci(i), end = " ")


# Advantages of recursion
'''
    Recursive functions make the code look clean and elegant
    A complex task can be broken down into simpler sub - problems using recursion
    Sequence generator is easier with recursion
    It reduces time complexity
'''
# Disadvantages
'''
    Sometimes the logic behind recursion is hard to follow
    Recursion calls are inefficient as they take up a lot of memory and time
    They are hard to debug
'''