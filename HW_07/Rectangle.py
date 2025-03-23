from Figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        if a <= 0 or b <= 0:
            raise ValueError("Rectangle doesn't exist")

        self._a = a
        self._b = b

    def dimension(self):
        return 2

    def perimetr(self):
        return self.__perimetr()

    def __perimetr(self):
        return (self._a + self._b) * 2

    def square(self):
        return self.__square()

    def __square(self):
        return self._a * self._b

    def volume(self):
        return self.square()

    def __str__(self):
        return f"Rectangle {self._a}, {self._b}, volume = {self.volume()}"


if __name__ == '__main__':
    t = Rectangle(2,4)
    print(t.dimension(),
          t.perimetr(),
          t.square(),
          t.squareBase(),
          t.squareSurface(),
          t.height())
    print(t)