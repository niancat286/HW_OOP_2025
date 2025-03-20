import math
from Figure import Figure

class Ball(Figure):
    def __init__(self, r):
        super().__init__()
        if r <= 0:
            raise ValueError("Circle doesn't exist")

        self._r = r


    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return 4 * math.pi * self._r ** 2

    def squareBase(self):
        return math.pi * self._r ** 2

    def height(self):
        return 2 * self._r

    def volume(self):
        return 4/3 * math.pi * self._r ** 3

    def __str__(self):
        return f"Ball {self._r},  volume = {self.volume()}"


if __name__ == '__main__':
    b = Ball(10)
    print(b.squareSurface())
    print(b)