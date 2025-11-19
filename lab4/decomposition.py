from statsmodels.tsa.seasonal import STL

def decompose(array, seasonal = 13, robust=True):
    stl = STL(array, period=seasonal, robust=robust)
    result = stl.fit()
    return result.trend, result.seasonal, result.resid