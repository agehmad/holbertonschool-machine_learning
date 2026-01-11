#!/usr/bin/env python3
"""
Docstring for pipeline.5-slice
"""


def slice(df):
    df = df[['High', 'Low', 'Close', 'Volume_BTC']]
    df = df.iloc[::60]
    return df
