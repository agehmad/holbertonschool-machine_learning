#!/usr/bin/env python3
"""documented"""
import tensorflow.keras as K
import numpy as np


def one_hot(labels, classes=None):
    """documented"""
    if classes == None:
        classes = np.max(labels) + 1
    return np.eye(classes)[labels]
