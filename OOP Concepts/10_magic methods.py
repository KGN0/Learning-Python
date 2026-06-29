'''These are special methods. These are also known as denders. Magic methods are used for converting objects to built in types
we have seen __init__, but now there are several other methods to allow operators such as +, -, *, / and many other operations
which are having double underscore at the beginning end of their names like __add__ for +, __sub__ for -'''

# Example 1
class Add:
    def __init__(self, a):
        self.a = a
    def __add__(self, other):
        return self.a + other.a
obj1 = Add(4)
obj2 = Add(3)
result = obj1 + obj2
print('Result:', result)

# Example 2
class Sub:
    def __init__(self, a):
        self.a = a
    def __sub__(self, other):
        return self.a - other.a
obj1 = Sub(7)
obj2 = Sub(3)
result = obj1 - obj2
print('Result:', result)

# Example 3
class Mul:
    def __init__(self, a):
        self.a = a
    def __mul__(self, other):
        return self.a * other.a
obj1 = Mul(3)
obj2 = Mul(3)
result = obj1 * obj2
print('Result:', result)

# Example 4
class Truediv:
    def __init__(self, a):
        self.a = a
    def __truediv__(self, other):
        return self.a / other.a
obj1 = Truediv(4)
obj2 = Truediv(3)
result = obj1 / obj2
print('Result:', result)

# Example 5
class Floordiv:
    def __init__(self, a):
        self.a = a
    def __floordiv__(self, other):
        return self.a // other.a
obj1 = Floordiv(3)
obj2 = Floordiv(3)
result = obj1 // obj2
print('Result:', result)

# Example 5 
class Mod:
    def __init__(self, a):
        self.a = a
    def __mod__(self, other):
        return self.a % other.a
obj1 = Mod(5)
obj2 = Mod(3)
result = obj1 % obj2
print("Result:", result)

# Example 6
class Div:
    def __init__(self, a):
        self.a = a
    def __divmod__(self, other):
        # Always check if 'other' is the correct type
        if isinstance(other, Div):
            # Calculate floor division and modulo of the underlying values
            quotient = self.a // other.a
            remainder = self.a % other.a
            return (quotient, remainder)
        return NotImplemented
obj1 = Div(10)
obj2 = Div(3)
# Use the built-in divmod() function
result = divmod(obj1, obj2)
print('Result (Quotient, Remainder):', result)

# Example 7
class Pow:
    def __init__(self, a):
        self.a = a
    def __pow__(self, other):
        return self.a ** other.a
obj1 = Pow(5)
obj2 = Pow(3)
result = obj1 ** obj2
print("Result:", result)

# Example 8
class And:
    def __init__(self, a):
        self.a = a
    def __and__(self, other):
        return self.a & other.a
obj1 = And(5)
obj2 = And(2)
result = obj1 & obj2
print('Result:', result)

# Example 9
class Or:
    def __init__(self, a):
        self.a = a
    def __or__(self, other):
        return self.a | other.a
obj1 = Or(5)
obj2 = Or(2)
result = obj1 | obj2
print('Result:', result)

# Example 10
class Xor:
    def __init__(self, a):
        self.a = a
    def __xor__(self, other):
        return self.a ^ other.a
obj1 = Xor(5)
obj2 = Xor(2)
result = obj1 ^ obj2
print('Result:', result)

# Example 11
class lt:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        return self.a < other.a
obj1 = lt(5)
obj2 = lt(2)
result = obj1 < obj2
print('Result:', result)

# Example 12
class gt:
    def __init__(self, a):
        self.a = a
    def __gt__(self, other):
        return self.a > other.a
obj1 = gt(5)
obj2 = gt(2)
result = obj1 > obj2
print('Result:', result)

# Example 13
class eq:
    def __init__(self, a):
        self.a = a
    def __eq__(self, other):
        return self.a == other.a
obj1 = eq(5)
obj2 = eq(2)
result = obj1 == obj2
print('Result:', result)

# Example 14
class ne:
    def __init__(self, a):
        self.a = a
    def __ne__(self, other):
        return self.a != other.a
obj1 = ne(5)
obj2 = ne(2)
result = obj1 != obj2
print('Result:', result)

# Example 15
class ge:
    def __init__(self, a):
        self.a = a
    def __ge__(self, other):
        return self.a >= other.a
obj1 = ge(5)
obj2 = ge(2)
result = obj1 >= obj2
print('Result:', result)

# Example 16
class le:
    def __init__(self, a):
        self.a = a
    def __le__(self, other):
        return self.a <= other.a
obj1 = le(5)
obj2 = le(2)
result = obj1 <= obj2
print('Result:', result)

# Example 17
class Iadd:
    def __init__(self, a):
        self.a = a
    def __iadd__(self, other):
        return self.a + other
obj1 = Iadd(3)
obj1 += 5
print('Result:', obj1)

# Example 18
class Radd:
    def __init__(self, a):
        self.a = a
    def __radd__(self, other):
        return self.a + other
obj1 = Radd(4)
result = 5 +  obj1
print('Result:', result)

# Example 19
class Stud:
    def __init__(self, name, idno):
        self.name = name
        self.idno = idno
    def __repr__(self):
        return "student ('{}, '{}')".format(self.name, self.idno)
stud = Stud('abc', 189)
print(repr(stud))

# Example 20

class Len:
    def __init__(self, a):
        self.a = a
    def __len__(self):
        return len(self.a)
obj1 = Len("Hello")
print('Result:', len(obj1))