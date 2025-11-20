from lab1.parsing_data import *
import pandas as pd
from lab4.generate_data import *
from lab1.generate_data import *
from lab1.display_data import *
from lab4.stationary_test import *
from lab2.model_determination import *
from lab5.arima_aproximation import *



if __name__ == "__main__":
    # data = file_parsing("bitcoin_price.xlsx", "Price")
    data = file_parsing("gdp.xlsx", "Gdp", "IT")
    # data = file_parsing("Oschadbank (USD).xls", "Купівля")
    # data = generate_seasonality_sin(150, 5, 25)


    display_arr(data, "X", "Y" , "Generated Data")
    
    print("----Stationary Test----")
    adf_test(data)
    kpss_test(data)
    print()
    
    print("----Characteristics of Data-----")
    calculate_statistics(data) 
    print() 
    
    data = pd.DataFrame(data)

    # Trained ARIMA Model 80% train data
    ARIMA_model(data, 0.8, order=(1, 1, 10), text="ARIMA Parameters (1, 1, 10) Train data 80%")
    ARIMA_model(data, 0.8, order=(1, 0, 10), text="ARMA Parameters (1, 0, 10) Train data 80%")
    ARIMA_model(data, 0.8, order=(1, 0, 0), text="AR Parameters (1, 0, 0) Train data 80%")
    ARIMA_model(data, 0.8, order=(0, 0, 10), text="MA Parameters (0, 0, 10) Train data 80%")


    # Extrapolation
    ARIMA_model_extrapolation(data, 1.5, order=(1, 1, 10), text="ARIMA Parameters (1, 1, 10) Extrapolation 0.5")
    ARIMA_model_extrapolation(data, 2, order=(1, 1, 10), text="ARIMA Parameters (1, 1, 10) Extrapolation 1")
    ARIMA_model_extrapolation(data, 2.5, order=(1, 1, 10), text="ARIMA Parameters (1, 1, 10) Extrapolation 1.5")
    ARIMA_model_extrapolation(data, 35, order=(1, 1, 10), text="ARIMA Parameters (1, 1, 10) Extrapolation 2")




   