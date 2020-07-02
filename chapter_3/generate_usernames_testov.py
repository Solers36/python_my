"""Модифицируйте программу generate_usernames.py так, чтобы в
каждой строке она выводила информацию о двух пользователях,
ограничив длину имени 17 символами; через каждые 64 строки
программа должна выводить символ перевода формата и в начале
каждой страницы она должна выводить заголовки столбцов.
Это достаточно сложно. Вам потребуется сохранить заголовки
столбцов в переменных, чтобы потом их можно было использовать
по мере необходимости, и изменить спецификаторы формата, что бы
обеспечить вывод более коротких имен. Один из способов обеспечить
постраничный вывод заключается в том, чтобы сохранить все
выводимые строки в списке, а затем выполнить обход списка, используя
оператор извлечения среза с шагом для получения элементов
слева и справа и применяя функцию zip() для их объединения.
Решение приводится в файле generate_usernames_ans.py, а достаточно
большой объем исходных данных вы найдете в файле data/users2.txt."""

import collections
import sys


ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)

User = collections.namedtuple("User",
                              "username forename middlename surname id")


def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} file1 [file2 [... fileN]]".format(
              sys.argv[0]))
        sys.exit()

    usernames = set()
    users = {}
    for filename in sys.argv[1:]:
        with open(filename, encoding="utf8") as file:
            for line in file:
                line = line.rstrip()
                if line:
                    user = process_line(line, usernames)
                    users[(user.surname.lower(), user.forename.lower(),
                           user.id)] = user
    print_users(users)


def process_line(line, usernames):
    fields = line.split(":")
    username = generate_username(fields, usernames)
    user = User(username, fields[FORENAME], fields[MIDDLENAME],
                fields[SURNAME], fields[ID])
    return user


def generate_username(fields, usernames):
    username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] +
                 fields[SURNAME]).replace("-", "").replace("'", ""))
    username = original_name = username[:8].lower()
    count = 1
    while username in usernames:
        username = "{0}{1}".format(original_name, count)
        count += 1
    usernames.add(username)
    return username


def print_users(users):
    namewidth = 17
    usernamewidth = 9

    header = "{0:<{nw}} {1:^6} {2:{uw}} ".format(
        "Name", "ID", "Username", nw=namewidth, uw=usernamewidth)
    separator = "{0:-<{nw}} {0:-<6} {0:-<{uw}} ".format(
        "", nw=namewidth, uw=usernamewidth)

    users_to_print = []

    for key in sorted(users):
        user = users[key]
        initial = ""
        if user.middlename:
            initial = " " + user.middlename[0]
        name = "{0.surname}, {0.forename}{1}".format(user, initial)
        users_to_print.append("{0:.<{nw}.{nw}} ({1.id:4}) {1.username:{uw}}".format(
            name, user, nw=namewidth, uw=usernamewidth))

   
    line_number = 0
    lines_per_page = 64
    for first_column, second_column in zip(users_to_print[0::2], users_to_print[1::2]):
        if line_number == 0:
            print("{0} {0}\n{1} {1}".format(header, separator))
        print("{0}  {1}".format(first_column, second_column))
        line_number += 1
        if line_number == lines_per_page:
            print("\n")
            line_number = 0
    if users_to_print[-1] != second_column:
        print(users_to_print[-1])



main()