# Output statement
'''
The simplest way to produce output is using the print statement
where we can pass zero or more expressions seperated by commas
we use the print() function to output data to the standard output device'''

# Example
print("Output to the screen")

a = 3.14
print('The value of a is', a)

'''
By default the separated comma produce a single space between string and value a 
but we change it
syntax: print(*objects, sep = "")'''

# Example
print(1,2,3,4,5)
# sep
print(1,2,3,4,5, sep = "*") # now space is replaced by "*"

# end
'''
It defaults into a new line 
but it is also we can change'''

# before using end as default
print(1)
print(2)

# after end is modified
print(1, end = " ")
print(2)

# there are different type formats to print output
# 1. expressions are seperated by comma
a = 4
b = 2
c = a + b
print('The addition of', a, 'and', b, 'is', c)

# 2. using f-strings
a = 3
b = 1
c = a - b
print(f"The subtraction of {a} and {b} is {c}")

# 3. using % operator
a = 9
b = 9
c = a * b
print("The multiplication of %d and %d is %d" %(a, b, c)) # for int - d, float - f, string - s

# using str.format() method
a = 1
b = 1
c = a / b
print('The division of {} and {} is {}'.format(a, b, c))

# we can also use default arguments
print('The division of {x} and {y} is {z}'.format(z = c, x = a, y = b))