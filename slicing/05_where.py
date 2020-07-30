# -*- coding: utf-8 -*-
# %%
##

import numpy as np
import pandas as pd

# %%
##
s = pd.Series(np.random.randn(20))

df = pd.DataFrame(np.random.randn(31, 2),
                  columns=list('ab'),
                  index=pd.date_range('20190101', periods=31))

# %% Series
##
out = s[s > 0]
out = s.where(s > 0)

# %% DataFrame
##
out = df[df > 0]
out = df.where(df > 0)
out_2 = df.where(df > 0, 0)

out_3 = df.where(df > 0, 0).where(df < 1, 1)

# %% nadpisanie
##
df = df.where(df > 0, 0).where(df < 1, 1)
