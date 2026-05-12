#!/usr/bin/env python3
"""documented"""
import tensorflow.keras as K


def save_model(network, filename):
    """documented"""
    network.save(filename)
    return None


def load_model(filename):
    """documented"""
    return K.models.load_model(filename)
