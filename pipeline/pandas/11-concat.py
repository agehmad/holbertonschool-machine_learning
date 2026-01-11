#!/usr/bin/env python3
"""
Docstring for pipeline.pandas.11-concat
"""
index = __import__('10-index').index


def concat(df1, df2):
    """
    Docstring for concat

    :param df1: Description
    :param df2: Description
    """
    df1 = index(df1)
    df2 = index(df2)

    df2 = df2.loc[: 1417411920]

    result = df1.__class__. concat(
        [df2, df1],
        keys=['bitstamp', 'coinbase']
    )

    return result
