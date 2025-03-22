import math

from Triangle import Triangle


class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self._h = h

    def dimension(self):
        return 3

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        l = math.sqrt(self._h ** 2 + (self._a ** 2 / 12))
        p = super().perimetr()
        return p * l / 2

    def squareBase(self):
        sq = super().square()
        return sq

    def height(self):
        return self._h

    def volume(self):
        return self.squareBase() * self._h / 3

    def __str__(self):
        return f"TriangularPyramid {self._a}, {self._h}, volume = {self.volume()}"


if __name__ == '__main__':
    t = TriangularPyramid(3, 3)
    print(t.dimension(),
          t.perimetr(),
          t.square(),
          t.squareBase(),
          t.squareSurface(),
          t.height())
    print(t)
