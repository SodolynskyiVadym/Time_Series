from statsmodels.tsa.arima.model import ARIMA
from lab1.calculate_statistic import *
import matplotlib.pyplot as plt
from lab2.model_determination import *



def ARIMA_model(data, train_coef, order=(1, 1, 15), text='ARIMA Model'):
    time_series = data
    train_size = int(len(time_series) * train_coef)
    train_data, test_data = time_series[:train_size], time_series[train_size:]


    model = ARIMA(train_data, order=order)

    model_fit = model.fit()
    forecast_steps = len(test_data)
    forecast = model_fit.forecast(steps=forecast_steps)

    print(f"{text} KPI")
    kpi_model(test_data.values.flatten(), forecast.values)
    print()

    plt.figure(figsize=(12, 6))
    plt.plot(train_data.index, train_data, label='Training Data', color='blue')
    plt.plot(test_data.index, test_data, label='Actual Test Data', color='green')
    plt.plot(forecast.index, forecast, label='ARIMA Forecast', color='red', linestyle='--')
    plt.title(text)
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()
    return  forecast



def ARIMA_model_extrapolation(data, extrapolation_coef, order=(1, 1, 15), text='ARIMA Model'):
    time_series = data

    model = ARIMA(time_series, order=order)

    model_fit = model.fit()
    forecast_steps = int(len(time_series) * extrapolation_coef)
    forecast = model_fit.forecast(steps=forecast_steps)

    plt.figure(figsize=(12, 6))
    plt.plot(time_series.index, time_series, label='Training Data', color='blue')
    plt.plot(forecast.index, forecast, label='ARIMA Forecast', color='red', linestyle='--')
    plt.title(text)
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()
    return  forecast