import math


class Triangle:
    def check_triangle_existence(self, a, b, c):
        return (a > 0 and b > 0 and c > 0 and
                a + b > c and a + c > b and b + c > a)

    def __init__(self, a, b, c):
        if not self.check_triangle_existence(a, b, c):
            raise ValueError("Triangle doesn't exist")

        self._a = a
        self._b = b
        self._c = c

    def get_perimeter(self):
        return self._a + self._b + self._c

    def get_square(self):
        p = self.get_perimeter() / 2
        return math.sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))

    def __str__(self):
        return f"Triangle {self._a}, {self._b}, {self._c}, perimetr = {self.get_perimeter()}, square = {self.get_square()}"


class Rectangle:
    def __init__(self, a, b):
        if a <= 0 or b <= 0:
            raise ValueError("Rectangle doesn't exist")

        self._a = a
        self._b = b

    def get_perimeter(self):
        return (self._a + self._b) * 2

    def get_square(self):
        return self._a * self._b

    def __str__(self):
        return f"Rectangle {self._a}, {self._b}, perimetr = {self.get_perimeter()}, square = {self.get_square()}"


class Trapeze:

    def check_existance(self, a, b, c, d):
        if a <= 0 or b <= 0 or c <= 0 or d <= 0:
            return False

        if (c + d > abs(a - b)) and (c + abs(a - b) > d) and (d + abs(a - b) > c):
            return True

        return False


    def __init__(self, a, b, c, d):
        if not self.check_existance(a, b, c, d):
            raise ValueError("Trapeze doesn't exist")

        self._a = a
        self._b = b
        self._c = c
        self._d = d

    def get_perimeter(self):
        return self._a + self._b + self._c + self._d

    def get_square(self):
        a, b, c, d = self._a, self._b, self._c, self._d

        # Формула для знаходження висоти
        h = (math.sqrt((-a + b + c + d) * (a - b + c + d) * (a - b + c - d) * (a - b - c + d))) / (2 * abs(a - b))

        # Формула площі трапеції
        return ((a + b) / 2) * h



    def __str__(self):
        return f"Trapeze {self._a}, {self._b}, {self._c},  {self._d}, perimetr = {self.get_perimeter()}, square = {self.get_square()}"


class Parallelogram:
    def check_existance(self, a, b, h):
        if a <= 0 or b <= 0 or h <= 0:
            return False

        return True

    def __init__(self, a, b, h):
        if not self.check_existance(a, b, h):
            raise ValueError("Parallelogram doesn't exist")

        self._a = a
        self._b = b
        self._h = h

    def get_perimeter(self):
        return (self._a + self._b) * 2

    def get_square(self):
        return max(self._a * self._h, self._b * self._h)

    def __str__(self):
        return f"Parallelogram {self._a}, {self._b}, {self._h},  perimetr = {self.get_perimeter()}, square = {self.get_square()}"


class Circle:
    def __init__(self, r):
        if r <= 0:
            raise ValueError("Circle doesn't exist")

        self._r = r

    def get_perimeter(self):
        return 2 * math.pi * self._r

    def get_square(self):
        return math.pi * self._r ** 2

    def __str__(self):
        return f"Circle {self._r},  perimetr = {self.get_perimeter()}, square = {self.get_square()}"


if __name__ == '__main__':
    t1 = Triangle(4, 9, 11)
    print(t1.get_perimeter())
    print(t1.get_square())
    print(t1)

    rec1 = Rectangle(4, 5)
    print(rec1.get_perimeter())
    print(rec1.get_square())
    print(rec1)

    trap1 = Trapeze(10, 6, 5, 7)
    print(trap1.get_perimeter())
    print(trap1.get_square())
    print(trap1)

    par1 = Parallelogram(8, 6, 4)
    print(par1.get_perimeter())
    print(par1.get_square())
    print(par1)

    c1 = Circle(6)
    print(c1.get_perimeter())
    print(c1.get_square())

    print(c1)
