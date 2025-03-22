import math

from Circle import Circle


class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self._h = h

    def dimension(self):
        return 3

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        L = super().perimetr()
        l = (self._r ** 2 + self._h ** 2) ** 0.5
        return L * l / 2

    def squareBase(self):
        return super().square()

    def height(self):
        return self._h

    def volume(self):
        return 1 / 3 * self.squareBase() * self._h

    def __str__(self):
        return f"Cone {self._r},  volume = {self.volume()}"


if __name__ == '__main__':
    t = Cone(10, 3)
    print(t.dimension(),
          t.perimetr(),
          t.square(),
          t.squareBase(),
          t.squareSurface(),
          t.height())
    print(t)