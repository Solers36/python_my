"""
1. Создайте словарь, связав его с переменной school, и наполните данными, которые бы отражали количество 
учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.). Внесите изменения в словарь согласно следующему: 
а) в одном из классов изменилось количество учащихся, б) в школе появился новый класс, 
с) в школе был расформирован (удален) другой класс. Вычислите общее количество учащихся в школе.

2. Создайте словарь, где ключами являются числа, а значениями – строки. Примените к нему метод items(), 
полученный объект dict_items передайте в написанную вами функцию, которая создает и возвращает новый словарь, 
"обратный" исходному, т. е. ключами являются строки, а значениями – числа.
"""

# 1
import random


school = {}
leters = ["а", 'б', 'в', 'г']
for number in range(1, 12):
    for leter in range(random.randint(1, 4)):
        leter = leters.pop(0)
        key = "{}{}".format(number, leter)
        school[key] = random.randint(12, 25)
    leters = ["а", 'б', 'в', 'г']

# a)
while True:
    key = "{}{}".format(random.randint(1, 11), leters[random.randint(0, 3)])
    if school.get(key) != None:
        school[key] = random.randint(1, 11)
        break

# б)
while True:
    key = "{}{}".format(random.randint(1, 11), leters[random.randint(0, 3)])
    if school.get(key) == None:
        school[key] = random.randint(1, 11)
        break

# с)
while True:
    key = "{}{}".format(random.randint(1, 11), leters[random.randint(0, 3)])
    if school.get(key) != None:
        school.pop(key)
        break

amount = 0
for i in school:
    amount += school[i]
print("1.")
print("Сумма всех учеников школы равна: ", amount, ".", sep="")

# 2
def dictionary_reverse(dict_items):
    new_dict = {}
    for key, value in dict_items:
        new_dict[value] = key
    return new_dict


dict_default = {1: 'one', 2: 'two', 3: 'three'}
dict_items = dict_default.items()
print("2.")
print(dictionary_reverse(dict_items))