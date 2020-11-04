# 1
# Создайте словарь, связав его с переменной school, и наполните данными, которые бы отражали количество 
# учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.). Внесите изменения в словарь согласно следующему: 
# а) в одном из классов изменилось количество учащихся, 
# б) в школе появился новый класс, 
# с) в школе был расформирован (удален) другой класс. Вычислите общее количество учащихся в школе.

import random


school = {}
leters = ["а", 'б', 'в', 'г']

for number in range(1, 12):
    letter_index = 0
    for leter in range(random.randint(1, 4)):
        leter = leters[letter_index]#вместо того, что бы создавать 12 массивов
        key = "{}{}".format(number, leter)
        school[key] = random.randint(12, 25)
        letter_index += 1

# a)в одном из классов изменилось количество учащихся, 
while True:
    key = "{}{}".format(random.randint(1, 11), leters[random.randint(0, 3)])
    if school.get(key) != None:
        school[key] = random.randint(1, 11)
        break

# б)в школе появился новый класс, 
while True:
    key = "{}{}".format(random.randint(1, 11), leters[random.randint(0, 3)])
    if school.get(key) == None:
        school[key] = random.randint(1, 11)
        break

# с)в школе был расформирован (удален) другой класс. Вычислите общее количество учащихся в школе.
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
# Создайте словарь, где ключами являются числа, а значениями – строки. Примените к нему метод items(), 
# полученный объект dict_items передайте в написанную вами функцию, которая создает и возвращает новый словарь, 
# "обратный" исходному, т. е. ключами являются строки, а значениями – числа.
def dictionary_reverse(dict_items):
    new_dict = {}
    for key, value in dict_items:
        new_dict[value] = key
    return new_dict


dict_default = {1: 'one', 2: 'two', 3: 'three'}
dict_items = dict_default.items()
print("\n2.")
print(dictionary_reverse(dict_items))