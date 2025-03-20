from Figure2D import Figure2D


class Parallelogram(Figure2D):
    def check_existance(self, a, b, h):
        if a <= 0 or b <= 0 or h <= 0:
            return False

        return True

    def __init__(self, a, b, h):
        super().__init__()
        if not self.check_existance(a, b, h):
            raise ValueError("Parallelogram doesn't exist")

        self._a = a
        self._b = b
        self._h = h

    def perimetr(self):
        return (self._a + self._b) * 2

    def square(self):
        return max(self._a * self._h, self._b * self._h)

    def volume(self):
        return self.square()

    def __str__(self):
        return f"Parallelogram {self._a}, {self._b}, {self._h},  volume = {self.volume()}"


if __name__ == '__main__':
    p = Parallelogram(8, 6, 4)
    print(p)