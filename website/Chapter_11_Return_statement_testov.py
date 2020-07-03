"""1.Напишите программу, в которой вызывается функция, запрашивающая с ввода две строки и возвращающая
 в программу результат их конкатенации. Выведите результат на экран.

2.Напишите функцию, которая считывает с клавиатуры числа и перемножает их до тех пор, пока не будет введен 0.
 Функция должна возвращать полученное произведение. Вызовите функцию и выведите на экран результат ее работы."""

 # 1
  
def concatenations():
    line_1 = input("Введите первую строку: ")
    line_2 = input("Введите вторую строку: ")
    return line_1 + line_2

print(concatenations())

#2
def multiplier():
    list_of_numbers = []
    while True:
        try:
            list_of_numbers.append(int(input("Введите число: ")))
            if list_of_numbers[-1] == 0:
                list_of_numbers.pop(-1)
                break
        except ValueError:
            print("Используйте для ввода только числа.")
    try: 
        result_of_multiplying = list_of_numbers.pop(1)
        for number in list_of_numbers:
            result_of_multiplying *= number
        return result_of_multiplying
    except IndexError:
        return "Вы не ввели ни одного значения, до ввода 0."

print(multiplier())