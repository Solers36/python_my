
# 1. 
# Чтобы избежать изменения исходного списка, не обязательно использовать кортеж. Можно создать его копию с помощью 
# метода списка copy() или взять срез от начала до конца [:]. Скопируйте список первым и вторым способом и убедитесь, 
# что изменение копий никак не отражается на оригинале.

first_list = [1, 2, 3]
second_list = ["4", "5", "6"]

third_list = first_list.copy()
fourth_list = second_list[:]

third_list[1] = "2"
fourth_list.append(7)

print(first_list, second_list, third_list, fourth_list, sep="\n", end="\n\n")

# 2
# Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно. Также заполните второй кортеж 
# числами от -5 до 0. Для заполнения кортежей числами напишите одну функцию. Объедините два кортежа с помощью оператора +, 
# создав тем самым третий кортеж. С помощью метода кортежа count() определите в нем количество нулей. Выведите на экран 
# третий кортеж и количество нулей в нем.
import random


def creating_a_random_tuple(first, last, size):
    new_list = []
    for i in range(size):
        i = random.randint(first, last)
        new_list.append(i)
    return tuple(new_list)

first_tuple = creating_a_random_tuple(0, 5, 10)
second_tuple = creating_a_random_tuple(-5, 0, 10)
third_tuple = first_tuple + second_tuple

print(third_tuple)
print("Колличество нулей в кортеже: {}.".format(third_tuple.count(0)))