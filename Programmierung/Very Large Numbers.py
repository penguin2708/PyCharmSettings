import pandas as pd
import math
from decimal import *
# from tqdm.notebook import tqdm
from matplotlib import pyplot as plt

# import seaborn as sns

plt.style.use('fivethirtyeight')


def bin_prob1(n, p, k):
    arr = math.factorial(n) // math.factorial(k) // math.factorial(n - k)
    bp = arr * (p ** k) * ((1 - p) ** (n - k))
    return bp


def bin_prob2(n, p, k):
    # instantiate a Decimal context
    ctx = Context()
    # Python can make arbitrarily large integers, limited only by RAM
    # Use // to keep them integer
    arr = math.factorial(n) // math.factorial(k) // math.factorial(n - k)
    bp = Decimal(arr) * ctx.power(Decimal(p), Decimal(k)) * ctx.power(Decimal(1 - p), Decimal(n - k))
    return float(bp)




# number of objects picked from the pile
n = 20000
# fraction of the original pile that are type A
p = 0.2
df = pd.DataFrame({'probability': [0.0] * (n + 1)})

# compute probabilities for all k
for k in range(n + 1):
    df.loc[k] = bin_prob2(n, p, k)

print(df)

dfcs = df.cumsum()
dfcs.rename(columns={'probability': 'cumulative probability'}, inplace=True)
print(dfcs)

df.plot(figsize=(16, 9))
plt.show()
dfcs.plot(figsize=(16, 9))
plt.show()
