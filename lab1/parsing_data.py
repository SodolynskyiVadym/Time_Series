import pandas as pd
import numpy as np
from lab1.site_parsing import fetch_gdp_data_to_excel

folder_path = "lab1"

def file_parsing(File_name, Data_name, country_code=""):
    if country_code != "":
        fetch_gdp_data_to_excel(country_code)

    d = pd.read_excel(f"{folder_path}/{File_name}")
    values = d[Data_name].values
    S_real = np.zeros((len(values)))
    for i in range(len(values)):
        S_real[i] = values[i]
    return S_real