import numpy as np
import math as mt


# Determines optimal polynomial degree by comparing experimental and theoretical standard deviations of high-order derivatives
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


    scv_y = np.zeros((degree - 1))
    var_SL = np.var(SL)
    scv_y_theor = np.zeros((degree - 1))
    dalta_array = np.zeros((degree - 1))

    for d in range(degree - 1):
        scv_y[d] = mt.sqrt(np.var(y[d]))
        scv_y_theor[d] = mt.sqrt((2 * var_SL) / (dt ** (2 * (d + 1))))
        dalta_array[d] = abs(scv_y[d] - scv_y_theor[d])

    m_polinom = np.argmin(dalta_array) + 1

    print("Polynomial-derivative scoring summary")
    print(f"Optimal polynomial degree (based on SCV difference): {m_polinom}")

    return m_polinom, dalta_array