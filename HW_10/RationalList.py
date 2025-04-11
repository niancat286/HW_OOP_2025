from Rational import Rational


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
            raise TypeError("Елемент має бути Rational або int")

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        if isinstance(value, Rational):
            self._data[index] = value
        elif isinstance(value, int):
            self._data[index] = Rational(value)
        else:
            raise TypeError("Значення має бути Rational або int")

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
            raise TypeError("Можна додавати лише RationalList, Rational або int")
        return result

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            for el in other:
                self.append(el)
        elif isinstance(other, (Rational, int)):
            self.append(other)
        else:
            raise TypeError("Можна додавати лише RationalList, Rational або int")
        return self

    def sum(self):
        result = Rational(0)
        for r in self._data:
            result += r
        return result


if __name__ == '__main__':
    lst = RationalList([
        Rational(3, 4),
        Rational(1, 2),
        Rational(-5, 2),
        Rational(2, 4),
        Rational(7, 1),
        Rational(1, 7)
    ])

    for r in lst:
        print(r)