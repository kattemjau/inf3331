#!/usr/bin/env python3
import numpy as np
import numba as nb

@nb.autojit
def numba_integrator(f, a, b, n):
        intervall = abs((b-a)/n)
        start = a
        suum = 0

        y=[]
        x=[]
        for i in range(0, n+1):
            suum += f(start) * intervall
            start += intervall
        return suum

@nb.autojit

def midpoint_integrate(f, a, b, n):
    intervall = abs((b-a)/n)
    start = a
    suum = 0

    y=[]
    x=[]
    for i in range(0, n+1):
        suum += f(start+intervall/2) * (intervall)
        start += intervall
    return suum
