"""
Напишите программу, демонстрирующую содержимое каталогов по>
добно тому, как это делает команда dir в Windows или ls в UNIX. Пре>
имущество наличия собственной программы отображения каталогов
состоит в том, что мы можем заложить в нее предпочитаемые парамет>
ры по умолчанию и использовать одну и ту же программу в любой сис>
теме, не утруждая себя необходимостью запоминать различия между
командами dir и ls. Программа должна иметь следующий интерфейс:
Usage: ls.py [options] [path1 [path2 [... pathN]]]
The paths are optional; if not given . is used.
Options:
-h, --help show this help message and exit
-H, --hidden show hidden files [default: off]
-m, --modified show last modified date/time [default: off]
-o ORDER, --order=ORDER
order by ('name', 'n', 'modified', 'm', 'size', 's')
[default: name]
-r, --recursive recurse into subdirectories [default: off]
-s, --sizes show sizes [default: off]
(Вывод программы был несколько изменен, чтобы уместить его в ши>
рину книжной страницы.)
Ниже приводится пример вывода содержимого небольшого каталога
с помощью команды ls.py –ms –os misc/:
2007-04-10 15:49:01 322 misc/chars.pyw
2007-08-01 11:24:57 1,039 misc/pfa!bug.pyw
2007-10-12 09:00:27 2,445 misc/test.lout
2007-04-10 15:50:31 2,848 misc/chars.png
2008-02-11 14:17:03 12,184 misc/abstract.pdf
2008-02-05 14:22:38 109,788 misc/klmqtintro.lyx
2007-12-13 12:01:14 1,359,950 misc/tracking.pdf
misc/phonelog/
7 files, 1 directory
Мы использовали группировку ключей командной строки (она обраба>
тывается модулем optparse автоматически), но тот же самый эффект
можно было бы получить, используя ключи по отдельности, напри>
мер, ls.py –m –s –os misc/, или даже применив более плотную группи>
ровку, ls.py –msos misc/, или используя длинные имена параметров,
ls.py ––modified ––sizes ––order=size misc/, или любую их комбинацию.
в вывод программы «скрытых» файлов или каталогов, имена которых
начинаются с точки (.).
Упражнение довольно сложное. Вам придется ознакомиться с доку>
ментацией к модулю optparse, чтобы узнать, как объявлять парамет>
ры, которые принимают значение True, и как определить фиксирован>
ный перечень параметров. Если пользователь определяет в вызове па>
раметр ––recursive, программа должна выполнить обход файлов (но не
каталогов) с помощью функции os.walk(); в противном случае она
должна использовать для получения списка файлов и каталогов функ>
цию os.listdir().
Еще один подводный камень – организация пропуска скрытых ката>
логов при рекурсии. Их можно удалять из списка dirs, возвращаемого
os.walk(), и тем самым пропускать их, модифицируя список. Но будь>
те внимательны – не присваивайте новое значение непосредственно
переменной dirs, поскольку это не повлияет на список, на который она
ссылается, а просто (и совершенно бесполезно) заместит его. Подход,
использованный в решении, основан на присваивании срезу всего спи>
ска, то есть dirs[:] = [dir for dir in dirs if not dir.startswith(".")].
Лучший способ группировки разрядов при отображении
размеров файлов состоит в том, чтобы импортировать
модуль locale, вызвать функцию locale.setlocale() для
получения региональных настроек пользователя и ис>
пользовать спецификатор формата n. Общий размер про>
граммы ls.py, разбитой на четыре функции, будет состав>
лять около 130 строк.
"""
import os
import locale
import time
from optparse import OptionParser

locale.setlocale(locale.LC_ALL, "en_us.UTF-8")


def get_options():
    usage = "Usage: %prog [options] [path1 [path2 [... pathN]]]\nThe paths are optional; if not given . is used."
    parser = OptionParser(usage=usage)
    parser.add_option("-H", "--hidden", default=False, action="store_true",
                      help="show hidden files [default: off]")
    parser.add_option("-m", "--modified", default=False, action="store_true",
                      help="show last modified date/time [default: off]")
    parser.add_option("-o", "--order", default=False, action="store",
                      choices=['name', 'n', 'modified', 'm', 'size', 's'],
                      help="order by ('name', 'n', 'modified', 'm', 'size', 's') [default: name]")
    parser.add_option("-r", "--recursive", default=False, action="store_true",
                      help="recurse into subdirectories [default: off]")
    parser.add_option("-s", "--sizes", default=False, action="store_true",
                      help="show sizes [default: off]")
    (options, args) = parser.parse_args()
    if not args:
        parser.print_help()
    return options, args


def recursive(files, args, options, number_of_files, number_of_folders):
    for path in args:
            for way, dirs, files in os.walk(path):
                if not options.hidden:
                    dirs[:] = [dir for dir in dirs
                               if not dir.startswith(".")]
                for name in files:
                    if not options.hidden and name.startswith("."):
                        continue
                    fullname = os.path.join(way, name)
                    if fullname.startswith("./"):
                        fullname = fullname[2:]
                    files.append(fullname)
                    number_of_files += 1
                number_of_folders += len(dirs)
    return files, [], number_of_files, number_of_folders


def not_recursive(dirs, files, args, options, number_of_files, number_of_folders):
    for path in args:
        if os.path.isfile(path):
            files.append(path)
            number_of_files += 1
            continue
        for name in os.listdir(path):
            if not options.hidden:
                if name.startswith("."):
                    continue
            fullname = os.path.join(path, name)
            if fullname.startswith("./"):
                fullname = fullname[2:]
            if os.path.isfile(fullname):
                files.append(fullname)
                number_of_files += 1
            else:
                dirs.append(fullname)
                number_of_folders += 1
    return files, dirs, number_of_files, number_of_folders


def configurator_line(files, dirs, options):
    lines = []
    for name in files:

        modified = ""
        if options.modified:
            modified = time.strftime(
                "%Y-%m-%d  %H:%M:%S  ", time.gmtime(os.path.getmtime(name)))
        else:
            modified = " " * 20  # надо подумать

        size = ""
        if options.sizes:
            size = "{1:>12n}".format(os.path.getsize(name))
        else:
            size = " " * 12  # надо подумать
        name_dir = os.path.join(os.path.dirname(name), name)

        line = modified + size + name_dir

        lines.append((name, line))

    # if options.order in ('size', 's'):
    #     lines = sorted(lines, key=lambda x: os.path.getsize(lines[x][0]))
    # elif options.order in ('modified', 'm'):
    #     lines = sorted(lines, key=lambda x: os.path.getmtime((lines[x][0]))
    # elif options.order in ('name', 'n'):
    #     pass
    #     # lines = sorted(lines, key=lambda x: lines[x][0])
    for dir in dirs:
        dir = os.path.join(os.path.dirname(dir) + dir)
        line = 32 * " " + dir
        lines.append((dir, line))
    return lines

def print_content(lines):
    for line in lines:
        print(line[1])

def print_end(number_of_files, number_of_folders):
    print("{0} file{1}, {2} director{3}".format(
          "{0:n}".format(number_of_files) if number_of_files else "no",
          "s" if number_of_files != 1 else "",
          "{0:n}".format(number_of_folders) if number_of_folders else "no",
          "ies" if number_of_folders != 1 else "y"))

def main():
    number_of_files=0
    number_of_folders=0
    options, args=get_options()
    dirs=[]
    files=[]
    if options.recursive:
        files, dirs, number_of_files, number_of_folders=recursive(
            files, args, options, number_of_files, number_of_folders)
    else:
        files, dirs, number_of_files, number_of_folders=not_recursive(
            dirs, files, args, options, number_of_files, number_of_folders)

    lines=configurator_line(files, dirs, options)

    print_content(lines)

    print_end(number_of_files, number_of_folders)



main()
