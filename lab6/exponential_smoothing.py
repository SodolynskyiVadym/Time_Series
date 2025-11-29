from statsmodels.tsa.api import *


def exponential_smoothing(data):
    model = SimpleExpSmoothing(data)
    model_single_fit = model.fit()
    forecast_single = model_single_fit.forecast(len(data))

    return model_single_fit, forecast_single


def double_exponential_smoothing(data):
    model = Holt(data)
    model_single_fit = model.fit()
    forecast_single = model_single_fit.forecast(len(data))

    return model_single_fit, forecast_single



def holt_winter_seasonal_smoothing(data, seasonal_periods=12):
    model = ExponentialSmoothing(
        data,
        seasonal_periods=seasonal_periods,
        trend='add',
        seasonal='add')
    
    model_single_fit = model.fit()
    forecast_single = model_single_fit.forecast(len(data))

    return model_single_fit, forecast_single