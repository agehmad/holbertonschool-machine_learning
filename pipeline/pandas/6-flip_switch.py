#!/usr/bin/env python3
"""
Docstring for pipeline.pandas.6-flip_switch
"""
import pandas as pd


def flip_switch(df):
    df = df.sort_values(ascendin=False)
    df - df.transpose()
    return df
