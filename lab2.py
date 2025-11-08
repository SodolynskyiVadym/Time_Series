import numpy as np
from lab1.parsing_data import *
from lab1.display_data import *
from lab1.generate_data import *
from lab2.statistical_learning import *
from lab2.model_determination import *
from lab2.polynomial_degree import *
from lab2.anomaly import *




if __name__ == "__main__":
    print("World Population Data Analysis")
    arr_real = file_parsing("gdp.xlsx", "Gdp", "US")

    polynom_degree, dalta_array = degree_polynomial_derivatives_scor(arr_real, 10, 1)
    coeffs, Yout = LSM(arr_real, polynom_degree)
    extrapolated_arr = extrapolation(arr_real, 1, 1.5)

    r2_score_ts_stat_lern(arr_real, Yout, "LSM Polynomial Trend Fitting for GDP Data")
    kpi_model(arr_real, Yout)

    display_arr(range(1, len(dalta_array) + 1), dalta_array, "Degree", "Delta SCV", "Delta SCV vs Polynomial Degree for GDP Data")
    display_trend(np.arange(len(arr_real)), arr_real, generate_polynomial_trend(len(arr_real), coeffs), "GDP Data with Polynomial Trend")
    display_arrays_comparison(np.arange(len(extrapolated_arr)), extrapolated_arr, np.arange(len(arr_real)), arr_real, "Extrapolated Data", "Real Data", "Comparison of Extrapolated and Real World Population Data")
    print("---------------------------------------------------")
    print()


    print("Anomaly Detection on Synthetic Data")
    n = 1000
    anomaly_rate = 10
    anomaly_magnitude = 3
    dsig = 3

    arr_real = generate_quadratic_trend(n)
    arr_noised = anomaly_creation(arr_real, dsig, anomaly_rate, anomaly_magnitude)
    arr_clear = sliding_wind_anomaly_detection(arr_noised, 5)

    display_arrays_comparison(np.arange(n), arr_noised, np.arange(n), arr_clear, "Noised Data", "Cleared Data", "Anomaly Detection using Sliding Window for Synthetic Data", arr_real)
    display_trend(np.arange(n), arr_clear, arr_real, "Noised Data with Cleared Trend")
    print("---------------------------------------------------")
    print()

    print("USA Inflation Data Analysis")
    arr_real = file_parsing("usa_inflation.xlsx", "Inflation")
    arr_clear = sliding_wind_anomaly_detection(arr_real, 5)
    polynom_degree, dalta_array = degree_polynomial_derivatives_scor(arr_clear, 9, 1)
    coeffs, Yout = LSM(arr_clear, polynom_degree)
    r2_score_ts_stat_lern(arr_clear, Yout, "LSM Polynomial Trend Fitting")
    kpi_model(arr_clear, Yout)
    display_arr(range(1, len(dalta_array) + 1), dalta_array, "Degree", "Delta SCV", "Delta SCV vs Polynomial Degree for USA Inflation Data")
    display_arrays_comparison(np.arange(len(arr_real)), arr_real, np.arange(len(arr_clear)), arr_clear, "Real Data", "Cleared Data", "USA Inflation Data: Real vs Cleared", Yout.flatten())
