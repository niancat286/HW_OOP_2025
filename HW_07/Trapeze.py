import math

from Figure import Figure


class Trapeze(Figure):

    def check_existance(self, a, b, c, d):
        if a <= 0 or b <= 0 or c <= 0 or d <= 0:
            return False

        if (c + d > abs(a - b)) and (c + abs(a - b) > d) and (d + abs(a - b) > c):
            return True

        return False

    def __init__(self, a, b, c, d):
        if not self.check_existance(a, b, c, d):
            raise ValueError("Trapeze doesn't exist")

        self._a = a
        self._b = b
        self._c = c
        self._d = d

    def dimension(self):
        return 2

    def perimetr(self):
        return self._a + self._b + self._c + self._d

    def square(self):
        a, b, c, d = self._a, self._b, self._c, self._d

        # Формула для знаходження висоти
        h = (math.sqrt((-a + b + c + d) * (a - b + c + d) * (a - b + c - d) *
                       (a - b - c + d))) / (2 * abs(a - b))

        # Формула площі трапеції
        return ((a + b) / 2) * h

    def volume(self):
        return self.square()

    def __str__(self):
        return f"Trapeze {self._a}, {self._b}, {self._c}, {self._d}, volume = {self.volume()}"


if __name__ == '__main__':
    t = Trapeze(10, 6, 5,7)
    print(t.dimension(),
          t.perimetr(),
          t.square(),
          t.squareBase(),
          t.squareSurface(),
          t.height())
    print(t)