#!/usr/bin/env python3
"""
Docstring for pipeline.pandas.2-from_file
"""
import pandas as pd


def array(df):
    """
    Docstring for array

    :param df: Description
    """
    df = df.iloc[:10]
    df = df.to_numpy()
    return df
