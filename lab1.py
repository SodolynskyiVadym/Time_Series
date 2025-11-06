import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from parsing_data import file_parsing

# Simple utilities to generate random errors and trends and to display basic statistics/plots.
# The script can run in two modes: simulated model data (with controllable error/trend)
# or real data loaded from Excel files via file_parsing().

def generate_norm_error(m, sigma, n):
    # Generate n samples from a normal distribution with mean m and stddev sigma.
    return np.random.normal(m, sigma, n)

def generate_exp_error(lambd, n):
    # Generate n samples from an exponential distribution with rate lambda.
    # numpy.exponential expects scale = 1/lambda.
    return np.random.exponential(1/lambd, n)


def calculate_statistics(values):
    # Compute basic statistics for a 1-D array-like: mean, variance, and standard deviation (SCV here).
    mean = np.mean(values)
    disp = np.var(values)
    scv = np.sqrt(disp)

    return mean, disp, scv

def print_statistics(mean, disp, scv):
    # Nicely print the three statistics to console.
    print(f"Mean: {mean}")
    print(f"Dispersion: {disp}")
    print(f"SCV: {scv}")


def calculate_norm_dispersion(errors):
    # Manual calculation of variance (dispersion) for a list/array of errors.
    # This duplicates np.var but shows the explicit formula.
    mean = np.mean(errors)
    disp = 0
    for error in errors:
        disp += (error - mean) ** 2
    disp /= len(errors)
    return disp


def calculate_exp_dispersion(lambd):
    # Theoretical variance for an exponential distribution with rate lambda.
    return 1 / (lambd ** 2)


def show_histogram_norm_error(m, sigma, errors):
    # Plot a normalized histogram of the errors and overlay the theoretical normal PDF.
    plt.hist(errors, bins=30, density=True, alpha=0.6, color='g')
    xmin, xmax = plt.xlim()

    x = np.linspace(xmin, xmax, 100)
    p = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - m) / sigma) ** 2)

    plt.plot(x, p, 'k', linewidth=2)
    title = f"Normal error histogram: m = {m},  sigma = {sigma}"
    plt.title(title)
    plt.show()


def show_histogram_exp_error(lambd, errors):
    # Plot a normalized histogram of exponential errors and overlay the theoretical exponential PDF.
    plt.hist(errors, bins=30, density=True, alpha=0.6, color='g')
    xmin, xmax = plt.xlim()

    x = np.linspace(xmin, xmax, 100)
    p = lambd * np.exp(-lambd * x)

    plt.plot(x, p, 'k', linewidth=2)
    title = f"Exponential error histogram: lambda = {lambd}"
    plt.title(title)
    plt.show()


def generate_quadratic_trend(n, a=0.00007, b=0.0001, c=10):
    # Return a quadratic trend sequence of length n using coefficients a, b, c.
    x = np.arange(n)
    return a * x**2 + b * x + c


def generate_linear_trend(n, a=0.05, b=10):
    # Return a linear trend sequence of length n with slope a and intercept b.
    x = np.arange(n)
    return a * x + b


def show_trend(x, y, ideal_trend, text):
    # Plot the observed series y and the ideal trend on the same axes.
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
    # Interactive CLI to choose between simulated model data and real datasets
    print('Select the source of input data and further actions:')
    print('1 - Model')
    print('2 - Real data')
    mode = int(input('Mode:'))
    if mode == 1:
        # Default parameters for simulation
        m = 0
        sigma = 2.5
        lambd = 0.5
        n = 1000

        # Choose the combination of error distribution and trend
        print("Select the error distribution and the trend of the studied process:")
        print("1 - Normal error and linear trend")
        print("2 - Normal error and quadratic trend")
        print("3 - Exponential error and linear trend")
        print("4 - Exponential error and quadratic trend")
        mode_rule = int(input("Select mode:"))
        if mode_rule == 1:
            # Normal errors + linear trend
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
            # Add errors to the trend and show combined statistics and plot
            linear_trend_with_noise = linear_trend + norm_errors
            mean, disp, scv = calculate_statistics(linear_trend_with_noise)
            print_statistics(mean, disp, scv)
            print(f"VERIFICATION {mean_err} + {mean_lin} = {mean_err + mean_lin} = {mean}")
            show_trend(np.arange(n), linear_trend_with_noise, linear_trend, "Linear Trend + Normal Errors")


        elif mode_rule == 2:
            # Normal errors + quadratic trend
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
            show_trend(np.arange(n), quadratic_trend_with_noise, quadratic_trend, "Quadratic Trend + Normal Errors")


        elif mode_rule == 3:
            # Exponential errors + linear trend
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
            show_trend(np.arange(n), linear_trend_with_noise, linear_trend, "Linear Trend + Exponential Errors")


        elif mode_rule == 4:
            # Exponential errors + quadratic trend
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
            show_trend(np.arange(n), quadratic_trend_with_noise, quadratic_trend, "Quadratic Trend + Exponential Errors")


    elif mode == 2:
        # Real data mode: choose among several datasets parsed from Excel
        print('Select the dataset:')
        print('1 - World Population Data')
        print('2 - USA Inflation Data')
        print('3 - GDP Data')
        data_mode = int(input('Dataset:'))

        if data_mode == 1:
            # Load population column from a spreadsheet and display stats/plot
            print("---------------- World Population Data -----------------------")
            data = file_parsing("world_population.xlsx", "Population")
            mean, disp, scv = calculate_statistics(data)
            print_statistics(mean, disp, scv)
            show_trend(np.arange(len(data)), data, data, "World Population Data")

        elif data_mode == 2:
            # Load inflation column and display
            print("---------------- USA Inflation Data -----------------------")
            data = file_parsing("usa_inflation.xlsx", "Inflation")
            mean, disp, scv = calculate_statistics(data)
            print_statistics(mean, disp, scv)
            show_trend(np.arange(len(data)), data, data, "USA Inflation Data")

        elif data_mode == 3:
            # Load GDP data for a specific country code, convert units to billions for readability
            country_code = input("Choose the country code for GDP data (e.g., 'FR' for France, 'US' for USA):")
            print(f"---------------- GDP Data {country_code} (Billion USD) -----------------------")
            data = file_parsing("gdp.xlsx", "Gdp", country_code)
            for i in range(len(data)):
                data[i] = data[i] / 1_000_000_000
            mean, disp, scv = calculate_statistics(data)
            print_statistics(mean, disp, scv)
            show_trend(np.arange(len(data)), data, data, f"GDP Data {country_code} (Billion USD)")

        # Final printout of statistics (redundant if already printed above, but kept for consistency)
        mean, disp, scv = calculate_statistics(data)
        print(f"Mean: {mean}, Dispersion: {disp}, SCV: {scv}")
