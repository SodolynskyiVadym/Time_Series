import numpy as np
import math as mt


# Adds Gaussian noise and random anomalies to array based on specified rate and magnitude
def anomaly_creation(arr, dsig, anomaly_rate, anomaly_magnitude):
    errors = np.random.normal(0, dsig, len(arr))
    for i in range(len(errors)):
        if np.random.randint(0, 100) < anomaly_rate:
            errors[i] += errors[i] * anomaly_magnitude
    return arr + errors



# Detects and removes anomalies using sliding window median filtering
def sliding_wind_anomaly_detection(arr_real, window_size):
    iter = len(arr_real)
    j_Wind=mt.ceil(iter-window_size)+1
    arr_window=np.zeros((window_size))
    medium_arr = np.zeros(( iter))

    for j in range(j_Wind):
        for i in range(window_size):
            l=(j+i)
            arr_window[i] = arr_real[l]
        medium_arr[l] = np.median(arr_window)

    arr_cleared = np.zeros((iter))
    for j in range(iter):
        arr_cleared[j] = medium_arr[j]

    for j in range(window_size):
        arr_cleared[j] = arr_real[j]

    return arr_cleared