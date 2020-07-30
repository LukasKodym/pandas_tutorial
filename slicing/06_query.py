# -*- coding: utf-8 -*-
# %%
##

import numpy as np
import pandas as pd

# %%
##

df = pd.DataFrame(np.random.randn(10, 5),
                  columns=list('abcde'))

# %%
##
df.query('(a < b)')

# %%
##
df.query('(a < b) & (b < c)')
df.query('(a < b) | (b < c)')

# %%
##
df = df.round(1)

# %%
##
df.query('c == [0.4, 0.3]')
df.query('c != 0.3')

df.query('[0.4, 0.8] in c')
