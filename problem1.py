import numpy as np
import math as m
import scipy.stats as stats
from scipy.stats import norm
from scipy.stats import t

# import or paste dataset here
file_0 = open('engagement_0.txt')  # students who did not demonstrate knowledge
data_0 = file_0.readlines()
file_0.close()
data_0 = [float(x) for x in data_0]

file_1 = open('engagement_1.txt')  # students who did demonstrate knowledge
data_1 = file_1.readlines()
file_1.close()
data_1 = [float(x) for x in data_1]

# calculate general statistical variables
samp_mean_0 = np.mean(data_0)
sd_0 = np.std(data_0, ddof=1)  # ddof = 1 for a sample, divides by N-1 instead of N.

samp_mean_1 = np.mean(data_1)
sd_1 = np.std(data_1, ddof=1)

# code for question 2
print('Problem 2 Answers:')
# code below this line
pop_mean = 0.75
n_1 = len(data_1)
SE_1 = sd_1 / m.sqrt(n_1)
zscore_1 = (samp_mean_1 - pop_mean) / SE_1
p_1 = 2 * stats.norm.cdf(-abs(zscore_1))
print(f'  Sample Size: {n_1}')
print(f'  Sample Mean: {samp_mean_1}')
print(f'  Standard Error: {SE_1}')
print(f'  Standard Score: {zscore_1}')
print(f'  P-Value: {p_1}')

# code for question 3
print('Problem 3 Answers:')
# code below this line
new_z_1 = stats.norm.ppf(0.05 / 2)
new_SE_1 = (samp_mean_1 - pop_mean) / new_z_1
new_n_1 = (sd_1 / new_SE_1) ** 2
print(f'  Largest Standard Error for significance of 0.05: {new_SE_1}')
print(f'  Corresponding minimum sample size: {m.ceil(new_n_1)}')

# code for question 5
print('Problem 5 Answers:')
# code below this line
n_0 = len(data_0)
sd = m.sqrt((sd_0**2) / n_0 + (sd_1**2) / n_1)
test_samp_mean = samp_mean_0 - samp_mean_1
test_pop_mean = 0
z = (test_samp_mean - test_pop_mean) / sd
p = 2 * stats.norm.cdf(-abs(z))
print(f'  Sample Size engagement_0: {n_0}, Sample Size engagement_1: {n_1}')
print(f'  Sample Mean engagement_0: {samp_mean_0}, Sample Mean engagement_1: {samp_mean_1}')
print(f'  Standard Error: {sd}')
print(f'  Standard Score: {z}')
print(f'  P-Value: {p}')

