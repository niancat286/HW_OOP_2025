import math
from Figure import Figure


class Circle(Figure):
    def __init__(self, r):
        if r <= 0:
            raise ValueError("Circle doesn't exist")
        self._r = r

    def dimension(self):
        return 2

    def perimetr(self):
        return self.__perimetr()

    def __perimetr(self):
        return 2 * math.pi * self._r

    def square(self):
        return self.__square()

    def __square(self):
        return math.pi * self._r ** 2

    def volume(self):
        return self.square()

    def __str__(self):
        return f"Circle {self._r},  volume = {self.volume()}"


if __name__ == '__main__':
    t = Circle(10)
    print(t.dimension(),
          t.perimetr(),
          t.square(),
          t.squareBase(),
          t.squareSurface(),
          t.height())
    print(t)
