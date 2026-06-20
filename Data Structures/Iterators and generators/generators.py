# Generators

# Making generator
nested_list = [[1,2], [3,4],[5]]
def func(nested_list):
    for sublist in nested_list:
        for elmt in sublist:
            yield elmt

for num in func(nested_list):
    print(num)

'''Differnce between normal function and generator 
normal function return one value, but generator yield several values one at a time
when it is, it resumes it execution at the point where it stopped'''

# Example
def mygenerator():
    print('First item')
    yield 10
    print('Second item')
    yield 20
    print('Third item')
    yield 30

gen = mygenerator()
print(next(gen))
print(next(gen))
print(next(gen))

# Example
def mygenerator1():
    print('First item')
    yield 10
    return          # if we use return it stops execution
    print('Second item')
    yield 20
    print('Third item')
    yield 30

gen = mygenerator1()
print(next(gen))
# print(next(gen))  # raise stop iteratin error
# print(next(gen)) 


# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    yield n
    n += 1
    print('This is printed second')
    yield n
    n += 1
    print('This is printed last')
    yield n
    
for item in my_gen():
    print(item)