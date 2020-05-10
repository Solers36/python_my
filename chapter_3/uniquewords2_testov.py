"""Модифицируйте программу uniquewords2.py так, чтобы она выводила
слова не в алфавитном порядке, а по частоте встречаемости.
Вам потребуется обойти элементы словаря и создать маленькую
функцию из двух строк, которая будет извлекать значение каждого
элемента, и передать ее в виде аргумента key функции sorted(). Кроме
того, потребуется соответствующим образом изменить инструкцию
print(). Это несложно, но тут есть некоторый подвох. Решение
приводится в файле uniquewords_ans.py."""

import collections
import string
import sys


def sorting_by_quantity(words_items):
    return words_items[1]


words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    with open(filename) as file:
        for line in file:
            for word in line.lower().split():
                word = word.strip(strip)
                if len(word) > 2:
                    words[word] += 1
for word, value in sorted(words.items(), key=sorting_by_quantity, reverse=True):
    print("'{0}' occurs {1} times".format(word, value))
