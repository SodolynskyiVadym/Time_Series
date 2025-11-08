import numpy as np


def calculate_statistics(values):
    # Compute basic statistics for a 1-D array-like: mean, variance, and standard deviation (SCV here).
    mean = np.mean(values)
    disp = np.var(values)
    scv = np.sqrt(disp)

    return mean, disp, scv


def calculate_norm_dispersion(errors):
    # Manual calculation of variance (dispersion) for a list/array of errors.
    # This duplicates np.var but shows the explicit formula.
    mean = np.mean(errors)
    disp = 0
    for error in errors:
        disp += (error - mean) ** 2
    disp /= len(errors)
    return disp


def calculate_exp_dispersion(lambd):
    # Theoretical variance for an exponential distribution with rate lambda.
    return 1 / (lambd ** 2)