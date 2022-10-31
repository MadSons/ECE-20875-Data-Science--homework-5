import math as m
import numpy as np
import scipy.stats as stats

# import or paste dataset here
data = [3, -3, 3, 12, 15, -16, 17, 19, 23, -24, 32, 10, -4]

# code for question 1
print('Problem 1 Answers:')
# code below this line
c = 0.9  # confidence interval
s_mean = np.mean(data)
n = len(data)
df = n - 1  # degrees of freedom
s_sd = np.std(data, ddof=1)
SE = s_sd / m.sqrt(n)
t_c = stats.t.ppf(1 - (1 - c) / 2, df)
l_c = s_mean - (t_c * SE)
u_c = s_mean + (t_c * SE)

print(f'  Sample Mean: {s_mean}')
print(f'  Standard Error: {SE}')
print(f'  t-value: {t_c}')
print(f'  {c*100}% confidence interval = ({l_c},{u_c})')

# code for question 2
print('Problem 2 Answers:')
# code below this line
new_c = 0.95
new_t_c = stats.t.ppf(1 - (1 - new_c) / 2, df)
new_l_c = s_mean - (new_t_c * SE)
new_u_c = s_mean + (new_t_c * SE)
print(f'  Sample Mean: {s_mean}')
print(f'  Standard Error: {SE}')
print(f'  t-value: {new_t_c}')
print(f'  {new_c*100}% confidence interval = ({new_l_c},{new_u_c})')

# code for question 3
print('Problem 3 Answers:')
# code below this line
c = 0.95
p_sd = 15.836
SE = p_sd / m.sqrt(n)
z_c = stats.norm.ppf(1 - (1 - c) / 2)
l_c = s_mean - SE * z_c
u_c = s_mean + SE * z_c
print(f'  Standard Error: {SE}')
print(f'  Z-Value: {z_c}')
print(f'  95% confidence interval = ({l_c},{u_c})')

# code for question 4
print('Problem 4 Answers:')
# code below this line
t_c = s_mean / SE
p = 2 * stats.t.cdf(-abs(t_c), df)
c = 1 - p
print(f'{c} level of confidence the team will win on average')
