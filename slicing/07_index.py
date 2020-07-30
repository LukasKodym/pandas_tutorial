# -*- coding: utf-8 -*-
# %%
##

import numpy as np
import pandas as pd

# %%
##

idx = pd.Index(['8637', '0643', '0953', '3246'])

df = pd.DataFrame(np.random.randn(4, 5),
                  index=idx,
                  columns=list('abcde'))
