from Rational import Rational


class RationalList:
    def __init__(self, iterable=None):
        self._data = []
        if iterable:
            for item in iterable:
                self.append(item)

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
