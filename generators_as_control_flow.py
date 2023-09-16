from collections.abc import Generator
from typing import Callable


def newt(
    f: Callable, f_prime: Callable, guess: float,
) -> Generator[float, None, None]:
    while True:
        guess -= f(guess) / f_prime(guess)
        yield guess


def newt2(f, var, guess):
    f_prime = f.diff(var)
    while True:
        guess -= f.subs(var).evalf() / f_prime.subs(var).evalf()
        yield guess
