#!/usr/bin/env python3

import time
import numpy as np
from integrate import integrator
from integrate import numpy_integrate
from integrate import numba_integrator

def test_lin():
    return integrator.midpoint_integrate(lambda x:np.sin(x), 0, np.pi, 1000000)

# take time
def test_numpy():
    return numpy_integrate.midpoint_integrate(lambda x:np.sin(x), 0, np.pi, 1500000)

def test_numba():
    return numba_integrator.midpoint_integrate(lambda x:np.sin(x), 0, np.pi, 1000000)



print(test_lin())
print(test_numpy())
print(test_numba())
