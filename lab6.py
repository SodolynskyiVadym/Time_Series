from lab1.parsing_data import *
import pandas as pd
from lab1.generate_data import *
from lab1.display_data import *
from lab1.calculate_statistic import *
from lab2.model_determination import *
from lab4.stationary_test import *
from lab4.decomposition import *
from lab4.visualization import *
from lab6.exponential_smoothing import *



if __name__ == "__main__":
    # data = file_parsing("data/bitcoin_price.xlsx", "Price")
    data = file_parsing("data/gdp.xlsx", "Gdp", "IT")
    # data = file_parsing("data/usa_inflation.xlsx", "Inflation")
    # data = generate_quadratic_trend(100)
    
    display_arr(data, "Index", "Value", "Original Data")
    mean, disp, scv = calculate_statistics(data)
    display_statistics(mean, disp, scv)
    print("\n Stationarity Tests:")
    adf_test(data)
    kpss_test(data)
    trend, seasonal, residual = decompose(data)
    display_three_graphs(trend, seasonal, residual, "Trend", "Seasonal", "Residuals")

    data = pd.DataFrame(data)


    model_single_fit, forecast_single = exponential_smoothing(data)
    model_double_fit, forecast_double = double_exponential_smoothing(data)
    model_holt_winter_fit, forecast_holt_winter = holt_winter_seasonal_smoothing(data)

    display_three_arrays(data, model_single_fit.fittedvalues, forecast_single, "Data", "Single Exp Smoothing Fitted", "Single Exp Smoothing Forecast", "Single Exponential Smoothing Results")
    display_three_arrays(data, model_double_fit.fittedvalues, forecast_double, "Data", "Double Exp Smoothing Fitted", "Double Exp Smoothing Forecast", "Double Exponential Smoothing Results")
    display_three_arrays(data, model_holt_winter_fit.fittedvalues, forecast_holt_winter, "Data", "Holt-Winter Fitted", "Holt-Winter Forecast", "Holt-Winter Seasonal Smoothing Results")

    print("\n KPI Simple Exponential Smoothing")
    kpi_model(data, model_single_fit.fittedvalues)

    print("\n KPI Double Exponential Smoothing")
    kpi_model(data, model_double_fit.fittedvalues)

    print("\n KPI Holt-Winter Seasonal Smoothing")
    kpi_model(data, model_holt_winter_fit.fittedvalues)