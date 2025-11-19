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


def group_by_column(file_path, group_column, sum_column):
    """
    Читає Excel файл та групує дані за вказаною колонкою, сумуючи значення іншої колонки.
    
    Параметри:
    file_path (str): Шлях до Excel файлу
    group_column (str): Назва колонки для групування (наприклад, 'Order Date')
    sum_column (str): Назва колонки для сумування (наприклад, 'Revenue')
    
    Повертає:
    dict: Словник {ключ_групування: сума_значень}
    """
    try:
        # Читання Excel файлу
        df = pd.read_excel(f"{folder_path}/{file_path}")
        
        # Перевірка наявності колонок
        if group_column not in df.columns:
            raise ValueError(f"Колонка '{group_column}' не знайдена в файлі")
        if sum_column not in df.columns:
            raise ValueError(f"Колонка '{sum_column}' не знайдена в файлі")
        
        # Групування та сумування
        result = df.groupby(group_column)[sum_column].sum().to_dict()
        
        return result
    
    except FileNotFoundError:
        print(f"Помилка: Файл '{file_path}' не знайдено")
        return {}
    except Exception as e:
        print(f"Помилка: {str(e)}")
        return {}