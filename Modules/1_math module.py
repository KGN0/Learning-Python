# Module
'''
Basically, a module in python is a file containg definations of functions, classes, variables, constnats or other python objects. 
Contents of this file can be made availalbe to any other program'''

# Math module
# The math module provides access to the mathematical functions
# To import module, write import math in shell or in your python scripts/program

import math
# Math methods

# math.acos(x) -1 <= x <= 1
'''Returns the arc cosine of a number'''
result_radians = math.acos(0.5) 
print(result_radians)

# math.acosh(x) x >= 1
'''Returns the inverse hyperbolic cosine of a number'''
result_radians = math.acosh(10) 
print(result_radians)

# math.asin(x) -1 <= x <= 1
'''Returns the arc sine of a number'''
result_radians = math.asin(1) 
print(result_radians)

# math.asinh(x) -inf < x < inf
'''Returns the inverse hyperbolic sine of a number'''
result_radians = math.asinh(30) 
print(result_radians)

# math.tan(x) x ia any real number
'''Returns the arc tangent of a number in radians'''
result_radians = math.atan(54) 
print(result_radians)

# math.atan2(y, x) -inf < x, y < inf , x != 0
'''Return the arc tangent of y/x in radians'''
result_radians = math.atan2(10,30) 
print(result_radians)

# math.atanh(x) -1 < x < 1
'''Returns the inverse hyperbolic tangent of a number'''
result_radians = math.atanh(0.9) 
print(result_radians)

# math.ceil(x) x is any real number
'''Rounds a number up to the nearest integer'''
result = math.ceil(36.345) 
print(result)

# math.comb(n, k)    - n! / (k! *(n -k)!)
'''Returns the number of ways to choose k items from n items from n items without repetition and order'''
result = math.comb(10,3)  
print(result)

# math.copysign(x, y)
'''Returns a float consisting of the value of the first parameter and the sign of the second parameter'''
result = math.copysign(100,-10) 
print(result)

# math.cos(x) -inf < x < inf
'''Returns the cosine of a number'''
result_radians = math.cos(2) 
print(result_radians)

# math.cosh(x) -inf < x < inf
'''Returns the hyperbolic cosine of a number'''
result_radians = math.cosh(3) 
print(result_radians)

# math.degrees()
'''Converts the angle from radians to degree'''
result_radians = math.degrees(math.cos(4)) 
print(result_radians)

# math.dist([x1, y1], [x2, y2])
'''Returns the Euclidean distance between two points x, y where x and y are the coordinates of that number'''
result = math.dist([10,30], [10, 20]) 
print(result)

# math.erf(x) -inf < x < inf
'''Returns the error function of a number'''
result = math.erf(float('inf')) 
print(result)

# math.erfc(x) 1 - erf(x)
'''Returns the complementary error function of a number'''
result = math.erfc(30) 
print(result)

# math.exp(x)  
'''Returns E raised to the power of x'''
result = math.exp(2) 
print(result)

# math.expm1()
'''Returns Ex - 1'''
result = math.expm1(3) 
print(result)

# math.fabs(x)
'''Returns the abs value of a number'''
result = math.fabs(-30.32) 
print(result)

# math.factorial(x)
'''Returns the factorial of a number'''
result = math.factorial(6) 
print(result)

# math.floor(x)
'''Returns a number down to the nearest integer'''
result = math.floor(43.89)
print(result)

# math.fmod(x, y)
'''Returns the remainder of x/y'''
result = math.fmod(30, 4) 
print(result)

# math.frexp(x)
'''Returns the mantissa and the exponent, of a specified number'''
result = math.frexp(30) 
print(result)

# math.fsum(x)
'''Return the sum of all items in any iterable(tuple, arrays, lists, etc)'''
result = math.fsum([1,2,3,4,5,6]) 
print(result)

# math.gamma(x)
'''Returns the gamma function of x'''
result = math.gamma(3) 
print(result)

# math.gcd(x, y)
'''Returns the greatest common divisor of two integers'''
result = math.gcd(30, 21) 
print(result)

# math.hypot(*num)
'''Returns the Euclidean norm'''
result = math.hypot(30, 20) 
print(result)

# math.isclose(x, y)
'''Checks whether two values are close to each other, or not'''
result = math.isclose(30, 31) 
print(result)

# math.isfinite(x)
'''Checks whether a number is finite or not'''
result = math.isfinite(3489220984897209) 
print(result)

# math.isinf(x)
'''Checks whether a number is infinite or not'''
result = math.isinf(float('inf')) 
print(result)

# math.isnan(x)
'''Checks wheter a value is Nan(not a number) or not'''
result = math.isnan(20) 
print(result)
result = math.isnan(float('nan')) 
print(result)

# math.isqrt(x)
'''Rounds a square root number downwards to the nearest integer'''
result = math.isqrt(50)
print(result)

# math.ldexp(x, i)
'''Returns the inverse of math.frexp() which is x * (2**i) of the given numbers x and i'''
result = math.ldexp(30, 3) 
print(result)

# math.lgamma(x)
'''Returns the log gamma value of x'''
result = math.lgamma(30) 
print(result)

# math.log(x)
'''Returns the natural logarithm of a number, or the logarithm of number to base'''
result = math.log(53) 
print(result)

# math.log10(x)
'''Returns the base-10 logarithm of x'''
result = math.log10(53) 
print(result)

# math.log1p(x)
'''Returns the natural logarithm of 1 + x'''
result = math.log1p(53) 
print(result)

# math.log2(x)
'''Returns the base-2 logarithm of x'''
result = math.log2(53) 
print(result)

# math.perm(n, k)
'''Returns the number of ways to choose k itme from n items with order and without repetition'''
result = math.perm(30, 2) 
print(result)

# math.pow(x , y)
'''Return sthe value of x to the power of y'''
result = math.pow(30, 2) 
print(result)

# math.prod(*num)
'''Returns the product of all the elements in an iterable'''
result = math.prod([1,2,3,4,5]) 
print(result)

# math.radians(x)
'''Converts a degree value into radians'''
result = math.radians(30) 
print(result)

# math.remainder(x, y)
'''Returns the closest value that can make numerator completely divisible by the denominator'''
result = math.remainder(30, 4) 
print(result)

# math.sin(x) -inf < x < inf
'''Return the sine of a number'''
result_radians = math.sin(10) 
print(result_radians)

# math.sinh(x) -inf < x < inf
'''Returns the hyperbolic sine of a number'''
result_radians = math.sinh(10) 
print(result_radians)

# math.sqrt(x)
'''Returns the square root of a number'''
result = math.sqrt(36) 
print(result)

# math.tan(x)
'''Returns the tangent of a number'''
result_radians = math.tan(10) 
print(result_radians)

# math.tanh(x) -inf < x < inf
'''Returns the hyperbolic tangent of a number'''
result_radians = math.tanh(10) 
print(result_radians)

# math.trunc(x)
'''Returns the truncated integer parts of a number'''
result = math.trunc(31.9) 
print(result)

# Math constants

# math.e
'''Returns Euler's number(2.7182)'''
print(math.e)

# math.inf
'''Return a floating-point positive infinity'''
print(math.inf)
print(float('inf'))

# math.nan
'''Returns a floating-point NaN (Not a Number) value'''
print(math.nan)

# math.pi
'''Return PI (3.14159)'''
print(math.pi)

# math.tau
'''REturn tau (6.2831)'''
print(math.tau)

# Frequenty used mathematical functions
'''
1. sqrt()
2. ceil()
3. floor()
4. pow()
5. fabs()
6. sin()
7. cos()
8. tan()
'''