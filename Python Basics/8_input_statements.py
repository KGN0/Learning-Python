# input statement
'''
python input funtion takes a single parameter that is a string
This string is often called the prompt because it contains some helpful text prompting the user to enter something
syntax is input([prompt])
where prompt is the string we wish to display on the screen. It is optional'''

# Example
n = input("Enter a number: ")
print("you entered", n, 'and type of n is', type(n))

'''
if you observe that actually you entered a number but it return string
to convert this into  we use type conversion'''

m = int(n)
print('after type conversion the number is', m, 'and type of number is', type(m))

# Example

name = input("What is your name?: ")
age = int(input("What is your age?: "))
print(name, "'your's age is:",age)