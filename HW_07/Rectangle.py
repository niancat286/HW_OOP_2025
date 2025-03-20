from Figure2D import Figure2D


class Rectangle(Figure2D):
    def __init__(self, a, b):
        super().__init__()
        if a <= 0 or b <= 0:
            raise ValueError("Rectangle doesn't exist")

        self._a = a
        self._b = b

    def perimetr(self):
        return (self._a + self._b) * 2

    def square(self):
        return self._a * self._b

    def volume(self):
        return self.square()

    def __str__(self):
        return f"Rectangle {self._a}, {self._b}, volume = {self.volume()}"


if __name__ == '__main__':
    r = Rectangle(2,4)
    print(r)