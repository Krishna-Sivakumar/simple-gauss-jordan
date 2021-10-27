from dataclasses import dataclass


@dataclass(frozen=True)
class Fraction:
    _numerator: int      # Numerator
    _denomenator: int    # Denomenator

    def gcd(self, a, b):
        if a > b:
            small = b
        else:
            small = a
        for i in range(1, small+1):
            if ((a%i) == 0 and (b%i) == 0):
                gcd = i

        return gcd

    def __add__(self, f):
        if self._denomenator == f._denomenator:
            n = self._numerator + f._numerator
            d = self._denomenator
        else:
            lcm = int(abs(self._denomenator * f._denomenator) / self.gcd(self._denomenator, f._denomenator))
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


def main():
    a = Fraction(1, 2)
    b = Fraction(3, 4)

    print(a, b)


if __name__ == "__main__":
    main()
