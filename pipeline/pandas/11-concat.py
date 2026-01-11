#!/usr/bin/env python3
"""
Docstring for pipeline.pandas.11-concat
"""
import pandas as pd


def concat(df1, df2):
    """
    Concatenates two DataFrames with specific conditions. 

    : param df1: pd.DataFrame (coinbase)
    :param df2: pd.DataFrame (bitstamp)
    :return: concatenated pd.DataFrame
    """
    # Import the index function from 10-index.py
    index = __import__('10-index').index

    # Index both dataframes on their Timestamp columns
    df1 = index(df1)
    df2 = index(df2)

    # Filter df2: include all timestamps up to and including 1417411920
    df2 = df2[df2.index <= 1417411920]

    # Concatenate:  df2 on top of df1, with keys
    result = df1.__class__. concat(
        [df2, df1],
        keys=['bitstamp', 'coinbase']
    )

    return result
