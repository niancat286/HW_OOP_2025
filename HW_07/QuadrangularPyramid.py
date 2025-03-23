import math

from Rectangle import Rectangle


class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self._h = h

    def dimension(self):
        return 3

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        la = ((self._b / 2) ** 2 + self._h ** 2) ** 0.5
        lb = ((self._a / 2) ** 2 + self._h ** 2) ** 0.5
        return self._a * la + self._b * lb

    def squareBase(self):
        sq = super().square()
        return sq

    def height(self):
        return self._h

    def volume(self):
        return self.squareBase() * self._h / 3

    def __str__(self):
        return f"QuadrangularPyramid {self._a}, {self._b}, {self._h}, volume = {self.volume()}"


if __name__ == '__main__':
    t = QuadrangularPyramid(3, 3, 3)
    print(t.dimension(),
          t.perimetr(),
          t.square(),
          t.squareBase(),
          t.squareSurface(),
          t.height())
    print(t)
