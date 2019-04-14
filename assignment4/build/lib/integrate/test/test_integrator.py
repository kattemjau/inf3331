#!/usr/bin/env python3

import time
from integrate import integrator
from integrate import numpy_integrate
from integrate import numba_integrator

def test_integral_of_constant_function():
    assert abs(integrator.integrate(lambda x:2, 0, 1, 1) - 2) < 1E-20
    # print(integrator.integrate(lambda x:2, 0, 1, 400000))
    assert abs(integrator.integrate(lambda x:2, 0, 1, 400000) - 2) < 1E-10

def test_integral_of_linear_function():
    # print(integrator.integrate(lambda x:x**2, 0, 1, 4000000))
    assert abs(integrator.integrate(lambda x:x**2, 0, 1, 4000000) - 1/3) < 1E-5


# take time
def test_numpy():
    assert abs(numpy_integrate.numpy_integrate(lambda x:x**2, 0, 1, 4000000) - 1/3) < 1E-5


def test_numba():
    assert abs(numba_integrator.numba_integrator(lambda x:x**2, 0, 1, 4000000) - 1/3) < 1E-5



print("times for all functions")
start=time.time()
test_integral_of_constant_function()
stop=time.time()
print("integral constant =", (stop-start))
start1=time.time()
test_integral_of_linear_function()
stop1=time.time()
print("integral linerer =", (stop1-start1))
start2=time.time()
test_numpy()
stop2=time.time()
print("integral numpy =", (stop2-start2))
print("numpy raskere: ", ((stop1-start1)-(stop2-start2)))

start3=time.time()
test_numba()
stop3=time.time()
print("integral numba =", (stop3-start3))
#numba will improove speed if run several times
