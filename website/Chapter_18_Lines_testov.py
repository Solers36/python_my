# 1
#  Вводится строка, включающая строчные и прописные буквы. Требуется вывести ту же строку в одном регистре, 
# который зависит от того, каких букв больше. При равном количестве преобразовать в нижний регистр. Например, 
# вводится строка "HeLLo World", она должна быть преобразована в "hello world", потому что в исходной строке 
# малых букв больше. В коде используйте цикл for, строковые методы upper() (преобразование к верхнему регистру) 
# и lower() (преобразование к нижнему регистру), а также методы isupper() и islower(), проверяющие регистр 
# строки или символа.

from my_checks import awesome_input

def upper_or_lower(line):
    if line.isupper() or line.islower() :
        return line
         
    lowercase_letters = []
    uppercase_letters = []

    for word in line:
        if word.islower():
            lowercase_letters.append(word)
        elif word.isupper():
            uppercase_letters.append(word)
    if len(lowercase_letters) >= len(uppercase_letters):
        return line.lower()
    else:
        return line.upper()

#print(upper_or_lower(input("Введите строку: ")))
# print(upper_or_lower("sdfgsdDSF").__eq__("sdfgsddsf"))
# print(upper_or_lower("sdfgsdadsf").__eq__("sdfgsdadsf"))
# print(upper_or_lower("DSF").__eq__("DSF"))
# print(upper_or_lower("sdfgsdDSF").__eq__("SDFGSDDSF") == False)
# print(upper_or_lower("sdfgsdDSF").__eq__("sdfgsddsf"))


# # 2
# # Строковый метод isdigit() проверяет, состоит ли строка только из цифр. Напишите программу, которая 
# # запрашивает с ввода два целых числа и выводит их сумму. В случае некорректного ввода программа не должна 
# # завершаться с ошибкой, а должна продолжать запрашивать числа. Обработчик исключений try-except использовать нельзя.

def get_int(message):
    while True:
        raw = input(message)
        if raw.isdigit():
            return int(raw)

first = get_int("Введите первое целое число: ")
second = get_int("Введите второе целое число: ")
amount = first + second
print("Сумма введенных чисел равна: ", amount)


