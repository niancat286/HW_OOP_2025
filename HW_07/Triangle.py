import math

from Figure2D import Figure2D


class Triangle(Figure2D):
    def check_triangle_existence(self, a, b, c):
        return (a > 0 and b > 0 and c > 0 and
                a + b > c and a + c > b and b + c > a)

    def __init__(self, a, b, c):
        super().__init__()
        if not self.check_triangle_existence(a, b, c):
            raise ValueError("Triangle doesn't exist")

        self._a = a
        self._b = b
        self._c = c

    def perimetr(self):
        return self._a + self._b + self._c

    def square(self):
        p = self.perimetr() / 2
        return math.sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))

    def volume(self):
        return self.square()

    def __str__(self):
        return f"Triangle {self._a}, {self._b}, {self._c}, volume = {self.square()}"


if __name__ == '__main__':
    t = Triangle(3,4,5)
    print(t)