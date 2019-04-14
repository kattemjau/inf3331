#!/usr/bin/env python3
from polynommials import Polynomial, sample_usage


def test_degree():
    p= Polynomial([1, 2, 3])
    assert p.degree() == 2
    p= Polynomial([1, 2, 3, 6, 8, 8,8, 8,9, 8, 8,8])
    assert p.degree() == 11

def test_add():
    p= Polynomial([1, 2, 3])
    q= Polynomial([1, 2, 3, 4, 5])
    assert (p+2).coefficients()==[3, 2, 3]
    assert (p+q).coefficients()==[2, 4, 6, 4, 5]


def test_sub():
    p= Polynomial([2, 3, 4])
    q= Polynomial([1, 2, 3])
    # print((p-q).coefficients())
    assert (p-q).coefficients()==[1, 1, 1]

def test_mul():
    p= Polynomial([1, 2, 3])

    assert (p*1).coefficients()==[1,2,3]
    assert (p*2).coefficients()==[2,4,6]



sample_usage()

test_degree()
test_add()
test_sub()
test_mul()
