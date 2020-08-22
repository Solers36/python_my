"""
1.Заполните список случайными числами. Используйте в коде цикл for, функции range() и randint().

2.Если объект range (диапазон) передать встроенной в Python функции list(), то она преобразует 
его к списку. Создайте таким образом список с элементами от 0 до 100 и шагом 17.

3.В заданном списке, состоящем из положительных и отрицательных чисел, посчитайте количество 
отрицательных элементов. Выведите результат на экран.

4.Напишите программу, которая заполняет список пятью словами, введенными с клавиатуры, измеряет 
длину каждого слова и добавляет полученное значение в другой список. Например, список слов – 
['yes', 'no', 'maybe', 'ok', 'what'], список длин – [3, 2, 5, 2, 4]. Оба списка должны выводиться на экран.
"""

# 1
import random

list_1 = []
for i in range(10):
    list_1.append(random.randint(-100, 100))

# 2
list_2 = list(range(0, 101, 17))

# 3
list_3 = []
for i in sorted(list_1):
    if i < 0:
        list_3.append(i)
    else:
        break
print(len(list_3))

# 4
word_list = []
length_list = []
for i in range(5):
    i = input("Введите слово: ")
    word_list.append(i)
for word in word_list:               # можно было запихну в один цикл for, но мне показалось, что задание подразумевает 
    length_list.append(len(word))    # такое решение, хотя оно менее опимальное.
print(word_list)
print(length_list)