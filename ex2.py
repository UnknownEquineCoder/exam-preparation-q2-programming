from __future__ import annotations

from math import gcd


class Fraction:
    def __init__(self, a: int, b: int = 0) -> None:
        if (type(a) is not int) or (type(b) is not int) or (not b):
            raise ValueError("Initialisation Failed")
        divisor = gcd(a, b)
        self.a = a // divisor
        self.b = b // divisor

    @property
    def sign(self) -> bool:
        return self.a * self.b < 0

    def adjust_sign(self) -> Fraction:
        if self.sign and (not self.a < 0):
            self.a = -self.a
            self.b = -self.b
        return self

    def __repr__(self) -> str:
        return f'{"- " if self.sign else ""}{abs(self.a)}/{abs(self.b)}'

    def __add__(self, other: object) -> Fraction:
        if type(other) is int:
            return Fraction(self.a + other * self.b, self.b)
        if type(other) is Fraction:
            return Fraction(
                self.a * other.b + other.a * self.b, self.b * other.b
            ).adjust_sign()
        raise TypeError("Invalid type")

    def __sub__(self, other: object) -> Fraction:
        if type(other) is int:
            return Fraction(self.a - other * self.b, self.b)
        if type(other) is Fraction:
            return Fraction(
                self.a * other.b - other.a * self.b, self.b * other.b
            ).adjust_sign()
        raise TypeError("Invalid type")

    def __mul__(self, other: object) -> Fraction:
        if type(other) is int:
            return Fraction(self.a * other, self.b)
        if type(other) is Fraction:
            return Fraction(self.a * other.a, self.b * other.b).adjust_sign()
        raise TypeError("Invalid type")

    def __truediv__(self, other: object) -> Fraction:
        if type(other) is int:
            return Fraction(self.a, self.b * other)
        if type(other) is Fraction:
            return Fraction(self.a * other.b, self.b * other.a).adjust_sign()
        raise TypeError("Invalid type")

    def __div__(self, other: object) -> Fraction:
        return self.__truediv__(other)


if __name__ == '__main__':
    one_half = Fraction(1, 2)
    two_thirds = Fraction(2, 3)
    four_sixth = Fraction(4, 6)

    negative_one_half = Fraction(-1, 2)

    print(f'{one_half = !r}')
    print(f'{two_thirds = !r}')
    print(f'{four_sixth = !r}')
    print(f'{negative_one_half = !r}')

    print(f'{(one_half + four_sixth) = !r}')
    print(f'{(one_half - two_thirds) = !r}')
    print(f'{(one_half * two_thirds) = !r}')
    print(f'{(one_half / negative_one_half) = !r}')
