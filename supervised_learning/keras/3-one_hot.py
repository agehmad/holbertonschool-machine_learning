#!/usr/bin/env python3
"""documented"""
import tensorflow.keras as K


def one_hot(labels, classes=None):
    """documented"""
    if classes is None:
        classes = max(labels) + 1
    return K.utils.to_categorical(labels, num_classes=classes)
