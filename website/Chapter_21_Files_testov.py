# 1.Создайте файл data.txt по образцу урока. Напишите программу, которая открывает этот 
# файл на чтение, построчно считывает из него данные и записывает строки в другой файл 
# (dataRu.txt), заменяя английские числительные русскими, которые содержатся в списке 
# (["один", "два", "три", "четыре", "пять"]), определенном до открытия файлов.

#еще можно использовать "one three five two".replace("one", "один") ; пары слов можно например хранить в словаре
# word_list = ["один", "два", "три", "четыре", "пять"]
# old_file = None
# new_file = None
# try:
#     old_file = open("data.txt", "r")
#     new_file = open("dataRu.txt", "w")
#     list_of_strings = old_file.readlines()
#     new_list_of_strings = []
#     for string in list_of_strings:
#         index = string.index(" ")
#         string = word_list.pop(0) + string[index:]
#         new_list_of_strings.append(string)
#     new_file.writelines(new_list_of_strings)
# except Exception as err:
#     print(err)
# finally:
#     if old_file is not None:
#         old_file.close()
#     if new_file is not None:
#         new_file.close()

# 2.Создайте файл nums.txt, содержащий несколько чисел, записанных через пробел. Напишите 
# программу, которая подсчитывает и выводит на экран общую сумму чисел, хранящихся в этом файле.
file_read = None
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