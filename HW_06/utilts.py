import math

class Triangle:
    def check_triangle_existence(self, a, b, c):
        return a + b > c and a + c > b and b + c > a

    def __init__(self, a, b, c):
        assert self.check_triangle_existence(a, b, c), "Трикутник з такими сторонами не існує"
        self._a = a
        self._b = b
        self._c = c

    def get_perimeter(self):
        return self._a + self._b + self._c

    def get_square(self):
        return math.sqrt(self.get_perimeter()/2*(self.get_perimeter()/2 - self._a)*(self.get_perimeter()/2 - self._b)*(self.get_perimeter()/2 - self._c))


if __name__ == '__main__':
    t1 = Triangle(3,4,5)
    print(t1.get_perimeter())
    print(t1.get_square())