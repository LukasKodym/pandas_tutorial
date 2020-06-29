# -*- coding: utf-8 -*-

# %%
##

import pandas as pd
import numpy as np

# %%
## Example 1

s = pd.Series(4)

# %%
## Example 2

s_def = pd.Series(data=[21, 34, 54], index=['adam', 'tomek', 'pawel'],
                  name='age')

# %%
## Example 3

A = np.random.randn(10)
s = pd.Series(A)

# %%
## Example 4

stocks = {'Apple': 'USA', 'CD Project': 'Poland', 'Amazon': 'USA'}
series = pd.Series(stocks, name='country')

# %%
## Example 5

stocks_price = {'Apple': 196, 'CD Project': 215, 'Amazon': 1877}
stock_price_series = pd.Series(stocks_price, name='price')

stock_price_array = stock_price_series.values

apple_price = stock_price_series['Apple']

'Apple' in stock_price_series

# %%
## Example 6

np.random.seed(0)

A = np.random.randn(20)
s = pd.Series(A)

s[0]
s[1]
s[5:10]
s[:10]
s[5:]
