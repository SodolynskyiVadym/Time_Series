from lab1.generate_data import *
from lab1.parsing_data import *
from lab1.display_data import *
from lab4.decomposition import *
from lab4.fractal import *
from lab4.visualization import *
from lab4.generate_data import *
from lab1.calculate_statistic import *
from lab4.stationary_test import *
from lab4.clustering import *
from lab4.correlation import *



if __name__ == '__main__':

    arr_real1 = file_parsing("gdp.xlsx", "Gdp", "IT")
    arr_real2 = file_parsing("gdp.xlsx", "Gdp", "US")
    arr_real3 = file_parsing("gdp.xlsx", "Gdp", "FR")
    arr_real4 = file_parsing("bitcoin_price.xlsx", "Price")

    print("1 - Correlation analysis")
    print("2 - Fractal analysis")
    print("3 - Clustering analysis")
    print("4 - Decomposition analysis")
    print("5 - Stationary test")
    print("6 - Statistical characteristics")
    print("7 - Data_Set_8 analysis")

    mode = int(input("Select mode"))

    if mode == 1:
        display_three_graphs(arr_real1, arr_real2, arr_real3, "GDP IT", "GDP US", "GDP FR")

        print("Correlation matrix between GDP IT, GDP US and GDP FR:")
        print(correlation_np(arr_real1, arr_real2, arr_real3))

        print("Rolling correlation between GDP IT and GDP US:")
        rolling_corr(arr_real1, arr_real2)
    
    elif mode == 2:
        display_arr(arr_real4, "X", "Y", "Bitcoin Price Time Series")
        print("Hurst Index for Bitcoin price:")
        hurst_index(np.array(arr_real4))
    
    elif mode == 3:
        print("K-Means clustering for Bitcoin price:")
        k_means_clustering(arr_real4, 3)
    
    elif mode == 4:
        print("Decomposition analysis for Bitcoin price:")
        trend, seasonal, resid = decompose(arr_real4, seasonal=30, robust=True)
        display_three_graphs(trend, seasonal, resid, "Trend", "Seasonal", "Residuals of Bitcoin Price")
        display_arrays_comparison(range(len(trend)), trend, range(len(arr_real4)), arr_real4, "Extracted Trend", "Real Data", "Trend vs Real Data")

    elif mode == 5:
        print("ADF and KPSS tests for Bitcoin price:")
        adf_test(arr_real4)
        kpss_test(arr_real4)
    
    elif mode == 6:
        print("Statistical characteristics for Bitcoin price:")
        mean, disp, scv = calculate_statistics(arr_real4)
        print(f"Mean: {mean:.2f}, Dispersion: {disp:.2f}, Standard Deviation: {scv:.2f}")
    
    elif mode == 7:
        revenue_date = group_by_column("Data_Set_8.xlsx", "Order Date", "Revenue")
        
        print("Result grouping:")
        for date, total_revenue in sorted(revenue_date.items()):
            print(f"{date}: ${total_revenue:,.2f}")

        display_arr(list(revenue_date.values()), "Order Date", "Total Revenue", "Total Revenue by Order Date")

        data = list(revenue_date.values())
        adf_test(data)
        kpss_test(data)

        print("Characteristics of Total Revenue:")
        mean, disp, scv = calculate_statistics(data)
        print(f"Mean: {mean:.2f}, Dispersion: {disp:.2f}, Standard Deviation: {scv:.2f}")

        trend, seasonal, resid = decompose(data, seasonal=3, robust=True)
        display_three_graphs(trend, seasonal, resid, "Trend", "Seasonal", "Residuals of Total Revenue")

        display_arrays_comparison(range(len(trend)), trend, range(len(data)), data, "Extracted Trend", "Real Data", "Trend vs Real Data")


        fee_date = group_by_column("Data_Set_8.xlsx", "Order Date", "Shipping Fee")
        data_fee = list(fee_date.values())
        print("Результат групування:")
        for date, total_fee in sorted(fee_date.items()):
            print(f"{date}: ${total_fee:,.2f}")
        display_arr(data_fee, "Order Date", "Total Shipping Fee", "Total Shipping Fee by Order Date")

        display_arrays_comparison(range(len(data)), data, range(len(data_fee)), data_fee, "Total Revenue", "Total Shipping Fee", "Revenue vs Shipping Fee")

        correlation_np(data, data_fee)
        rolling_corr(data, data_fee)







    # FOR TESTING WITHOUT MODE SELECTION:

    # display_three_graphs(arr_real1, arr_real2, arr_real3, "GDP IT", "GDP US", "GDP FR")

    # print("Correlation matrix between GDP IT, GDP US and GDP FR:")
    # print(correlation_np(arr_real1, arr_real2, arr_real3))

    # print("Rolling correlation between GDP IT and GDP US:")
    # rolling_corr(arr_real1, arr_real2)


    # display_arr(arr_real4, "X", "Y", "Bitcoin Price Time Series")
    # print("Hurst Index for Bitcoin price:")
    # hurst_index(np.array(arr_real4))


    # print("K-Means clustering for Bitcoin price:")
    # k_means_clustering(arr_real4, 3)


    # print("Decomposition analysis for Bitcoin price:")
    # trend, seasonal, resid = decompose(arr_real4, seasonal=30, robust=True)
    # display_three_graphs(trend, seasonal, resid, "Trend", "Seasonal", "Residuals of Bitcoin Price")
    # display_arrays_comparison(range(len(trend)), trend, range(len(arr_real4)), arr_real4, "Extracted Trend", "Real Data", "Trend vs Real Data")


    # print("ADF and KPSS tests for Bitcoin price:")
    # adf_test(arr_real4)
    # kpss_test(arr_real4)


    # print("Statistical characteristics for Bitcoin price:")
    # mean, disp, scv = calculate_statistics(arr_real4)
    # print(f"Mean: {mean:.2f}, Dispersion: {disp:.2f}, Standard Deviation: {scv:.2f}")


    # revenue_date = group_by_column("Data_Set_8.xlsx", "Order Date", "Revenue")
    
    # print("Result grouping:")
    # for date, total_revenue in sorted(revenue_date.items()):
    #     print(f"{date}: ${total_revenue:,.2f}")

    # display_arr(list(revenue_date.values()), "Order Date", "Total Revenue", "Total Revenue by Order Date")

    # data = list(revenue_date.values())
    # adf_test(data)
    # kpss_test(data)

    # print("Characteristics of Total Revenue:")
    # mean, disp, scv = calculate_statistics(data)
    # print(f"Mean: {mean:.2f}, Dispersion: {disp:.2f}, Standard Deviation: {scv:.2f}")

    # trend, seasonal, resid = decompose(data, seasonal=3, robust=True)
    # display_three_graphs(trend, seasonal, resid, "Trend", "Seasonal", "Residuals of Total Revenue")

    # display_arrays_comparison(range(len(trend)), trend, range(len(data)), data, "Extracted Trend", "Real Data", "Trend vs Real Data")


    # fee_date = group_by_column("Data_Set_8.xlsx", "Order Date", "Shipping Fee")
    # data_fee = list(fee_date.values())
    # print("Результат групування:")
    # for date, total_fee in sorted(fee_date.items()):
    #     print(f"{date}: ${total_fee:,.2f}")
    # display_arr(data_fee, "Order Date", "Total Shipping Fee", "Total Shipping Fee by Order Date")

    # display_arrays_comparison(range(len(data)), data, range(len(data_fee)), data_fee, "Total Revenue", "Total Shipping Fee", "Revenue vs Shipping Fee")

    # correlation_np(data, data_fee)
    # rolling_corr(data, data_fee)