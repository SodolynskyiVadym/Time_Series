import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from parsing_data import file_parsing


def generate_norm_error(m, sigma, n):
    return np.random.normal(m, sigma, n)

def generate_exp_error(lambd, n):
    return np.random.exponential(1/lambd, n)


def calculate_statistics(values):
    mean = np.mean(values)
    disp = np.var(values)
    scv = np.sqrt(disp)

    return mean, disp, scv

def print_statistics(mean, disp, scv):
    print(f"Mean: {mean}")
    print(f"Dispersion: {disp}")
    print(f"SCV: {scv}")


def calculate_norm_dispersion(errors):
    mean = np.mean(errors)
    disp = 0
    for error in errors:
        disp += (error - mean) ** 2
    disp /= len(errors)
    return disp


def calculate_exp_dispersion(lambd):
    return 1 / (lambd ** 2)


def show_histogram_norm_error(m, sigma, errors):
    plt.hist(errors, bins=30, density=True, alpha=0.6, color='g')
    xmin, xmax = plt.xlim()

    x = np.linspace(xmin, xmax, 100)
    p = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - m) / sigma) ** 2)

    plt.plot(x, p, 'k', linewidth=2)
    title = f"Normal error histogram: m = {m},  sigma = {sigma}"
    plt.title(title)
    plt.show()


def show_histogram_exp_error(lambd, errors):
    plt.hist(errors, bins=30, density=True, alpha=0.6, color='g')
    xmin, xmax = plt.xlim()

    x = np.linspace(xmin, xmax, 100)
    p = lambd * np.exp(-lambd * x)

    plt.plot(x, p, 'k', linewidth=2)
    title = f"Exponential error histogram: lambda = {lambd}"
    plt.title(title)
    plt.show()


def generate_quadratic_trend(n, a=0.00007, b=0.0001, c=10):
    x = np.arange(n)
    return a * x**2 + b * x + c


def generate_linear_trend(n, a=0.05, b=10):
    x = np.arange(n)
    return a * x + b


def show_trend(x, y, ideal_trend, text):

    plt.figure()
    plt.plot(x, y, label=text, linewidth=2)
    plt.plot(x, ideal_trend, label="Ideal Trend", linestyle='--', linewidth=2)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title(text)
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    print('Select the source of input data and further actions:')
    print('1 - Model')
    print('2 - Real data')
    mode = int(input('Mode:'))
    if mode == 1:
        m = 0
        sigma = 3
        lambd = 0.5
        n = 1000

        print("Select the error distribution and the trend of the studied process:")
        print("1 - Normal error and linear trend")
        print("2 - Normal error and quadratic trend")
        print("3 - Exponential error and linear trend")
        print("4 - Exponential error and quadratic trend")
        mode_rule = int(input("Select mode:"))
        if mode_rule == 1:
            norm_errors = generate_norm_error(m, sigma, n)
            mean_err, disp_err, scv_err = calculate_statistics(norm_errors)
            print("----------------------- STATISTICS (Normal Errors) -----------------------")
            print_statistics(mean_err, disp_err, scv_err)
            print(f"Calculated dispersion: {calculate_norm_dispersion(norm_errors)}")
            show_histogram_norm_error(m, sigma, norm_errors)

            print("----------------------- STATISTICS (Linear Trend) -----------------------")
            linear_trend = generate_linear_trend(n)
            mean_lin, disp_lin, scv_lin = calculate_statistics(linear_trend)
            print_statistics(mean_lin, disp_lin, scv_lin)
            print()

            print("----------------------- STATISTICS (Linear Trend + Normal Errors) -----------------------")
            linear_trend_with_noise = linear_trend + norm_errors
            mean, disp, scv = calculate_statistics(linear_trend_with_noise)
            print_statistics(mean, disp, scv)
            print(f"VERIFICATION {mean_err} + {mean_lin} = {mean_err + mean_lin} = {mean}")
            show_trend(np.arange(n), linear_trend_with_noise, linear_trend, "Linear Trend")


        elif mode_rule == 2:
            norm_errors = generate_norm_error(m, sigma, n)
            print("----------------------- STATISTICS (Normal Errors) -----------------------")
            mean_err, disp_err, scv_err = calculate_statistics(norm_errors)
            print_statistics(mean_err, disp_err, scv_err)
            print(f"Calculated dispersion: {calculate_norm_dispersion(norm_errors)}")
            show_histogram_norm_error(m, sigma, norm_errors)
            print()

            print("----------------------- STATISTICS (Quadratic Trend) -----------------------")
            quadratic_trend = generate_quadratic_trend(n)
            mean_quad, disp_quad, scv_quad = calculate_statistics(quadratic_trend)
            print_statistics(mean_quad, disp_quad, scv_quad)
            print()

            print("----------------------- STATISTICS (Quadratic Trend + Normal Errors) -----------------------")
            quadratic_trend_with_noise = quadratic_trend + norm_errors
            mean, disp, scv = calculate_statistics(quadratic_trend_with_noise)
            print_statistics(mean, disp, scv)
            print(f"VERIFICATION {mean_err} + {mean_quad} = {mean_err + mean_quad} = {mean}")
            show_trend(np.arange(n), quadratic_trend_with_noise, quadratic_trend, "Quadratic Trend")


        elif mode_rule == 3:
            exp_errors = generate_exp_error(lambd, n)
            print("----------------------- STATISTICS (Exponential Errors) -----------------------")
            mean_err, disp_err, scv_err = calculate_statistics(exp_errors)
            print_statistics(mean_err, disp_err, scv_err)
            print(f"Calculated dispersion: {calculate_exp_dispersion(lambd)}")
            show_histogram_exp_error(lambd, exp_errors)
            print()

            print("----------------------- STATISTICS (Linear Trend) -----------------------")
            linear_trend = generate_linear_trend(n)
            mean_lin, disp_lin, scv_lin = calculate_statistics(linear_trend)
            print_statistics(mean_lin, disp_lin, scv_lin)
            print()

            print("----------------------- STATISTICS (Linear Trend + Exponential Errors) -----------------------")
            linear_trend_with_noise = linear_trend + exp_errors
            mean, disp, scv = calculate_statistics(linear_trend_with_noise)
            print_statistics(mean, disp, scv)
            print(f"VERIFICATION {mean_err} + {mean_lin} = {mean_err + mean_lin} = {mean}")
            show_trend(np.arange(n), linear_trend_with_noise, linear_trend, "Linear Trend")


        elif mode_rule == 4:
            exp_errors = generate_exp_error(lambd, n)
            print("----------------------- STATISTICS (Exponential Errors) -----------------------")
            mean_err, disp_err, scv_err = calculate_statistics(exp_errors)
            print_statistics(mean_err, disp_err, scv_err)
            print(f"Calculated dispersion: {calculate_exp_dispersion(lambd)}")
            show_histogram_exp_error(lambd, exp_errors)
            print()

            print("----------------------- STATISTICS (Quadratic Trend) -----------------------")
            quadratic_trend = generate_quadratic_trend(n)
            mean_quad, disp_quad, scv_quad = calculate_statistics(quadratic_trend)
            print_statistics(mean_quad, disp_quad, scv_quad)
            print()

            print("----------------------- STATISTICS (Quadratic Trend + Exponential Errors) -----------------------")
            quadratic_trend_with_noise = quadratic_trend + exp_errors
            mean, disp, scv = calculate_statistics(quadratic_trend_with_noise)
            print_statistics(mean, disp, scv)
            print(f"VERIFICATION {mean_err} + {mean_quad} = {mean_err + mean_quad} = {mean}")
            show_trend(np.arange(n), quadratic_trend_with_noise, quadratic_trend, "Quadratic Trend")


    elif mode == 2:
        print('Select the dataset:')
        print('1 - World Population Data')
        print('2 - USA Inflation Data')
        print('3 - GDP Data')
        data_mode = int(input('Dataset:'))

        if data_mode == 1:
            print("---------------- World Population Data -----------------------")
            data = file_parsing("world_population.xlsx", "Population")
            mean, disp, scv = calculate_statistics(data)
            print_statistics(mean, disp, scv)
            show_trend(np.arange(len(data)), data, data, "World Population Data")

        elif data_mode == 2:
            print("---------------- USA Inflation Data -----------------------")
            data = file_parsing("usa_inflation.xlsx", "Inflation")
            mean, disp, scv = calculate_statistics(data)
            print_statistics(mean, disp, scv)
            show_trend(np.arange(len(data)), data, data, "USA Inflation Data")

        elif data_mode == 3:
            country_code = input("Choose the country code for GDP data (e.g., 'FR' for France, 'US' for USA):")
            print(f"---------------- GDP Data {country_code} (Billion USD) -----------------------")
            data = file_parsing("gdp.xlsx", "Gdp", country_code)
            for i in range(len(data)):
                data[i] = data[i] / 1_000_000_000
            mean, disp, scv = calculate_statistics(data)
            print_statistics(mean, disp, scv)
            show_trend(np.arange(len(data)), data, data, f"GDP Data {country_code} (Billion USD)")

        mean, disp, scv = calculate_statistics(data)
        print(f"Mean: {mean}, Dispersion: {disp}, SCV: {scv}")


