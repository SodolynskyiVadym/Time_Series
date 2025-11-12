import numpy as np
from lab1.parsing_data import *
from lab1.display_data import *
from lab1.generate_data import *
from sklearn.metrics import *


def ABF(S0):
    iter = len(S0)
    Yin = np.zeros((iter, 1))
    YoutAB = np.zeros((iter, 1))
    T0 = 1

    for i in range(iter):
        Yin[i, 0] = float(S0[i])

    Yspeed_retro = (Yin[1, 0] - Yin[0, 0]) / T0
    Yextra = Yin[0, 0] + Yspeed_retro
    alfa = 2 * (2 * 1 - 1) / (1 * (1 + 1))
    beta = (6 / 1) * (1 + 1)
    YoutAB[0, 0] = Yin[0, 0] + alfa * (Yin[0, 0])

    for i in range(1, iter):
        YoutAB[i, 0] = Yextra + alfa * (Yin[i, 0] - Yextra)
        Yspeed = Yspeed_retro + (beta/T0) * (Yin[i, 0] - Yextra)
        Yspeed_retro = Yspeed
        Yextra = YoutAB[i,0] + Yspeed_retro
        alfa = (2 * (2 * i - 1)) / (i * (i + 1))
        beta = 6 / (i * (i + 1))

    return YoutAB

def ABGF_modified(S0):
    iter = len(S0)
    Yin = np.zeros(iter)
    Yout_ABG = np.zeros(iter)
    T0 = 1
    for i in range(iter):
        Yin[i] = float(S0[i])

    Yspeed_retro = (Yin[1] - Yin[0]) / T0
    Yaccel_retro = (Yin[2] - 2 * Yin[1] + Yin[0]) / (T0 * T0)
    Yextra = Yin[0] + (Yspeed_retro * T0) + (Yaccel_retro * 0.5 * T0 * T0)

    alpha = 3 * (3 * 1 * 1 - 3 * 1 + 2) / (1 * (1 + 1) * (1 + 2))
    beta = 18 * (2 * 1 - 1) / (T0 * (1 + 1) * (1 + 2) * 1)
    gamma = 60 / (T0 * T0 * (1 + 1) * (1 + 2) * 1)
    Yout_ABG[0] = Yin[0]

    r2_previous = 1
    r2 = 1
    counter = 1
    coef = 1
    for i in range(1, iter):
        Yout_ABG[i] = Yextra + alpha * (Yin[i] - Yextra)
        Yspeed = Yspeed_retro + (beta / T0) * (Yin[i] - Yextra)
        Yaccel = Yaccel_retro + (gamma / T0 * T0) * (Yin[i] - Yextra)
        Yspeed_retro = Yspeed
        Yextra = Yout_ABG[i] + (Yspeed_retro * T0) + (Yaccel * 0.5 * T0 * T0)

        alpha = 3 * (3 * coef * coef - 3 * coef + 2) / (coef * (coef + 1) * (coef + 2))
        beta = 18 * (2 * coef - 1) / (T0 * (coef + 1) * (coef + 2) * coef)
        gamma = 60 / (T0 * T0 * (coef + 1) * (coef + 2) * coef)

        coef += 1
        if i % 100 == 0:
            coef = 1

        r2 = r2_score(S0[::i], Yout_ABG[::i])
        if r2 < 0.6:
            r2 = 1
            r2_previous = 1
            pass
        else:
            if r2 - r2_previous < 0:
                alpha /= r2 ** counter
                beta /= r2 ** counter
                gamma /= r2 ** counter
                counter += 1
            else:
                counter = 1
            r2_previous = r2
    return Yout_ABG


def ABGF(S0):

    iter = len(S0)
    Yin = np.zeros((iter, 1))
    Yout_ABG = np.zeros((iter, 1))
    T0 = 1
    for i in range(iter):
        Yin[i, 0] = float(S0[i])

    Yspeed_retro = (Yin[1, 0] - Yin[0, 0]) / T0
    Yaccel_retro = (Yin[2, 0] - 2 * Yin[1, 0] + Yin[0, 0]) / (T0 * T0)
    Yextra = Yin[0, 0] + (Yspeed_retro * T0) + (Yaccel_retro * 0.5 * T0 * T0)

    alpha = 3 * (3 * 1 * 1 - 3 * 1 + 2) / (1 * (1 + 1) * (1 + 2))
    beta = 18 * (2 * 1 - 1) / (T0 * (1 + 1) * (1 + 2) * 1)
    gamma = 60 / (T0 * T0 * (1 + 1) * (1 + 2) * 1)
    Yout_ABG[0, 0] = Yin[0, 0]
    for i in range(1, iter):
        Yout_ABG[i, 0] = Yextra + alpha * (Yin[i, 0] - Yextra)
        Yspeed = Yspeed_retro + (beta / T0) * (Yin[i, 0] - Yextra)
        Yaccel = Yaccel_retro + (gamma / T0 * T0) * (Yin[i, 0] - Yextra)
        Yspeed_retro = Yspeed
        Yextra = Yout_ABG[i, 0] + (Yspeed_retro * T0) + (Yaccel * 0.5 * T0 * T0)

        alpha = 3 * (3 * i * i - 3 * i + 2) / (i * (i + 1) * (i + 2))
        beta = 18 * (2 * i - 1) / (T0 * (i + 1) * (i + 2) * i)
        gamma = 60 / (T0 * T0 * (i + 1) * (i + 2) * i)

    return Yout_ABG