'''
These may be situations where a statement or group of statements are associated with a control statement or a function.
Such a statement or group of statements is referred to as a block or code block
'''
# code that find the positive difference between 'a' and 'b'
# The below code will be explain later

a = 5
b = 10
if (a > b):
    d = a - b
    print("a is greater than b, and")
    print("they differ by", d)
else:
    d = b - a
    print("b is greater than a, and")
    print("they differ by", d)