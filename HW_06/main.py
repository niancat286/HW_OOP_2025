from utilts import *


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

                    figs.append(fig)

                except ValueError as e:
                    print(f"Помилка при створенні фігури {tmp[0]}: {e}")

    return figs


def chec_data(figs):
    max_perimeter = 0
    max_perimeter_fig = []
    max_square = 0
    max_square_fig = []
    for fig in figs:
        tmp_perimeter = fig.get_perimeter()
        if tmp_perimeter is not None and tmp_perimeter > max_perimeter:
            max_perimeter = tmp_perimeter
            # max_perimeter_fig = tmp

        tmp_square = fig.get_square()
        if tmp_square is not None and tmp_square > max_square:
            max_square = tmp_square
            # max_square_fig = tmp

    print(f'figure with max perimeter {max_perimeter:.3f} is {max_perimeter_fig}')
    print(f'figure with max square {max_square:.3f} is {max_square_fig}')


if __name__ == '__main__':

    figs = read_file('input01.txt')
    for fig in figs:
        print(f"{fig}")


    # check_file('input02.txt')
    # check_file('input03.txt')
