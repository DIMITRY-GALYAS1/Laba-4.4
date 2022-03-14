#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from random import randint

"""
Решите следующую задачу: напишите программу, которая будет генерировать матрицу из
случайных целых чисел. Пользователь может указать число строк и столбцов, а также
диапазон целых чисел. Произведите обработку ошибок ввода пользователя.
"""


class Generation:

    def __init__(self, num1, num2, num3, num4):
        self.line = int(num1)
        self.column = int(num2)
        self.min = int(num3)
        self.max = int(num4)

    def make_matrix(self):
        lst = [[randint(self.min, self.max) for z in range(self.column)] for x in range(self.line)]
        for z in lst:
            print()
            for k in z:
                print(k, end=" ")


if __name__ == "__main__":
    try:
        first = input("Количество строк: ")
        second = input("Количество столбцов: ")
        third = input("Минимальная граница диапазона чисел: ")
        fourth = input("Максимальная граница диапазона чисел: ")
        matrix = Generation(first, second, third, fourth)
        matrix.make_matrix()
    except ValueError:
        print("Ошибка, попробуйте снова")
