# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
# type: ignore
import numpy as np
import pandas as pd

np.random.seed(0)
print(pd.Series(np.random.randint(0, 7, size=10)).sum())

assert False

def test_fail():
    assert False