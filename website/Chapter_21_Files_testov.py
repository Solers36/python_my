"""
1. Создайте файл data.txt по образцу урока. Напишите программу, которая открывает этот 
файл на чтение, построчно считывает из него данные и записывает строки в другой файл 
(dataRu.txt), заменяя английские числительные русскими, которые содержатся в списке 
(["один", "два", "три", "четыре", "пять"]), определенном до открытия файлов.

2.Создайте файл nums.txt, содержащий несколько чисел, записанных через пробел. Напишите 
программу, которая подсчитывает и выводит на экран общую сумму чисел, хранящихся в этом файле.
"""

# 1.
word_list = ["один", "два", "три", "четыре", "пять"]
fh = None
nfh = None
try:
    fh = open("data.txt", "r")
    nfh = open("dataRu.txt", "w")
    list_of_strings = fh.readlines()
    new_list_of_strings = []
    for string in list_of_strings:
        index = string.index(" ")
        string = word_list.pop(0) + string[index:]
        new_list_of_strings.append(string)
    nfh.writelines(new_list_of_strings)
except Exception as err:
    print(err)
finally:
    if fh is not None:
        fh.close()
    if nfh is not None:
        nfh.close()

# 2.
fh = None
try:
    file_read = open("nums.txt", "r")
    string_of_numbers = file_read.read()
    list_of_number = string_of_numbers.split(" ")
    result_of_computation = 0.0
    for number in list_of_number:
        result_of_computation += float(number)
    print(result_of_computation)
except Exception as err:
    print(err)
finally:
    if file_read is not None:
        file_read.close()