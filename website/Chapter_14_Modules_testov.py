import square


answer = input("Введите цифру соответствующую фигуте, площадь которой Вы хотите вычислить? (прямоугольника-1, треугольника-2 или круга-3) ")
if answer == "1":
    a = float(input("Чему равна длина прямоугольника? "))
    b = float(input("Чему равна ширина прямоугольника? "))
    result_of_calculation = square.rectangle(a, b)
elif answer == "2":
    a = float(input("Чему равна длина основания треугольника? "))
    h = float(input("Чему равна высота треугольника? "))
    result_of_calculation = square.triangle(a, h)
elif answer == "3":
    r = float(input("Чему равен радиус круга? "))
    result_of_calculation = square.circle(r)
else:
    print("Для вычисления площади необходимо ввести цифру соответствующую фигуре(прямоугольника-1, треугольника-2 или круга-3)")
    print("А Вы ввели '{0}'.".format(answer))
print("Площадь равна: {0}".format(result_of_calculation))