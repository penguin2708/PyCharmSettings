import pandas as pd
import math


def binomial_coefficient(n, k):
    coeff = math.factorial(n) / math.factorial(k) / math.factorial(n - k)
    return coeff


n = 100
df_coeff = pd.DataFrame({'coefficient': [0.0] * (n + 1)})

for k in range(n + 1):
    df_coeff.loc[k] = binomial_coefficient(n, k)
