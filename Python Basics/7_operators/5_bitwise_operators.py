# Bitwise operators
'''
Bitwise operators acts on individual bits of the operands
These operators directly act on binary numbers
If we want to use these operators on the integers then first these numbers are converted into binaary numbers'''

# Bitwise AND (&)
a = 10 
b = 11
print(f"a = {a}\nb = {b}")
c = a & b
print(f'a & b is {c}')

# Bitwise OR (|)
c = a | b
print(f'a | b is {c}')

# Bitwise XOR (^)
c = a ^ b
print(f'a ^ b is {c}')

# Bitwise complement (~)
c = ~ a
print(f'~ a is {c}')

c = ~ b
print(f'~ b is {c}')

# Bitwise left shift (<<)
c = a << 2
print(f'a << 2 is {c}')

# Bitwise right shift (>>)
c = a >> 2
print(f'a >> 2 is {c}')
