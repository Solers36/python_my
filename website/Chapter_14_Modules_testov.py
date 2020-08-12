import square


answer = input("Введите цифру соответствующую фигуте площадь которой Вы хочет вычислить? (прямоугольника-1, треугольника-2 или круга-3)")
if answer == 1:
    result_of_calculation = square.rectangle()
