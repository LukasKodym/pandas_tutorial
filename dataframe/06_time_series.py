# -*- coding: utf-8 -*-
# %%
##
import pandas as pd
import numpy as np

# %%
##
np.random.seed(0)
index = pd.date_range('01-01-2019', periods=10000)

df = pd.DataFrame(np.random.randn(10000), index=index)

# %%
##
df_cunsum = df.cumsum()
df_cunsum.plot(kind='line')
