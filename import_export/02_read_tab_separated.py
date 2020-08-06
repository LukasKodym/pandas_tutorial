# -*- coding: utf-8 -*-
# %%
##
import pandas as pd

# %% in older version sep='\t'
##
df = pd.read_csv('./data/apple.tsv', index_col=0)
