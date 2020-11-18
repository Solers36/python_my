"""
Отладка действий с двоичными форматами может оказаться доста-
точно сложным делом, и в этом может помочь инструмент, который
выводит шестнадцатеричные дампы содержимого двоичных файлов. 
Напишите программу, которая выводила бы в консоли следую-
щий текст справки:
Usage: xdump.py [options] file1 [file2 [... fileN]]
Options:
-h, --help      show this help message and exit
-b BLOCKSIZE, --blocksize=BLOCKSIZE
                block size (8..80) [default: 16]
-d, --decimal   decimal block numbers [default: hexadecimal]
-e ENCODING, --encoding=ENCODING
                encoding (ASCII..UTF-32) [default: UTF-8]
(Перевод:
Порядок использования: xdump.py [параметры] file1 [file2 [... fileN]]
Параметры:
-h, -help       вывести это справочное сообщение и выйти
-b BLOCKSIZE, --blocksize=BLOCKSIZE
                Размер блока (8..80) [по умолчанию: 16]
-d, --decimal   блоки десятичных чисел
                [по умолчанию: шестнадцатеричные]
-e ENCODING, --encoding=ENCODING
                кодировка (ASCII..UTF-32) [по умолчанию: UTF-8]
конец перевода)
С помощью этой программы при наличии файла, созданного объек-
том BinaryRecordFile, в котором хранятся записи в формате "<i10s"
(обратный порядок следования байтов, 4-байтовое целое со знаком,
10-байтовая строка байтов), установив размер блока в соответствии
с размером одной записи (15 байтов, включая байт состояния),
можно было бы получить ясное представление о содержимом файла. 
Например:

xdump.py -b15 test.dat
Block    Bytes                             UTF-8 characters
-------- --------------------------------- ----------------
00000000 02000000 00416C70 68610000 000000 .....Alpha.....
00000001 01140000 00427261 766F0000 000000 .....Bravo.....
00000002 02280000 00436861 726C6965 000000 .(...Charlie...
00000003 023C0000 0044656C 74610000 000000 .<...Delta.....
00000004 02500000 00456368 6F000000 000000 .P...Echo......

Каждый байт представлен двумя шестнадцатеричными цифрами;
пробел между группами из четырех байтов (между группами из
восьми шестнадцатеричных цифр) добавляется исключительно ра-
ди удобочитаемости. В этом примере видно, что вторая запись
(«Bravo») была удалена, потому что ее байт состояния имеет значе-
ние 0x01, а не 0x02, используемое для обозначения непустых и не-
удаленных записей.
Для обработки параметров командной строки используйте модуль
optparse. (Указав «тип» параметра, можно заставить модуль opt-
parse выполнять преобразование значения параметра с размером
блока из строкового представления в целочисленное.) Может ока-
заться совсем непросто правильно выводить строку заголовка для
произвольно заданного размера блока и строки символов в послед-
нем блоке, поэтому обязательно проверьте работу программы с раз-
ными размерами блоков (например, 8, 9, 10, …, 40). Кроме того, не
забывайте, что в файлах переменной длины последний блок может
оказаться коротким. Для обозначения непечатаемых символов ис-
пользуйте точку, как показано в примере.
Программу можно уместить менее чем в 70 строк, распределенных
на две функции.
"""
import os
from optparse import OptionParser


def main():
    usage = "Usage: %prog [options] file1 [file2 [... fileN]]"
    parser = OptionParser(usage=usage)
    parser.add_option("-b", "--blocksize", default=16, dest="blocksize", type="int",
                      help="block size (8..80) [default: %default]")
    parser.add_option("-d", "--decimal", default=False, action="store_true",
                      help="decimal block numbers [default: hexadecimal]")
    parser.add_option("-e", "--encoding", default="UTF-8", action="store",
                      help="encoding (ASCII..UTF-32) [default: %default")
    (options, args) = parser.parse_args()
    if not args:
        parser.print_help()
    if not 8 <= options.blocksize <= 80:
        parser.error("blocksize must be in the range from 8 to 80")
    if options.decimal:
        format_block_number = "{0:0>8}"
    else:
        format_block_number = "{0:0>8X}"

    blocksize = int(options.blocksize)
    block_hexdecimal = (2 * blocksize) + (blocksize // 4)
    encoding = options.encoding.upper()
    
    for filename in args:
        count = 0
        print("\n", filename, sep="")
        print("{0: <8} {1: <{block_hexdecimal}} {2: <{blocksize}}".format("Block", "Bytes",
                                                                       encoding + " characters", 
                                                                       block_hexdecimal=block_hexdecimal,
                                                                       blocksize=blocksize))
        print("{0:-<8} {0:-<{block_hexdecimal}} {0:-<{blocksize}}".format("", block_hexdecimal=block_hexdecimal,
                                                                       blocksize=blocksize))
        file_data = None
        try:
            file_data = open(filename, "r+b")
            record = file_data.read(blocksize)
            while record != b'':
                print_data = ""
                i = 0
                text_from_encoding = ""

                for byte in record:
                    print_data += "{0:0>2X}".format(int(hex(byte), 16))
                    i += 1
                    if i == 4:
                        print_data += " "
                        i = 0
                    encoded_byte = bytes([byte]).decode(encoding, 'ignore')
                    if 32 <= byte <= 126:
                        text_from_encoding += encoded_byte
                    else:
                        text_from_encoding += "."

                if len(print_data) < block_hexdecimal :
                    print_data = "{0: <{block_hexdecimal}}".format(print_data, 
                                                                    block_hexdecimal=block_hexdecimal)

                print(format_block_number.format(count), "{0} {1}".format(print_data,
                                                                          text_from_encoding))
                record = file_data.read(blocksize)
                count += 1

        except Exception as err:
            print(err)
        finally:
            if file_data is not None:
                file_data.close()


main()