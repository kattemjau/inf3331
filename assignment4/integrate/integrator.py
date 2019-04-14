#!/usr/bin/env python3

# from lamtest import myfunc
import random
import inspect
import matplotlib.pyplot as plt

def integrate(f, a, b, n):
    # //lage en graph som regner ut areal av punkter
    intervall = abs((b-a)/n)
    start = a
    suum = 0

    y=[]
    x=[]
    for i in range(0, n):
        # make a graph of combinations of x
        start += intervall
        suum += f(start) * intervall

        x.append(start)
        y.append(f(start))

    plt.plot(x, y, 'b', label=inspect.getsource(f))
    plt.legend()
    plt.savefig('quadratic_error.png')
    # plt.show()
    return suum


def midpoint_integrate(f, a, b, n):
    intervall = abs((b-a)/n)
    start = a
    suum = 0

    #x=np.linspace(a, b, n)
    y=[]
    x=[]
    for i in range(0, n+1):
        # make a graph of combinations of x
        # plt.plot(f(start), intervall, 'o', label='points')
        suum += f(start+(intervall/2)) * (intervall)
        start += intervall

    return suum
