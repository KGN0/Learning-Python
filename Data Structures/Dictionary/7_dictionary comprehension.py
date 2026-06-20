# Dictionary comprehension
'''Dictionary comprehension is an elegant and concise way to create new dictionaries using iterative way in python
It is created by writing an expression pair or key: value pair followed by a for loop inside curly braces {}
Syntax: dictionary = {key:value for var in iterable}'''
# Example:- square of a number
square_dict = {x: x*x for x in range(1, 11)}
print(square_dict)

# Example:- filtering even number aged persons
original_dict = {'Ramesh':38, 'Raghav':48, 'Rahul':57, 'Rohan':33}
even_dict = {k:v for (k, v) in original_dict.items() if v % 2 == 0}
print(even_dict)

# Example:- display old or yound based on age > 40
original_dict = {'Ramesh':38, 'Raghav':48, 'Rahul':57, 'Rohan':33}
age_dict = {k:'Old' if age > 40 else 'Young' for k, age in original_dict.items()}
print(age_dict)

# create dictionary from two list using zip() method
keys = ['A', 'B', 'C', 'D', 'E']
values = [1,2,3,4,5]
new_dict = {key:value for key, value in zip(keys, values)}
print(new_dict)