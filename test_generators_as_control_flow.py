from math import sqrt

from hypothesis import given, strategies as st
from pytest import approx

from generators_as_control_flow import newt


@given(m=st.floats(-10, 10), b=st.floats(0, 10))
def test_newt_approximates_sqrt(m, b):
    f = lambda x: m * x ** 2 - b
    f_prime = lambda x: 2 * m * x
    gen = newt(f, f_prime, 10)
    for _ in range(20):
        next(gen)
    assert next(gen) == approx(sqrt(b), abs=1e-3, rel=1e-3)
