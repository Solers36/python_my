"""При запуске программа должна создать список всех файлов с расшире>
нием .lst в текущем каталоге. Воспользуйтесь функцией os.listdir("."),
чтобы получить список всех файлов, и отфильтруйте из него те файлы,
которые не имеют расширения .lst. В случае отсутствия таких файлов
программа должна попросить пользователя ввести имя файла и доба>
вить расширение .lst, если пользователь не сделал этого. Если были
найдены один или более файлов .lst, программа должна вывести их
имена в виде списка пронумерованных строк, начиная с 1. Пользова>
телю должно быть предложено ввести номер желаемого файла или 0; в
последнем случае программа должна попросить у пользователя ввести
имя нового файла.
Если был указан существующий файл, программа должна прочитать
его содержимое. Если файл пуст или было указано имя нового файла,
программа должна вывести сообщение «no items are in the list» (спи>
сок не содержит элементов).
В случае отсутствия элементов должно быть предложено два варианта
действий: «Add» (добавить) и «Quit» (выйти). Если список содержит
один или более элементов, строки из списка должны выводиться про>
нумерованными, начиная с 1, а из доступных действий должны быть
предложены варианты «Add» (добавить), «Delete» (удалить), «Save»
(сохранить) (если файл еще не сохранялся) и «Quit» (выйти). Если
пользователь выбирает действие «Quit» и при этом имеются несохра>
ненные изменения, ему должна быть предоставлена возможность со>
хранить их. Ниже приводится пример сеанса работы с программой
(большая часть пустых строк, а также заголовок «List Keeper», кото>
рый выводится всякий раз при выводе списка, были удалены из лис>
тинга):
Choose filename: movies
!! no items are in the list !!
[A]dd [Q]uit [a]: a
Add item: Love Actually
1: Love Actually
[A]dd [D]elete [S]ave [Q]uit [a]: a
Add item: About a Boy
1: About a Boy
2: Love Actually
[A]dd [D]elete [S]ave [Q]uit [a]:
Add item: Alien
1: About a Boy
2: Alien
3: Love Actually
[A]dd [D]elete [S]ave [Q]uit [a]: k
ERROR: invalid choice!!enter one of 'AaDdSsQq'
Press Enter to continue...
[A]dd [D]elete [S]ave [Q]uit [a]: d
Delete item number (or 0 to cancel): 2
1: About a Boy
2: Love Actually
[A]dd [D]elete [S]ave [Q]uit [a]: s
Saved 2 items to movies.lst
Press Enter to continue...
1: About a Boy
2: Love Actually
[A]dd [D]elete [Q]uit [a]:
Add item: Four Weddings and a Funeral
1: About a Boy
2: Four Weddings and a Funeral
3: Love Actually
[A]dd [D]elete [S]ave [Q]uit [a]: q
Save unsaved changes (y/n) [y]:
Saved 3 items to movies.lst
Функция main() должна быть не очень большой (не более 30 строк)
и должна содержать только основной цикл программы. Напишите
функцию, которая будет получать имя нового или существующего
файла (и в последнем случае загружать элементы списка), и функцию,
которая будет выводить перечень доступных действий и принимать
выбор пользователя. Напишите также функции, которые будут добав>
лять элемент, удалять элемент, выводить список (либо имен файлов,
либо элементов списка строк), загружать список и сохранять список.
Вставьте в свою программу копии функций get_string() и get_integer()
из программы make_html_skeleton.py или напишите свои собственные
версии.
При выводе элементов списка строк или имен файлов ширина поля
для вывода номеров строк должна быть равна 1, если список содержит
менее десяти элементов, 2 – если в списке менее 100 элементов и 3 –
в противном случае.
Всегда выводите элементы списка в алфавитном порядке, без учета ре>
гистра символов, и следите за состоянием списка (за наличием несо>
храненных изменений). Действие «Save» должно предлагаться только
при наличии несохраненных изменений, а перед выходом программа
должна спрашивать у пользователя, не желает ли он сохранить изме>
нения, только если таковые имеются. Добавление и удаление элемен>
тов считаются действиями, которые изменяют список, а после выпол>
нения операции сохранения список снова должен считаться неизме>
ненным.
"""

import os


def main():
    dictionary_for_printing = {}
    file_content = []
    result_of_search = file_search()
    if result_of_search:
        dictionary_for_printing = creating_a_dictionary(result_of_search)
        printer(dictionary_for_printing)
        while True:
            try:
                number_file = int(input(
                    "Enter the file number to open or 0 to create a new file: "))
                if number_file in dictionary_for_printing:
                    filename = dictionary_for_printing[number_file]
                    file_content = read_file(filename)
                    dictionary_for_printing = creating_a_dictionary(
                        file_content)
                    break
                elif number_file == 0:
                    filename = file_creation()
                    break
                else:
                    raise ValueError(
                        "The string cannot be empty and must contain numbers from 0 to {0}".format(len(result_of_search)))
            except ValueError as err:
                print(err)

    else:
        print("Files with the extension .lst not found.")
        filename = file_creation()

    main_loop(file_content, filename)


def file_search():
    list_of_all_files = os.listdir(".")
    list_of_files_lst = []
    for filename in list_of_all_files:
        if filename.endswith(".lst"):
            list_of_files_lst.append(filename)
    return list_of_files_lst


def file_creation():
    filename = input("Choose filename: ")
    if not filename.endswith(".lst"):
        filename += ".lst"
    saving_file(filename)
    return filename


def read_file(filename):
    active_file = None
    try:
        active_file = open(filename, "r", encoding="utf8")
        content_active_file = []
        for line in active_file:
            content_active_file.append(line.replace("\n", ""))
        return content_active_file
    except EnvironmentError as err:
        print("ERROR", err)

    finally:
        active_file.close()


def numbers_length(length):
    if length < 10:
        number = 1
    elif length < 100:
        number = 2
    else:
        number = 3
    return number


def creating_a_dictionary(list_line):
    length = len(list_line)
    dictionary_for_printing = dict(
        zip(range(1, length + 1), sorted(list_line, key=str.lower)))
    return dictionary_for_printing


def printer(dictionary_for_printing):
    length = len(dictionary_for_printing)
    number_of_characters = numbers_length(length)
    print("\n")
    print("List Keeper")
    for key in dictionary_for_printing:
        print("{0:{2}}: {1}".format(
            key, dictionary_for_printing[key], number_of_characters))


def message_constructor(delete, save, user_selection):
    message = "[A]dd {0}{1}[Q]uit".format(delete, save)
    message += ": " if user_selection is None else " [{0}]: ".format(
        user_selection)
    return message


def get_string(message, user_selection, posible_values, error_message):

    while True:
        try:
            line = input(message)
            if line not in posible_values or len(line) > 1:
                raise ValueError()
            if not line:
                if user_selection is not None:
                    return user_selection
                else:
                    raise ValueError()
            return line
        except ValueError:
            print(error_message)


def main_loop(file_content, filename):
    user_selection = None
    delete = ""
    save = ""

    while True:
        if len(file_content) != 0:
            delete = "[D]elete "
            dictionary_for_printing = creating_a_dictionary(file_content)
            printer(dictionary_for_printing)
            message = message_constructor(delete, save, user_selection)
            user_selection = get_string(message, user_selection, 'AaDdSsQq',
                                        "ERROR: invalid choice--enter one of 'AaDdSsQq'\nPress Enter to continue...")
        else:
            delete = ""
            print("\n-- no items are in the list --")
            message = message_constructor(delete, save, None)
            user_selection = get_string(message, user_selection, 'AaDdSsQq',
                                        "ERROR: invalid choice--enter one of 'AaDdSsQq'\nPress Enter to continue...")

        if user_selection in "Aa":
            file_content = adding_line(file_content)
            save = "[S]ave "

        if user_selection in "Dd" and delete == "[D]elete ":
            file_content = deleting_line(file_content)
            save = "[S]ave "

        if user_selection in "Ss" and save == "[S]ave ":
            saving_file(filename, file_content)
            save = ""
            user_selection = "a"

        if user_selection in "Qq":
            if save == "[S]ave ":
                if get_string("Save unsaved changes (y/n) [y]: ", "y", "YyNn", "ERROR: invalid choice--enter one of 'y/n'") == "y":
                    saving_file(filename, file_content)
            break


def adding_line(file_content):
    new_line = input("Add item: ")
    file_content.append(new_line)
    return file_content


def deleting_line(file_content):
    while True:
        try:
            string_to_delete = int(input("Delete item number (or 0 to cancel): "))
            if string_to_delete == 0:
                return file_content
            else:
                index = string_to_delete - 1
                file_content = sorted(file_content, key=str.lower)
                file_content.pop(index)
            return file_content
        except Exception:
            print(
                "ERROR: invalid choice--enter number from 1 to {0}".format(len(file_content)))


def saving_file(filename, file_content=None):
    active_file = None
    try:
        active_file = open(filename, "w", encoding="utf8")
        if file_content is not None:

            for line in file_content:
                active_file.write(line + "\n")
            print("Saved {0} items to {1}".format(len(file_content), filename))

    except EnvironmentError as err:
        print("ERROR", err)

    finally:
        active_file.close()


main()


# def test_creating_a_dictionary():
#     dictiorary_1 = creating_a_dictionary(["2.lst", "1.lst", "3.lst", "4.lst"])
#     dictionary_2 = {1: "1.lst", 2: "2.lst", 3: "3.lst", 4: "4.lst"}
#     result = dictiorary_1 == dictionary_2
#     print(result)


# def unit_tests():
#     test_creating_a_dictionary()


# unit_tests()
