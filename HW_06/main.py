from utilts import *


def check_file(file_path):
    with open(file_path, "r") as f:
        max_perimeter = 0
        max_perimeter_fig = []
        max_square = 0
        max_square_fig = []
        figs = []
        for line in f:
            tmp = line.strip().split()
            if all(int(x) != 0 for x in tmp[1:]):
                try:
                    if tmp[0] == 'Triangle':
                        fig = Triangle(*(int(x) for x in tmp[1:]))
                    elif tmp[0] == 'Rectangle':
                        fig = Rectangle(*(int(x) for x in tmp[1:]))
                    elif tmp[0] == 'Trapeze':
                        fig = Trapeze(*(int(x) for x in tmp[1:]))
                    elif tmp[0] == 'Parallelogram':
                        fig = Parallelogram(*(int(x) for x in tmp[1:]))
                    elif tmp[0] == 'Circle':
                        fig = Circle(*(int(x) for x in tmp[1:]))

                    figs.append(fig)

                    tmp_perimeter = fig.get_perimeter()
                    if tmp_perimeter is not None and tmp_perimeter > max_perimeter:
                        max_perimeter = tmp_perimeter
                        max_perimeter_fig = tmp

                    tmp_square = fig.get_square()
                    if tmp_square is not None and tmp_square > max_square:
                        max_square = tmp_square
                        max_square_fig = tmp

                except Exception as e:
                    print(f"Помилка при створенні фігури {tmp[0]}: {e}")

        print(f'figure with max perimeter {max_perimeter:.3f} is {max_perimeter_fig}')
        print(f'figure with max square {max_square:.3f} is {max_square_fig}')


if __name__ == '__main__':



    check_file('input01.txt')
    # check_file('input02.txt')
    # check_file('input03.txt')


