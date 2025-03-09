import math


class Triangle:
    def check_triangle_existence(self, a, b, c):
        return a + b > c and a + c > b and b + c > a

    def __init__(self, a, b, c):
        if not self.check_triangle_existence(a, b, c):
            self._a = self._b = self._c = None
            return

        self._a = a
        self._b = b
        self._c = c

    def get_perimeter(self):
        if None in [self._a, self._b, self._c]:
            return None
        return self._a + self._b + self._c

    def get_square(self):
        if None in [self._a, self._b, self._c]:
            return None

        p = self.get_perimeter() / 2
        return math.sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))


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
            try:
                h = math.sqrt(self._c ** 2 - ((self._b - self._a) / 2) ** 2)
                if h < 0:
                    return None
            except ValueError:
                return None
        else:
            num = (-self._a + self._b + self._c + self._d) * (self._a - self._b + self._c + self._d) * (self._a - self._b + self._c - self._d) * (self._a - self._b - self._c + self._d)
            if num < 0:
                return None
            h = math.sqrt(num) / (2 * abs(self._a - self._b))

        return 0.5 * (self._a + self._b) * h


class Parallelogram:
    def __init__(self, a, b, h):
        self._a = a
        self._b = b
        self._h = h

    def get_perimeter(self):
        return (self._a + self._b) * 2

    def get_square(self):
        return max(self._a * self._h, self._b * self._h)


class Circle:
    def __init__(self, r):
        self._r = r

    def get_perimeter(self):
        return 2 * math.pi * self._r

    def get_square(self):
        return math.pi * self._r ** 2


if __name__ == '__main__':
    t1 = Triangle(4, 9, 11)
    print(t1.get_perimeter())
    print(t1.get_square())

    rec1 = Rectangle(4, 5)
    print(rec1.get_perimeter())
    print(rec1.get_square())

    trap1 = Trapeze(10, 6, 5, 7)
    print(trap1.get_perimeter())
    print(trap1.get_square())

    par1 = Parallelogram(8, 6, 4)
    print(par1.get_perimeter())
    print(par1.get_square())

    c1 = Circle(6)
    print(c1.get_perimeter())
    print(c1.get_square())
