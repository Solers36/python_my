#!/usr/bin/env python3

"""
>>> import shutil
>>> import sys

>>> S = struct.Struct("<15s")
>>> fileA = os.path.join(tempfile.gettempdir(), "fileA.dat")
>>> fileB = os.path.join(tempfile.gettempdir(), "fileB.dat")
>>> for name in (fileA, fileB):
...    try:
...        os.remove(name)
...    except EnvironmentError:
...        pass

>>> brf = BinaryRecordFile(fileA, S.size)
>>> for text in ("Alpha", "Bravo", "Charlie", "Delta",
...        "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet",
...        "Kilo", "Lima", "Mike", "November", "Oscar", "Papa",
...        "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor",
...        "Whisky", "X-Ray", "Yankee", "Zulu"):
...    brf.append(S.pack(text.encode("utf8"))) 
>>> assert len(brf) == 26
>>> brf.append(S.pack(b"Extra at the end"))
>>> assert len(brf) == 27
>>> shutil.copy(fileA, fileB)
>>> del brf[12]
>>> assert len(brf) == 26
>>> brf.close()

>>> if ((os.path.getsize(fileA) + S.size) !=
...        os.path.getsize(fileB)):
...    print("FAIL#1: expected file sizes are wrong")
...    sys.exit()

>>> shutil.copy(fileB, fileA)
>>> if os.path.getsize(fileA) != os.path.getsize(fileB):
...    print("FAIL#2: expected file sizes differ")
...    sys.exit()

>>> for name in (fileA, fileB):
...    try:
...        os.remove(name)
...    except EnvironmentError:
...        pass

>>> filename =  os.path.join(tempfile.gettempdir(), "test.dat")
>>> if os.path.exists(filename): os.remove(filename)
>>> S = struct.Struct("<8s")
>>> test = BinaryRecordFile(filename, S.size)
>>> test.append(S.pack(b"Alpha"))
>>> test.append(S.pack(b"Bravo"))
>>> test.append(S.pack(b"Charlie"))
>>> test.append(S.pack(b"Delta"))
>>> test.append(S.pack(b"Echo"))
>>> test.close()
>>> os.path.getsize(filename)
40
>>> test = BinaryRecordFile(filename, S.size)
>>> len(test)
5
>>> for index in range(len(test)):
...     del test[index]
>>> test.close()
>>> os.path.getsize(filename)
0
>>> test = BinaryRecordFile(filename, S.size)
>>> test.append(S.pack(b"Alpha"))
>>> test.append(S.pack(b"Bravo"))
>>> test.append(S.pack(b"Charlie"))
>>> test.append(S.pack(b"Delta"))
>>> test.append(S.pack(b"Echo"))
>>> del test[2]
>>> del test[4]
>>> del test[3]
>>> test.close()
>>> os.path.getsize(filename)
16
>>> test = BinaryRecordFile(filename, S.size)
>>> test.append(S.pack(b"Charlie"))
>>> test.append(S.pack(b"Delta"))
>>> test.append(S.pack(b"Echo"))
>>> del test[3]
>>> del test[2]
>>> del test[0]
>>> test.close()
>>> os.path.getsize(filename)
16
>>> os.remove(filename)
"""

"""
Создайте новую версию более простого модуля BinaryRecordFile,
в котором не используется байт состояния записи. В этой версии
размер записи, устанавливаемый пользователем, должен совпадать
с истинным размером записи. Новые записи должны добавляться
с помощью нового метода append(), который просто перемещает ука>
затель в конец файла и производит вывод записи в файл. Метод
__setitem__() должен позволять замещать только существующие за>
писи – это легко реализовать с помощью метода __seek_to_index().
Из-за отсутствия байта состояния размер метода __getitem__() дол>
жен сократиться до трех строк. Метод __delitem__() придется пол>
ностью переписать, так как он должен будет перемещать все запи>
си, следующие за удаленной, чтобы заполнить освободившийся
промежуток. Сделать это можно с помощью чуть больше половины
десятка строк, но над реализацией придется подумать. Метод unde-
lete() нужно будет полностью убрать, так как теперь операция вос>
становления поддерживаться не будет. Точно так же надо будет уб>
рать методы compact() и inplace_compact(), так как они больше не
нужны.
Чтобы внести описанные изменения, придется добавить не более
20 новых и строк и удалить по крайней мере 60 строк по сравнению
с оригинальным модулем, и это без учета доктестов.
"""

import os
import struct
import tempfile


class BinaryRecordFile:

    def __init__(self, filename, record_size, auto_flush=True):
        """A random access binary file that behaves rather like a list
        with each item a bytes or bytesarray object of record_size.
        """
        self.__record_size = record_size 
        mode = "w+b" if not os.path.exists(filename) else "r+b"
        self.__fh = open(filename, mode)
        self.auto_flush = auto_flush


    @property
    def record_size(self):
        "The size of each item"
        return self.__record_size 


    @property
    def name(self):
        "The name of the file"
        return self.__fh.name


    def flush(self):
        """Flush writes to disk
        Done automatically if auto_flush is True
        """
        self.__fh.flush()


    def close(self):
        self.__fh.close()


    def append(self, record):
        """
        Adds a new entry to the end of the file.
        """
        assert isinstance(record, (bytes, bytearray)), \
               "binary data required"
        assert len(record) == self.record_size, (
            "record must be exactly {0} bytes".format(
            self.record_size))
        self.__fh.seek(0, os.SEEK_END)
        self.__fh.write(record)
        if self.auto_flush:
            self.__fh.flush()


    def __setitem__(self, index, record):
        """Sets the item at position index to be the given record

        The index position cannot be outside the current end of the file.
        """
        assert isinstance(record, (bytes, bytearray)), \
               "binary data required"
        assert len(record) == self.record_size, (
            "record must be exactly {0} bytes".format(
            self.record_size))
        self.__seek_to_index(index)
        self.__fh.write(record)
        if self.auto_flush:
            self.__fh.flush()


    def __getitem__(self, index):
        """Returns the item at the given index position

        If there is no item at the given position, raises an
        IndexError exception.
        """
        self.__seek_to_index(index)
        return self.__fh.read(self.record_size)
        

    def __seek_to_index(self, index):
        if self.auto_flush:
            self.__fh.flush()
        self.__fh.seek(0, os.SEEK_END)
        end = self.__fh.tell()
        offset = index * self.__record_size
        if offset >= end:
            raise IndexError("no record at index position {0}".format(
                             index))
        self.__fh.seek(offset)


    def __delitem__(self, index):
        """Deletes the item at the given index position.
        """
        length = len(self)
        while index < length -1: 
            self[index] = self[index + 1] 
            index += 1
        self.__fh.truncate((length - 1) * self.__record_size)
        self.__fh.flush()


    def __len__(self):
        """The number number of record positions.

        This is the maximum number of records there could be at
        present. 
        """
        if self.auto_flush:
            self.__fh.flush()
        self.__fh.seek(0, os.SEEK_END)
        end = self.__fh.tell()
        return end // self.__record_size


if __name__ == "__main__":
    import doctest
    doctest.testmod()