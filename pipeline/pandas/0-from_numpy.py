#!/usr/bin/env python3
import pandas as pd
import string

def from_numpy(array):
    num_columns = array.shape[1]
    columns = list(string.ascii_uppercase[:num_columns])
    df = pd.DataFrame(array, columns=columns)
    return df
