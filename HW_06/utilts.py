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


class Rectangle:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def get_perimeter(self):
        return (self._a + self._b) * 2

    def get_square(self):
        return self._a * self._b


class Trapeze:
    def __init__(self, a, b, c, d):
        self._a = a
        self._b = b
        self._c = c
        self._d = d


    def get_perimeter(self):
        return self._a + self._b + self._c + self._d

    def get_square(self):
        if self._a == self._b:  # Якщо це рівнобічна трапеція
            h = math.sqrt(self._c ** 2 - ((self._b - self._a) / 2) ** 2)
        else:
            num = (-self._a + self._b + self._c + self._d) * (self._a - self._b + self._c + self._d) * (self._a - self._b + self._c - self._d) * (self._a - self._b - self._c + self._d)
            h = math.sqrt(num) / (2 * abs(self._a - self._b))

        return 0.5 * (self._a + self._b) * h


if __name__ == '__main__':
    t1 = Triangle(4,9,11)
    print(t1.get_perimeter())
    print(t1.get_square())

    rec1 = Rectangle(4,5)
    print(rec1.get_perimeter())
    print(rec1.get_square())

    trap1 = Trapeze(10, 6, 5, 7)
    print(trap1.get_perimeter())
    print(trap1.get_square())