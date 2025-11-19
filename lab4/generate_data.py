import numpy as np


def generate_seasonality_sin(length, amplitude, period):
    arr = np.zeros(length)
    for i in range(length):
        arr[i] = amplitude * np.sin(2 * np.pi * i / period)
    return arr
