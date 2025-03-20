import math
from Figure import Figure

class Circle(Figure):
    def __init__(self, r):
        super().__init__()
        if r <= 0:
            raise ValueError("Circle doesn't exist")

        self._r = r


    def perimetr(self):
        return 2 * math.pi * self._r

    def square(self):
        return math.pi * self._r ** 2

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        return self.square()

    def __str__(self):
        return f"Circle {self._r},  volume = {self.volume()}"

