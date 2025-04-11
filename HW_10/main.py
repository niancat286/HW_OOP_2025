from RationalList import RationalList
from Rational import Rational


def read_rational_list_from_file(filename):
    rlist = RationalList()
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            for part in parts:
                if '/' in part:
                    n, d = map(int, part.split('/'))
                else:
                    n, d = int(part), 1
                rlist.append(Rational(n, d))
    return rlist


if __name__ == '__main__':
    rlist = read_rational_list_from_file("input03.txt")
    for r in rlist:
        print(r, end=' ')


