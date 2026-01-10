#!/usr/bin/env python3
import pandas as pd

def from_numpy(array):
    ndf = pd.DataFrame(array)
    ndf.sort_index(axis=1)
    ndf.columns = ndf.columns.str.upper()
    print(ndf)
