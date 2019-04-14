#!/usr/bin/env python3
import numpy as np
from integrate import numba_integrator



def test_lin48():
    print(numba_integrator.midpoint_integrate(lambda x:((1/np.pi)*(np.sin(x)/x)*(np.sin(x/3)/(x/3))*(np.sin(x/5)/(x/5))), 0, 10000000, 10000001))
    print(numba_integrator.midpoint_integrate(lambda x:((1/np.pi)*(np.sin(x)/x)*(np.sin(x/3)/(x/3))*(np.sin(x/5)/(x/5))*(np.sin(x/7)/(x/7))), 0, 10000000, 10000001))
    print(numba_integrator.midpoint_integrate(lambda x:((1/np.pi)*(np.sin(x)/x)*(np.sin(x/3)/(x/3))*(np.sin(x/5)/(x/5))*(np.sin(x/7)/(x/7))*(np.sin(x/9)/(x/9))*(np.sin(x/11)/(x/11))), 0, 10000000, 10000001))
    print(numba_integrator.midpoint_integrate(lambda x:((1/np.pi)*(np.sin(x)/x)*(np.sin(x/3)/(x/3))*(np.sin(x/5)/(x/5))*(np.sin(x/7)/(x/7))*(np.sin(x/9)/(x/9))*(np.sin(x/11)/(x/11))*(np.sin(x/13)/(x/13))), 0, 10000000, 10000001))
    print(numba_integrator.midpoint_integrate(lambda x:((1/np.pi)*(np.sin(x)/x)*(np.sin(x/3)/(x/3))*(np.sin(x/5)/(x/5))*(np.sin(x/7)/(x/7))*(np.sin(x/9)/(x/9))*(np.sin(x/11)/(x/11))*(np.sin(x/13)/(x/13))*(np.sin(x/15)/(x/15))), 0.00000000000000000001, 10000000, 10000001))
    print(numba_integrator.midpoint_integrate(lambda x:((1/np.pi)*(np.sin(x)/x)*(np.sin(x/4)/(x/4))*(np.sin(x/4)/(x/4))*(np.sin(x/7)/(x/7))*(np.sin(x/7)/(x/7))*(np.sin(x/9)/(x/9))*(np.sin(x/9)/(x/9))), 0, 10000000, 10000001))

test_lin48()
