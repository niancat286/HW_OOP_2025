import math

from Figure import Figure


class Triangle(Figure):
    def check_triangle_existence(self, a, b, c):
        return (a > 0 and b > 0 and c > 0 and
                a + b > c and a + c > b and b + c > a)

    def __init__(self, a, b, c):
        if not self.check_triangle_existence(a, b, c):
            raise ValueError("Triangle doesn't exist")

        self._a = a
        self._b = b
        self._c = c

    def dimension(self):
        return 2

    def perimetr(self):
        return self.__perimetr()

    def __perimetr(self):
        return self._a + self._b + self._c

    def square(self):
        return self.__square()

    def __square(self):
        p = self.__perimetr() / 2
        return math.sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))

    def volume(self):
        return self.square()

    def __str__(self):
        return f"Triangle {self._a}, {self._b}, {self._c}, volume = {self.volume()}"


if __name__ == '__main__':
    t = Triangle(3,4,5)
    print(t.dimension(),
          t.perimetr(),
          t.square(),
          t.squareBase(),
          t.squareSurface(),
          t.height())
    print(t)