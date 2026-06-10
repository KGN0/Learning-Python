# pass statement
'''
The pass statement is a null statement
But the difference between pass and comment is that comment is ignored by the interpreter whereas pass in not ignored.
The pass statement is generally used as a placeholder
Syntax: pass
'''

for letter in 'ABCDEF':
    if letter == " ":
        pass
    else:
        print("Current letter",letter)