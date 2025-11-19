import numpy as np
import matplotlib.pyplot as plt



def display_statistics(mean, disp, scv):
    print(f"Mean: {mean}")
    print(f"Dispersion: {disp}")
    print(f"SCV: {scv}")


def display_histogram_norm_error(m, sigma, errors):
    plt.hist(errors, bins=30, density=True, alpha=0.6, color='g')
    xmin, xmax = plt.xlim()

    x = np.linspace(xmin, xmax, 100)
    p = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - m) / sigma) ** 2)

    plt.plot(x, p, 'k', linewidth=2)
    title = f"Normal error histogram: m = {m},  sigma = {sigma}"
    plt.title(title)
    plt.show()



def display_histogram_exp_error(lambd, errors):
    plt.hist(errors, bins=30, density=True, alpha=0.6, color='g')
    xmin, xmax = plt.xlim()

    x = np.linspace(xmin, xmax, 100)
    p = lambd * np.exp(-lambd * x)

    plt.plot(x, p, 'k', linewidth=2)
    title = f"Exponential error histogram: lambda = {lambd}"
    plt.title(title)
    plt.show()



def display_trend(x, y, arr_real, text):
    plt.figure()
    plt.plot(x, y, label=text, linewidth=2)
    plt.plot(x, arr_real, label="Real Data", linestyle='--', linewidth=2)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title(text)
    plt.legend()
    plt.grid(True)
    plt.show()


def display_arr(y, text_x, text_y, title):
    plt.figure()
    plt.plot(range(len(y)), y, label=title, linewidth=2)
    plt.xlabel(text_x)
    plt.ylabel(text_y)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


def display_arrays_comparison(x1, y1, x2, y2, label1, label2, title, y_real = None):
    plt.figure()
    plt.plot(x1, y1, label=label1, linewidth=2)
    plt.plot(x2, y2, label=label2, linewidth=2)
    if y_real is not None:
        plt.plot(x1, y_real, label="Real Trend", linestyle='--', linewidth=2)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()