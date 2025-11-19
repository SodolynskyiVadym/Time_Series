import numpy as np


def generate_norm_error(n, m, sigma):
    # Generate n samples from a normal distribution with mean m and stddev sigma.
    return np.random.normal(m, sigma, n)


def generate_exp_error(lambd, n):
    # Generate n samples from an exponential distribution with rate lambda.
    # numpy.exponential expects scale = 1/lambda.
    return np.random.exponential(1/lambd, n)


def generate_quadratic_trend(n, a=0.00007, b=0.0001, c=10):
    # Return a quadratic trend sequence of length n using coefficients a, b, c.
    x = np.arange(n)
    return a * x**2 + b * x + c


def generate_polynomial_trend(n, arr):
    x = np.zeros(n, dtype=float)

    for k in range(n):
        for i, coeff in enumerate(arr[::-1]):
            x[k] += coeff * (k ** i)

    return x


def generate_linear_trend(n, a=0.05, b=10):
    # Return a linear trend sequence of length n with slope a and intercept b.
    x = np.arange(n)
    return a * x + b