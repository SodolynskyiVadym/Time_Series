import numpy as np


# Fits polynomial regression using Least Squares Method (LSM) by minimizing sum of squared residuals
def LSM(arr, max_degree: int = 2):
    iter = len(arr)
    Yin = np.zeros((iter, 1))
    F = np.ones((iter, max_degree + 1))

    for i in range(iter):
        Yin[i, 0] = float(arr[i])
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
    print('Regression model:')
    print('y(t) = ', ' + '.join(terms))

    return coeffs, Yout