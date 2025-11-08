from lab1.generate_data import generate_polynomial_trend
from lab2.statistical_learning import LSM
from lab2.polynomial_degree import *
from sklearn.metrics import *


# Calculates model evaluation metrics: MAE, MSE, RMSE, and R² score
def kpi_model(y_test, predicted):
    mae = mean_absolute_error(y_test, predicted)
    mse = mean_squared_error(y_test, predicted)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, predicted)

    print("Model evaluation metrics:")
    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"Mean Squared Error (MSE): {mse}")
    print(f"Root Mean Squared Error (RMSE): {rmse}")
    print(f"R-squared (R2) Score: {r2}")

    return


# Computes R² (coefficient of determination) manually from scratch for time series data
def r2_score_ts_stat_lern(SL, Yout, Text):
    iter = len(Yout)
    numerator = 0
    denominator_1 = 0

    for i in range(iter):
        numerator = numerator + (SL[i] - Yout[i, 0]) ** 2
        denominator_1 = denominator_1 + SL[i]

    denominator_2 = 0

    for i in range(iter):
        denominator_2 = denominator_2 + (SL[i] - (denominator_1 / iter)) ** 2

    R2_score_our = 1 - (numerator / denominator_2)
    print('------------', Text, '-------------')
    print('Number of elements in sample =', iter)
    print('Coefficient of determination (approximation probability) =', R2_score_our)

    return R2_score_our



# Extrapolates time series by fitting polynomial to training portion and extending beyond original data length
def extrapolation(arr_real, study_coef, extrapolation_coef):
    n = len(arr_real)
    if study_coef > 1:
        study_coef = 1
    if extrapolation_coef < 1:
        extrapolation_coef = 1

    study_arr = arr_real[:int(len(arr_real) * study_coef)]

    polynom_degree, _ = degree_polynomial_derivatives_scor(study_arr, 10, 1)

    coeffs, _ = LSM(study_arr, polynom_degree)
    return generate_polynomial_trend(int(n * extrapolation_coef), coeffs)