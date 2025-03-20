import math
from Figure2D import Figure2D


class Circle(Figure2D):
    def __init__(self, r):
        super().__init__()
        if r <= 0:
            raise ValueError("Circle doesn't exist")

        self._r = r

    def perimetr(self):
        return 2 * math.pi * self._r

    def square(self):
        return math.pi * self._r ** 2
    
    def volume(self):
        return self.square()

    def __str__(self):
        return f"Circle {self._r},  volume = {self.volume()}"
    

if __name__ == '__main__':
    c = Circle(10)
    print(c.square())
    print(c)

