# Set comprehension
# set comprehensions are pretty similar to list comprehensions. It returns a set based on existing iterables. The difference is {}
# Syntax: {expression(variable) for variable in input_set [predicate][,...]}
# Example:
set1 = {x for x in range(1, 11,2)}
print('set1:', set1)
set2 = {x for x in range(1, 11)}
print('set2:', set2)
set3 = {x for x in set2 if x % 2 == 0}
print('set3:',set3)

# Example:- common numbers
set4 = {x for x in range(1, 11)}
set5 = {x for x in range(8)}
set6 = {x for x in set4 if x in set5}
print('\n',set4, '\n', set5, '\n', set6)