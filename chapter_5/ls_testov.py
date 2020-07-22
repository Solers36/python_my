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
2007!04!10 15:49:01 322 misc/chars.pyw
2007!08!01 11:24:57 1,039 misc/pfa!bug.pyw
2007!10!12 09:00:27 2,445 misc/test.lout
2007!04!10 15:50:31 2,848 misc/chars.png
2008!02!11 14:17:03 12,184 misc/abstract.pdf
2008!02!05 14:22:38 109,788 misc/klmqtintro.lyx
2007!12!13 12:01:14 1,359,950 misc/tracking.pdf
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
from optparse import OptionParser


def file_search():
    list_of_all_files = os.listdir(".")
    list_of_files_lst = []
    for filename in list_of_all_files:
        if filename.endswith(".lst"):
            list_of_files_lst.append(filename)
    return list_of_files_lst


usage = "Usage: %prog [options] [path1 [path2 [... pathN]]]\nThe paths are optional; if not given . is used."
parser = OptionParser(usage=usage)
parser.add_option("-H", "--hidden", default=False, action="store_true",
                  help="show hidden files [default: off]")
parser.add_option("-m", "--modified", default=False, action="store_true",
                  help="show last modified date/time [default: off]")
parser.add_option("-o", "--order", default="name",
                  help="order by ('name', 'n', 'modified', 'm', 'size', 's') [default: name]")
parser.add_option("-r", "--recursive", default=False, action="store_true",
                  help="recurse into subdirectories [default: off]")
parser.add_option("-s", "--sizes", default=False, action="store_true",
                  help="show sizes [default: off]")

(options, args) = parser.parse_args()
