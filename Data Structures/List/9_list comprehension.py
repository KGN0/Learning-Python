# List comprehension
'''
Comprehensions are constructs that allow sequences to be built from other sequences
A list comprehension consists of the following parts
- An input sequence
- Variable representing members of the input sequence
- An optional predicate expression
- An output expression producing elements of the output list from members of the input sequence that statisfy the predicate

Syntax: [expression for item in list if expression]
this is equivalent to:
    for item in list:
        if conditional:
            expression'''

# Example
a_list = [1, 4, 9, 'a', 0, '4']
squared_list = [e ** 2 for e in a_list if type(e) == int]
# or
squared_list = [e ** 2 for e in a_list if isinstance(e, int)]
print(squared_list)

# Example
x = [i for i in range(1, 11)]
print(x)

# Example
string = ['this', 'is', 'an', 'example']
items = [word[0] for word in string]
print(items)

# Example
squares = [i ** 2 for i in range(1, 11)]

# Example
value = [x + y for x in [1, 2, 3] for y in [3, 2, 1]]
print(value)

# Example 
nums = [i for i in range(1, 51)]
even_nums = [i for i in nums if i % 2 == 0]
odd_nums = [i for i in nums if i % 2 != 0]
prime_nums = [i for i in nums if i > 1 and all( i % j != 0 for j in range(2, int(i ** 0.5) + 1))]
print(even_nums)
print(odd_nums)
print(prime_nums)

# Example
lst1 = [1, 2, 4, 6]
lst2 = [1, 3, 4, 5, 8, 0]
common_elements = [i for i in lst1 if i in lst2]
print(common_elements)

# Example
num_list = [i for i in range(1, 11)]
total = 0
for i in num_list:
    total += i
print(total)

# using list comprehension
total = 0
sum_list = [total:= total + i for i in num_list]
print(sum_list[-1])
