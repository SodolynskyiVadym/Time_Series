import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from hurst import compute_Hc

def hurst_index(data_np):
    series = pd.Series(data_np)

    H, c, data = compute_Hc(series, kind='price', simplified=True)

    print("H={:.4f}, c={:.4f}".format(H, c))

    f, ax = plt.subplots()
    ax.plot(data[0], c * data[0] ** H, color="deepskyblue")
    ax.scatter(data[0], data[1], color="purple")
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('Time interval')
    ax.set_ylabel('R/S ratio')
    ax.grid(True)
    plt.show()

    return