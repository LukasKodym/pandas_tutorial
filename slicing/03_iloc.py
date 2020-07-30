# -*- coding: utf-8 -*-
# %%
##

import numpy as np
import pandas as pd

# %%
##
df = pd.DataFrame(np.random.randn(20, 5),
                  columns=list('abcde'),
                  index=list('abcdefghijklmnoprstu'))

# %% by col
##
# iloc[row_indexer, column_indexer]

col_1 = df.iloc[:, 0]
col_a_b = df.iloc[:, :2]
col_a_b_v2 = df.iloc[:, [0, 1]]

col_last = df.iloc[:, -1]
col_last_v2 = df.iloc[:, 4]

col_by_2 = df.iloc[:, ::2]

# %% by row
##
row_1 = df.iloc[0, :]
row_1_df = df.iloc[[0], :]
rows = df.iloc[[0, 5, 6], :]

row_last = df.iloc[-1, :]
row_last_df = df.iloc[[-1], :]

row_by_2 = df.iloc[::2, :]

# %%
##

df_ = df.iloc[[0, -1], [0, -1]]
