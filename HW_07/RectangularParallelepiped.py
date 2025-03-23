import math

from Rectangle import Rectangle


class RectangularParallelepiped(Rectangle):
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
        return super().perimetr() * self._h

    def squareBase(self):
        sq = super().square()
        return sq

    def height(self):
        return self._h

    def volume(self):
        return self.squareBase() * self._h

    def __str__(self):
        return f"RectangularParallelepiped {self._a}, {self._b}, {self._h}, volume = {self.volume()}"


if __name__ == '__main__':
    t = RectangularParallelepiped(3,4,5)
    print(t.dimension(),
          t.perimetr(),
          t.square(),
          t.squareBase(),
          t.squareSurface(),
          t.height())
    print(t)
