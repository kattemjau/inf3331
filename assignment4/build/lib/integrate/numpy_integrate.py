#!/usr/bin/env python3

# import matplotlib.pyplot as plt
import numpy as np


def numpy_integrate(f, a, b, n):
    intervall = abs((b-a)/n)

    x=np.linspace(a, b, n+1)
    func=np.vectorize(f)
    res=func(x)

    # plt.plot(x, y, 'b', label='function')
    # plt.legend()
    # plt.show()
    return np.sum(res[1:]*intervall)


def midpoint_integrate(f, a, b, n):
    intervall = abs((b-a)/n)

    x=np.linspace(a, b, n+1)
    func=np.vectorize(f)
    res=func(x+intervall/2)

    return np.sum(res[1:]*(intervall))
