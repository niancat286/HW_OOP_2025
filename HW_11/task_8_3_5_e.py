"""Обов’язкові вимоги до виконання завдань
В усіх задачах цієї лабораторної роботи потрібно
•    побудувати рекурентне співвідношення (за необхідності, якщо воно явно не задане в умові задачі);
•    описати генератор-функцію для генерування членів заданої послідовності;
•    описати програму обчислення необхідного члена послідовності використовуючи цикл з лічильником або цикл з умовою."""

import math


def gen(x):
    n = 1
    while True:
        yield x**n / n
        n += 2


def approx_res(x, eps):
    g = gen(x)
    S = 0
    temp = next(g)
    counter = 1

    while abs(temp) >= eps:
        S += temp
        temp = next(g)
        counter += 1

    return 2 * S, counter


x = float(input("x= "))
eps = float(input("eps= "))


res, n = approx_res(x, eps)
res_math = math.log((1 + x) / (1 - x))

print(f"{res = }, {n=}")
print(f"{res_math = }")