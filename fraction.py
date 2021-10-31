from dataclasses import dataclass
import numpy as np


@dataclass(unsafe_hash=True)
class Fraction:
    _numerator: int      # Numerator
    _denominator: int    # Denomenator

    def __init__(self, numerator, denominator):
        self._numerator = numerator
        self._denominator = denominator

        gcd = np.gcd(numerator, denominator)
        if gcd > 1:
            self._numerator = int(numerator / gcd)
            self._denominator = int(denominator / gcd)

    def __add__(self, f):
        if self._denominator == f._denominator:
            n = self._numerator + f._numerator
            d = self._denominator
        else:
            lcm = int(abs(self._denominator * f._denominator) / np.gcd(self._denominator, f._denominator))
            ns = int(lcm / self._denominator) * self._numerator
            nf = int(lcm / f._denominator) * f._numerator
            n = ns + nf
            d = lcm

        return Fraction(n, d)

    def __sub__(self, f):
        if self._denominator == f._denominator:
            n = self._numerator - f._numerator
            d = self._denominator
        else:
            lcm = int(abs(self._denominator * f._denominator) / np.gcd(self._denominator, f._denominator))
            ns = int(lcm / self._denominator) * self._numerator
            nf = int(lcm / f._denominator) * f._numerator
            n = ns - nf
            d = lcm

        return Fraction(n, d)

    def __mul__(self, f):
        n = self._numerator * f._numerator
        d = self._denominator * f._denominator

        return Fraction(n, d)

    def __truediv__(self, f):
        n = self._numerator * f._denominator
        d = self._denominator * f._numerator

        if n == 0:
            return Fraction(0, 1)

        return Fraction(n, d)


def main():
    a = Fraction(1, 2)
    b = Fraction(3, 4)

    print(a, b)


if __name__ == "__main__":
    main()
