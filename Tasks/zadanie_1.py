#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Решите следующую задачу: напишите программу, которая запрашивает ввод двух значений.
Если хотя бы одно из них не является числом, то должна выполняться конкатенация, т. е.
соединение, строк. В остальных случаях введенные числа суммируются.
"""


class Test:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def summa(self):
        k = int(self.first) + int(self.second)
        print("Сумма чисел: ", k)

    def concatenation(self):
        z = self.first + self.second
        print("Результат конкатенации: ", z)


if __name__ == "__main__":
    try:
        num1 = input("Введите первое число: ")
        num2 = input("Введите второе число: ")
        test = Test(num1, num2)
        test.summa()
    except ValueError:
        test = Test(num1, num2)
        test.concatenation()
