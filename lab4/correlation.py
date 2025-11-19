import pandas as pd
import math as mt
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def correlation_np(x, y, z=None):
    if z is None:
        correlation_matrix = np.corrcoef(x, y)
    else:
        correlation_matrix = np.corrcoef([x, y, z])

    plt.figure(figsize=(6, 5))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.show()

    return correlation_matrix




def rolling_corr(arr1, arr2):
    df = pd.DataFrame({'Data1': arr1, 'Data2': arr2}, index=range(len(arr1)))

    rolling_corr = df['Data1'].rolling(window=20).corr(df['Data2'])
    ts_corr = df['Data1'].corr(df['Data2'])
    ts_cov = df['Data1'].cov(df['Data2'])

    print('Correlation =', ts_corr)
    print('Covariance =', ts_cov)

    plt.figure(figsize=(14, 7))
    plt.plot(rolling_corr, label='Rolling Correlation', color='blue')
    plt.title('Rolling Correlation')
    plt.xlabel('X')
    plt.ylabel('Correlation')
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.legend()
    plt.show()