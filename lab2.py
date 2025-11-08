import numpy as np
import math as mt
from lab1.parsing_data import *
from lab1.display_data import *
from lab1.generate_data import *


def degree_polynomial_derivatives_scor(SL: np.ndarray, degree, dt: float):
    degree += 1
    iter = len(SL)
    y = np.zeros((degree, iter, 1))

    pascal = np.zeros((degree, degree), dtype=int)
    for n in range(degree):
        for k in range(n + 1):
            if k == 0 or k == n:
                pascal[n, k] = 1
            else:
                pascal[n, k] = pascal[n - 1, k - 1] + pascal[n - 1, k]

    for i in range(iter):
        for d in range(1, degree):
            if i < (iter - d):
                coeffs = pascal[d, :d + 1]
                terms = [SL[i + j] * coeffs[j] * ((-1) ** (d - j)) for j in range(d + 1)]
                y[d - 1][i] = sum(terms) / (dt ** d)


    mean_array = np.zeros((degree - 1))

    for d in range(degree - 1):
        mean_array[d] = abs(np.mean(y[d]))
    m_polinom_mean = np.argmin(mean_array) + 1


    scv_y = np.zeros((degree - 1))
    for d in range(degree - 1):
        scv_y[d] = mt.sqrt(np.var(y[d]))


    var_SL = np.var(SL)
    scv_y_theor = np.zeros((degree - 1))
    for d in range(degree - 1):
        scv_y_theor[d] = mt.sqrt((2 * var_SL) / (dt ** (2 * (d + 1))))
    

    dalta_array = np.zeros((degree - 1))
    for d in range(degree - 1):
        dalta_array[d] = abs(scv_y[d] - scv_y_theor[d])
    m_polinom = np.argmin(dalta_array) + 1

    # Nicely formatted summary
    mean_str = np.array2string(mean_array, precision=6, separator=', ')
    print("\nPolynomial-derivative scoring summary")
    print("=" * 60)
    print(f"Mean absolute values by derivative order (d = 1..{len(mean_array)}):")
    print(f"  {mean_str}")
    print(f"Minimum mean at derivative order: d = {m_polinom_mean}")
    print()
    print("SCV (sqrt(var)) comparison by derivative order:")
    print("  d   observed         theoretical        |difference|")
    for d, (obs, theo, diff) in enumerate(zip(scv_y, scv_y_theor, dalta_array), start=1):
        print(f"  {d:2d}  {obs:15.6e}  {theo:15.6e}  {abs(diff):15.6e}")
    print()
    print(f"Optimal polynomial degree (based on SCV difference): {m_polinom}")
    print("=" * 60)

    return m_polinom, dalta_array


def LSM(S0, max_degree: int = 2):
    iter = len(S0)
    Yin = np.zeros((iter, 1))
    F = np.ones((iter, max_degree + 1))

    for i in range(iter):
        Yin[i, 0] = float(S0[i])
        for k in range(1, max_degree + 1):
            F[i, k] = float(i ** k)

    FT = F.T
    FFT = FT.dot(F)
    FFTI = np.linalg.inv(FFT)
    FFTIFT = FFTI.dot(FT)
    C = FFTIFT.dot(Yin)
    Yout = F.dot(C)

    coeffs = [float(C[j, 0]) for j in range(C.shape[0])][::-1]
    terms = []
    for j, coeff in enumerate(coeffs):
        if j == 0:
            terms.append(f"{coeff}")
        else:
            terms.append(f"{coeff} * t^{j}")
    print('Регресійна модель:')
    print('y(t) = ', ' + '.join(terms))
    print(coeffs)

    return coeffs, Yout





if __name__ == "__main__":
    arr_real = file_parsing("gdp.xlsx", "Gdp")

    polynom_degree, dalta_array = degree_polynomial_derivatives_scor(arr_real, 10, 1)
    display_arr(np.arange(1, len(dalta_array) + 1), dalta_array, "Degree", "Value", "Polynomial Derivatives")

    coeffs, Yout = LSM(arr_real, polynom_degree)

    arr_polynom = generate_polynomial_trend(len(arr_real), coeffs)
    display_trend(np.arange(len(arr_polynom)), arr_polynom, arr_real, f"Generated Polynomial Trend of {polynom_degree}th degree")
