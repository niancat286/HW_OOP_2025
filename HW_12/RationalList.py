from Rational import Rational
from Rational import RationalError
from Rational import RationalValueError


class RationalListIterator:
    def __init__(self, data):
        self._sorted_data = sorted(data, key=lambda el: (-el.d, -el.n))
        self._index = 0

    def __next__(self):
        if self._index >= len(self._sorted_data):
            raise StopIteration
        value = self._sorted_data[self._index]
        self._index += 1
        return value


class RationalList:
    def __init__(self, iterable=None):
        self._data = []
        if iterable:
            for item in iterable:
                self.append(item)

    def __iter__(self):
        return RationalListIterator(self._data)

    def append(self, value):
        if isinstance(value, Rational):
            self._data.append(value)
        elif isinstance(value, int):
            self._data.append(Rational(value))
        else:
            raise RationalValueError(RationalValueError.VALUE_ERR, "Можна додавати лише Rational або int")

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        if isinstance(value, Rational):
            self._data[index] = value
        elif isinstance(value, int):
            self._data[index] = Rational(value)
        else:
            raise RationalValueError(RationalValueError.VALUE_ERR, "Значення має бути Rational або int")

    def __len__(self):
        return len(self._data)

    def __add__(self, other):
        result = RationalList(self._data)
        if isinstance(other, RationalList):
            for el in other:
                result.append(el)
        elif isinstance(other, (Rational, int)):
            result.append(other)
        else:
            raise RationalValueError(RationalValueError.VALUE_ERR, "Можна додавати лише RationalList, Rational або int")
        return result

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            for el in other:
                self.append(el)
        elif isinstance(other, (Rational, int)):
            self.append(other)
        else:
            raise RationalValueError(RationalValueError.VALUE_ERR, "Можна додавати лише RationalList, Rational або int")
        return self

    def sum(self):
        result = Rational(0)
        for r in self._data:
            result += r
        return result


def to_rational(elem):
    if isinstance(elem, Rational):
        return elem
    if '/' in elem and len(elem.split('/')) == 2:
        return Rational(elem)
    return Rational(int(elem), 1)


def read_rational_list_from_file(filename):
    with open(filename, 'r') as f:
        for line_number, line in enumerate(f, 1):
            rational_list = RationalList()
            text = line.strip()
            if text:
                try:
                    elements = text.split()
                    for elem in elements:
                        if elem not in ('+', '-', '*', '/'):
                            rational_list.append(to_rational(elem))
                except RationalError as e:
                    print(f"RationalError, Рядок {line_number}: Помилка в елементі '{text}': {e}")
                except RationalValueError as e:
                    print(f"RationalValueError, Рядок {line_number}: Помилка в елементі '{text}': {e}")
            sum_result = Rational(0, 1)
            for num in rational_list:
                sum_result += num
            print(f"Сума раціональних чисел у рядку: {sum_result} ({sum_result()})")


if __name__ == '__main__':
    read_rational_list_from_file("input01_1.txt")
