"""
1. Напишите программу, которая запрашивает с ввода восемь чисел, добавляет их в список. 
На экран выводит их сумму, максимальное и минимальное из них. Для нахождения суммы, максимума 
и минимума воспользуйтесь встроенными в Python функциями sum(), max() и min().

2. Напишите программу, которая генерирует сто случайных вещественных чисел и заполняет ими список. 
Выводит получившийся список на экран по десять элементов в ряд. Далее сортирует список с помощью 
метода sort() и снова выводит его на экран по десять элементов в строке. Для вывода списка напишите 
отдельную функцию, в качестве аргумента она должна принимать список.
"""

# 1
my_list = []
i = 0
while i < 8:
    my_list.append(int(input("Введите число: ")))
    i += 1
print("Сумма всех введенных чисел: {0}".format(sum(my_list)))
print("Максималдьное число: {0}".format(max(my_list)))
print("Минимальное число: {0}".format(min(my_list)))


# 2
import random


def output_to_the_screen(random_list):
    i = 0
    list_to_print = []
    while i < 100:
        list_to_print = random_list[i: i + 11] 
        print(list_to_print)
        i += 10

list_of_random_numbers = []
i = 0
while i < 100:
    list_of_random_numbers.append(random.random())
    i += 1
output_to_the_screen(list_of_random_numbers)
list_of_random_numbers.sort()
output_to_the_screen(list_of_random_numbers)



