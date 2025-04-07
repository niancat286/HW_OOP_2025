from math import gcd


class Rational:
    def __init__(self, n, d=None):
        if d is None:
            if isinstance(n, str):
                n, d = map(int, n.strip().split('/'))
            else:
                raise TypeError("Неправильний тип ініціалізації")
        if d == 0:
            raise ZeroDivisionError("Знаменник не може дорівнювати нулю")
        self.n = n
        self.d = d
        self._simplify()

    def _simplify(self):
        g = gcd(self.n, self.d)
        self.n //= g
        self.d //= g
        # Зберігаємо знак у чисельнику
        if self.d < 0:
            self.n *= -1
            self.d *= -1

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        if isinstance(other, Rational):
            new_n = self.n * other.d + other.n * self.d
            new_d = self.d * other.d
            return Rational(new_n, new_d)

        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        if isinstance(other, Rational):
            new_n = self.n * other.d - other.n * self.d
            new_d = self.d * other.d
            return Rational(new_n, new_d)

        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        if isinstance(other, Rational):
            return Rational(self.n * other.n, self.d * other.d)

        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        if isinstance(other, Rational):
            if other.n == 0:
                raise ZeroDivisionError
            return Rational(self.n * other.d, self.d * other.n)

        return NotImplemented

    def __call__(self):
        return self.n / self.d

    def __getitem__(self, key):
        if key == "n":
            return self.n
        elif key == "d":
            return self.d
        else:
            raise KeyError

    def __setitem__(self, key, value):
        if key == "n":
            self.n = value
        elif key == "d":
            if value == 0:
                raise ZeroDivisionError
            self.d = value
        else:
            raise KeyError

        self._simplify()

    def __str__(self):
        return f"{self.n}/{self.d}" if self.d != 1 else f"{self.n}"









