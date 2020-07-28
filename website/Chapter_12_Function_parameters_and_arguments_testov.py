"""Функция getInput() не имеет параметров, запрашивает ввод с клавиатуры и возвращает 
в основную программу полученную строку.

Функция testInput() имеет один параметр. В теле она проверяет, можно ли переданное ей 
значение преобразовать к целому числу. Если можно, возвращает логическое True. Если нельзя – False.

Функция strToInt() имеет один параметр. В теле преобразовывает переданное значение к 
целочисленному типу. Возвращает полученное число.

Функция printInt() имеет один параметр. Она выводит переданное значение на экран и 
ничего не возвращает.

В основной ветке программы вызовите первую функцию. То, что она вернула, передайте во 
вторую функцию. Если вторая функция вернула True, то те же данные (из первой функции) 
передайте в третью функцию, а возвращенное третьей функцией значение – в четвертую."""


def getInput():
    return input("Введите строку: ")


def testInput(text):
    try:
        int(text)
        return True

    except ValueError:
        return False
        


def strToInt(text):
    return int(text)


def printInt(number):
    print(number) 

user_text = getInput()

if testInput(user_text) == True:
    printInt(strToInt(user_text))
else:
    print("Введенная строка не является числом.")