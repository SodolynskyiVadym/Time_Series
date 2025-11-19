from lab2.model_determination import kpi_model
from lab2.anomaly import sliding_wind_anomaly_detection
from lab1.parsing_data import *
from lab1.display_data import *
from lab1.generate_data import *
from sklearn.metrics import *
from lab3.kalman_filters import *




if __name__ == "__main__":
    n = 1000
    print("Quadratic synthetic data - 1")
    print("GDP data - 2")
    print("USA Inflation data - 3")
    print("World Population data - 4")
    mode = int(input("Select data for Kalman filter"))
    if mode == 1:
        arr_real = generate_quadratic_trend(n)
        arr_noise = generate_norm_error(n, 0, 2.5)
        arr_real = arr_real + arr_noise
    elif mode == 2:
        arr_real = file_parsing("gdp.xlsx", "Gdp", "BR")
    elif mode == 3:
        arr_real = file_parsing("usa_inflation.xlsx", "Inflation")
    elif mode == 4:
        arr_real = file_parsing("world_population.xlsx", "Population")
    
    arr_real = sliding_wind_anomaly_detection(arr_real, 5)

    arr_abgf = ABGF(arr_real)
    arr_abfg_modified = ABGF_modified(arr_real)

    print("Evaluation of ABFG Filter:")
    kpi_model(arr_real, arr_abgf)
    print()

    print("Evaluation of Modified ABFG Filter:")
    kpi_model(arr_real, arr_abfg_modified)

    display_arrays_comparison(np.arange(len(arr_abfg_modified)), arr_abfg_modified, np.arange(len(arr_abgf)), arr_abgf.flatten(), "ABFG Modified", "ADFG", "Comparison of Real and ABGF Filters", arr_real)