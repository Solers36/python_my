"""
1. Вводится строка, включающая строчные и прописные буквы. Требуется вывести ту же строку в одном регистре, 
который зависит от того, каких букв больше. При равном количестве преобразовать в нижний регистр. Например, 
вводится строка "HeLLo World", она должна быть преобразована в "hello world", потому что в исходной строке 
малых букв больше. В коде используйте цикл for, строковые методы upper() (преобразование к верхнему регистру) 
и lower() (преобразование к нижнему регистру), а также методы isupper() и islower(), проверяющие регистр 
строки или символа.

2. Строковый метод isdigit() проверяет, состоит ли строка только из цифр. Напишите программу, которая 
запрашивает с ввода два целых числа и выводит их сумму. В случае некорректного ввода программа не должна 
завершаться с ошибкой, а должна продолжать запрашивать числа. Обработчик исключений try-except использовать нельзя.
"""

# 1
lines = input("Введите строку: ")
lowercase_letters = []
uppercase_letters = []
for word in lines:
    if word.islower():
        lowercase_letters.append(word)
    elif word.isupper():
        uppercase_letters.append(word)
if len(lowercase_letters) >= len(uppercase_letters):
    print(lines.lower())
else:
    print(lines.upper())

# 2
while True:
    first = input("Введите первое целое число: ")
    if first.isdigit():
        while True:
            second = input("Введите второе целое число: ")
            if second.isdigit():
                break
        break
amount = int(first) + int(second)
print("Сумма введенных чисел равна: ", amount)