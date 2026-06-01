# Logical operators
'''
Logical operators are used to form compound conditions which are a combination of more than one simple condition
Each of the simple conditions are evaluated first and based on the result compound condition is evaluated
The result of the expression is either True or False based on the result of simple conditions.
'''

# logical AND (and)
a = 5 
b = 4
c = 2
d = 8
print(f'{a} > {b} and {c} < {d} is', a > b and c < d)

print(f'{a} > {b} and {c} > {d} is', a > b and c > d)


# logical OR (or)
print(f'{a} > {b} or {c} > {d} is', a > b or c > d)
print(f'{a} < {b} or {c} < {d} is', a < b and c < d)

# logical NOT (not)
print(f"not ({a} < {b})", not (a < b))