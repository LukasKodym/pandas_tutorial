# -*- coding: utf-8 -*-
# %%
##
import pandas as pd

# %%
##
df = pd.read_csv('./data/cdr.csv', sep=',', index_col=0)

# %%
##
df_ = pd.read_csv('./data/cdr.csv', sep=',', index_col=0, skiprows=10)

# %%
##
df_ = pd.read_csv('./data/cdr.csv', sep=',', index_col=0, nrows=10)

# %%
##
df = pd.read_csv('./data/reviews_clean.csv')
