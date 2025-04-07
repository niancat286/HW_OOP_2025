from RationalList import RationalList
from Rational import Rational


def read_rational_list_from_file(filename):
    with open(filename, 'r') as f:
        for idx, line in enumerate(f, 1):
            rlist = RationalList()
            tokens = line.strip().split()
            for token in tokens:
                if '/' in token:
                    rlist += Rational(token)
                else:
                    rlist += int(token)
            print(f"Рядок {idx}: сума = {rlist.sum()}")


if __name__ == '__main__':
    read_rational_list_from_file("input03.txt")



