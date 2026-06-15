# Statistics Moudel
'''The module provides funtions for calculating mathematical statistics of numeric(Real valued) data
To import statistics module, write import statistics in shell or in your python scripts'''

import statistics

# statistics methods
#1. Averages and Central LocationThese functions determine the middle or most typical values within a dataset.

#  mean(data)
# Calculates the arithmetic average.
print(statistics.mean([1, 2, 3, 4, 4]))
# Output: 2.8

#fmean(data, weights=None)
# Faster, floating-point version of mean() supporting optional weights.
print(statistics.fmean([1, 2, 3], weights=[1, 2, 3]))  
# Output: 2.3333333333333335

# geometric_mean(data)
# Calculates the geometric mean (useful for growth rates and percentages).
print(statistics.geometric_mean([2, 4, 8]))  
# Output: 4.0

#harmonic_mean(data, weights=None)
# Calculates the harmonic mean (typically used for ratios and speeds).
print(statistics.harmonic_mean([40, 60]))  
# Output: 48.0

# median(data)
# Finds the exact middle value. If the dataset size is even, it returns the average of the two middle values.
print(statistics.median([1, 3, 5, 7]))  
# Output: 4.0

# median_low(data)
# Returns the smaller of the two middle values when the dataset size is even.
print(statistics.median_low([1, 3, 5, 7]))  
# Output: 3

# median_high(data)
# Returns the larger of the two middle values when the dataset size is even.
print(statistics.median_high([1, 3, 5, 7]))  
# Output: 5

#median_grouped(data, interval=1)
# Estimates the median for continuous data grouped into intervals.
print(statistics.median_grouped([52, 52, 53, 54]))  
# Output: 52.5

# mode(data)
# Returns the single most common data point.
print(statistics.mode([1, 1, 2, 3]))  
# Output: 1

# multimode(data)
# Returns a list of all most frequent values if there are multiple modes.
print(statistics.multimode([1, 1, 2, 2, 3]))  
# Output: [1, 2]

#2. Measures of Spread (Dispersion)
# These methods assess the variability or spread of values relative to their average.

# pvariance(data, mu=None)
# Calculates the population variance for an entire dataset.
print(statistics.pvariance([1, 2, 3, 4]))  
# Output: 1.25

#variance(data, xbar=None)
# Calculates the sample variance (uses n-1 denominator).
print(statistics.variance([1, 2, 3, 4]))  
# Output: 1.6666666666666667

#pstdev(data, mu=None)
# Calculates the population standard deviation.
print(statistics.pstdev([1, 2, 3, 4]))  
# Output: 1.118033988749895

#stdev(data, xbar=None)
# Calculates the sample standard deviation.
print(statistics.stdev([1, 2, 3, 4]))  
# Output: 1.2909944487358056

#quantiles(data, *, n=4, method='exclusive')
# Divides the dataset into n continuous intervals with equal probability and returns the cut points.
print(statistics.quantiles([1, 2, 3, 4, 5, 6, 7, 8], n=4))  
# Output: [2.25, 4.5, 6.75]

#3. Relationships Between Two InputsThese functions evaluate how two separate variables correlate with each other.
# covariance(x, y)
# Calculates sample covariance to determine directional associations.
print(statistics.covariance([1, 2, 3], [2, 4, 6]))  
# Output: 2.0

#correlation(x, y, *, method='linear')
# Calculates Pearson's correlation coefficient r (ranging from -1 to +1).
print(statistics.correlation([1, 2, 3], [2, 4, 6]))  
# Output: 1.0

#linear_regression(x, y, *, proportional=False)
# Computes the slope and intercept coefficients for a simple linear regression line using least squares.
print(statistics.linear_regression([1, 2, 3], [2, 4, 5]))  
# Output: LinearRegression(slope=1.5, intercept=0.33333)

#4. Probability Distributions and Mathematical Objects
# The module includes object-oriented tools for creating and transforming statistical distributions.
# print(statistics.NormalDist(mu=0, sigma=1)
# Creates a normal distribution instance for data manipulation and probability tests.
from statistics import NormalDist

# Instantiate a distribution
iq_dist = NormalDist(100, 15)

# Methods available on NormalDist instances:
iq_dist.mean                      # 100 (returns mean)
iq_dist.stdev                     # 15 (returns standard deviation)
iq_dist.variance                  # 225 (returns variance)
iq_dist.pdf(115)                  # Probability density function at x
iq_dist.cdf(115)                  # Cumulative distribution function up to x
iq_dist.inv_cdf(0.95)             # Value matching a cumulative probability
iq_dist.overlap(NormalDist(110, 10)) # Measures overlap between two distributions
iq_dist.samples(5)                # Generates a list of random samples

#If you want to view a quick structural list of all active attributes inside the module on your local system, run:
# print(dir(statistics))