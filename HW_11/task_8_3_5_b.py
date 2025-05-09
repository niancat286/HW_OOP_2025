"""Обов’язкові вимоги до виконання завдань
В усіх задачах цієї лабораторної роботи потрібно
•    побудувати рекурентне співвідношення (за необхідності, якщо воно явно не задане в умові задачі);
•    описати генератор-функцію для генерування членів заданої послідовності;
•    описати програму обчислення необхідного члена послідовності використовуючи цикл з лічильником або цикл з умовою."""


def gen(N):
    Pn = 2
    yield Pn

    for k in range(2, N + 1):
        xk = 1 + 1/(k**2)
        Pn *= xk
        yield Pn


if __name__ == '__main__':
    n = int(input("n= "))

    for elem in gen(n):
        print(elem)
        el = elem

    print('---------')
    print(el)