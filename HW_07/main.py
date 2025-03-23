from Triangle import Triangle
from Rectangle import Rectangle
from Trapeze import Trapeze
from Parallelogram import Parallelogram
from Circle import Circle
from Ball import Ball
from TriangularPyramid import TriangularPyramid
from QuadrangularPyramid import QuadrangularPyramid
from RectangularParallelepiped import RectangularParallelepiped
from Cone import Cone
from TriangularPrism import TriangularPrism


def read_file(file_path):
    figs = []
    with open(file_path, "r") as f:
        for line in f:
            tmp = line.strip().split()
            # if all((int(x) is not None) and (int(x) != 0) for x in tmp[1:]):
            if len(tmp) > 0:
                try:
                    data = [int(x) for x in tmp[1:]]
                    if tmp[0] == 'Triangle':
                        a, b, c = data
                        fig = Triangle(a, b, c)
                    elif tmp[0] == 'Rectangle':
                        a, b = data
                        fig = Rectangle( a, b )
                    elif tmp[0] == 'Trapeze':
                        a, b, c, d = data
                        fig = Trapeze(a, b, c, d)
                    elif tmp[0] == 'Parallelogram':
                        a, b, h = data
                        fig = Parallelogram(a, b, h)
                    elif tmp[0] == 'Circle':
                        r = data[0]
                        fig = Circle(r)
                    elif tmp[0] == 'Ball':
                        r = data[0]
                        fig = Ball(r)
                    elif tmp[0] == 'TriangularPyramid':
                        a, h = data
                        fig = TriangularPyramid(a, h)
                    elif tmp[0] == 'QuadrangularPyramid':
                        a, b, h = data
                        fig = QuadrangularPyramid(a, b, h)
                    elif tmp[0] == 'RectangularParallelepiped':
                        a, b, h = data
                        fig = RectangularParallelepiped(a, b, h)
                    elif tmp[0] == 'Cone':
                        r, h = data
                        fig = Cone(r, h)
                    elif tmp[0] == 'TriangularPrism':
                        a, b, c, h = data
                        fig = TriangularPrism(a, b, c, h)
                    figs.append(fig)

                except ValueError as e:
                    print(f"Помилка при створенні фігури {tmp[0]}: {e}")

    return figs


def check_data(figs):
    max_volume = 0
    max_volume_fig = ''

    for fig in figs:
        tmp_volume = fig.volume()
        if tmp_volume > max_volume:
            max_volume = tmp_volume
            max_volume_fig = fig



    print(f'figure with max volume {max_volume:.3f} is {max_volume_fig}')


if __name__ == '__main__':

    figs = read_file('input03.txt')
    check_data(figs)
    #for fig in figs:
    #     print(f"{fig}")



