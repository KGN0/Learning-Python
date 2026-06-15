# Random module
'''The random module provides access to functions that are used to generate or manipulate random number 
To import random module, write "import random" in shell or in your python scrpt'''

import random
# random Methods

# random.seed()
'''Initialize the random number generator'''
# Initialize the seed
# random.seed(42)
# Generate pseudo-random numbers
print(random.randint(1, 100))  # Output will always be 82
print(random.random())         # Output will always be 0.11133106816568039

# random.getstate() and random.setstate()
''' getstate Returns the current internal state of the random number generator
setstate restores the internal state of the random number generator
'''
# # 1. Capture the initial state
# saved_state = random.getstate()
# # 2. Generate random numbers
# print("First run:")
# print(random.randint(1, 100))
# print(random.random())
# # 3. Restore the state
# random.setstate(saved_state)
# # 4. Generate numbers again (they will be identical to the first run)
# print("\nSecond run (restored state):")
# print(random.randint(1, 100))
# print(random.random())

# random.getrandbits()
'''Returns a number representing the random bits'''
print(random.getrandbits(8))

# random.randrange(start, stop, step) stop is exclusive
'''Returns a random number between the given range'''
print(random.randrange(1, 100))

# random.randint(start, stop) stop is inclusive & step is not support
'''Returns a random number between the given range'''
print(random.randint(10, 99))


# random.choice(sequence)   sequence may be list, tuple, range(1, 10), string
'''Retuns a random element from the given sequence'''
fruit = ['banana', 'apple', 'grapes', 'orange', 'papaya', 'sappota']
print(random.choice(fruit))

# random.choices(sequence, k = no of elements)
'''Retuns a list with a random selection from the sequence'''
fruit = ['banana', 'apple', 'grapes', 'orange', 'papaya', 'sappota']
print(random.choices(fruit, k = 3))

# random.suffle(sequence)
'''Takes a sequence and returns the sequence in a random order'''
fruit = ['banana', 'apple', 'grapes', 'orange', 'papaya', 'sappota']
random.shuffle(fruit)
print(fruit)

# random.sample(sequence, k = no of elements <= len(sequence))  returns unique elements 
'''Returns a random sample of a sequence'''
fruits = ['banana', 'apple', 'grapes', 'orange', 'papaya', 'sappota']
sample = random.sample(fruits, k = 3)
print(sample)

# random.random()
'''Returns a random float number between 0 and 1'''
print(random.random())

# random.uniform()
'''Return a random float number between two given parameters'''
print(random.uniform(1, 10))

# random.triangular()
'''Returns a random float number between two given parameters, you can also set a mode parameter to specify
the midpoint between the two other parameters'''
print(random.triangular(1, 5, mode=3))



#1. betavariate(alpha, beta)Used in statistics to model percentages, probabilities, or proportions. The result is always strictly between 0 and 1.
# Inputs: alpha (\(>0\)) and beta (\(>0\)) control the shape of the curve.
# Models a distribution skewed toward 1
print(random.betavariate(alpha=5, beta=2))  # Example: 0.843

#.2. expovariate(lambd)Models the time or space between independent events occurring at a constant average rate. 
# It is heavily used to simulate waiting lines (queueing theory) or particle decay.Inputs: lambd (lambda) is 1.0 divided by the desired mean. 
# If positive, results range from 0 to positive infinity.
# Simulate arrival time when the average rate is 2 arrivals per minute
print(random.expovariate(lambd=2.0))  # Example: 0.314

#.3. gammavariate(alpha, beta)A highly flexible distribution used to model wait times, rainfall amounts, or insurance claims. 
# It is a continuous, right-skewed distribution starting at 0.Inputs: alpha (\(>0\)) is the shape parameter, and beta (\(>0\)) is the scale parameter.
print(random.gammavariate(alpha=9, beta=2))  # Example: 19.42

#.4. gauss(mu, sigma)Generates random numbers following a Normal (Gaussian) distribution ("bell curve"). 
# It is a faster, optimized version of normalvariate(), making it better for large loops, though it is slightly less thread-safe.
# Inputs: mu is the mean (center), and sigma is the standard deviation (spread).
# Mean height of 170cm, standard deviation of 10cm
print(random.gauss(mu=170, sigma=10))  # Example: 168.45

#.5. normalvariate(mu, sigma)Functions identically to gauss() by generating a standard normal "bell curve". 
# It uses a slower but more mathematically straightforward algorithm, ensuring it is completely thread-safe.
# Inputs: mu is the mean, and sigma is the standard deviation.
print(random.normalvariate(mu=0, sigma=1))  # Example: -0.432

#.6. lognormvariate(mu, sigma)Models data whose natural logarithm follows a normal distribution. 
# It is used heavily in finance to model stock prices, or in economics to model wealth distribution. Values are always greater than 0.
# Inputs: mu (mean) and sigma (standard deviation) of the underlying log-normal curve.
print(random.lognormvariate(mu=0, sigma=0.25))  # Example: 1.125

#.7. vonmisesvariate(mu, kappa)Designed for circular or directional data, such as compass headings, wind directions, or clock times.
# Inputs: mu is the mean angle in radians (between 0 and \(2\pi\)). kappa (\(\ge 0\)) is the concentration parameter (higher means values cluster tighter around the mean).
import math
# Mean direction is 90 degrees (pi/2 radians)
print(random.vonmisesvariate(mu=math.pi/2, kappa=4))  # Example: 1.482

#.8. paretovariate(alpha)Models the Pareto distribution ("80/20 rule"), where a small number of items account for the majority of the value. 
# Used to simulate wealth concentration, sizes of human settlements, or internet traffic file sizes.Inputs: alpha is the shape parameter. 
# Results are always \(\ge 1\).
print(random.paretovariate(alpha=1.16))  # Example: 3.421

#.9. weibullvariate(alpha, beta)Widely used in engineering and manufacturing for reliability and lifetime analysis (e.g., predicting when a mechanical part will fail).
# Inputs: alpha (\(>0\)) is the scale parameter, and beta (\(>0\)) is the shape parameter.
print(random.weibullvariate(alpha=25, beta=1.5))  # Example: 18.94


# Frequently used
'''
1. random
2. randint
3. randrange
4. choice
5. sample
'''