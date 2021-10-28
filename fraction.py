from dataclasses import dataclass
import numpy as np


@dataclass(unsafe_hash=True)
class Fraction:
    _numerator: int      # Numerator
    _denomenator: int    # Denomenator

    def __init__(self, numerator, denomenator):
        self._numerator = numerator
        self._denomenator = denomenator

        gcd = np.gcd(numerator, denomenator)
        if gcd > 1:
            self._numerator = int(numerator / gcd)
            self._denomenator = int(denomenator / gcd)

    def __add__(self, f):
        if self._denomenator == f._denomenator:
            n = self._numerator + f._numerator
            d = self._denomenator
        else:
            lcm = int(abs(self._denomenator * f._denomenator) /
                      np.gcd(self._denomenator, f._denomenator))
            ns = int(lcm / self._denomenator) * self._numerator
            nf = int(lcm / f._denomenator) * f._numerator
            n = ns + nf
            d = lcm

        return Fraction(n, d)

    def __sub__(self, f):
        if self._denomenator == f._denomenator:
            n = self._numerator - f._numerator
            d = self._denomenator
        else:
            lcm = int(abs(self._denomenator * f._denomenator) / np.gcd(self._denomenator, f._denomenator))
            ns = int(lcm / self._denomenator) * self._numerator
            nf = int(lcm / f._denomenator) * f._numerator
            n = ns - nf
            d = lcm

        return Fraction(n, d)

    def __mul__(self, f):
        n = self._numerator * f._numerator
        d = self._denomenator * f._denomenator

        return Fraction(n, d)

    def __truediv__(self, f):
        n = self._numerator * f._denomenator
        d = self._denomenator * f._numerator

        return Fraction(n, d)


def main():
    a = Fraction(1, 2)
    b = Fraction(3, 4)

    print(a, b)


if __name__ == "__main__":
    main()
