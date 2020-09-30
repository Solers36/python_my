"""
Может ли в этой программе ученик учиться без учителя? Если да, пусть 
научится чему-нибудь сам.

Добавьте в класс Pupil метод, позволяющий ученику случайно "забывать" 
какую-нибудь часть своих знаний.
"""


class Data:
    def __init__(self, *info):
        self.info = list(info)

    def __getitem__(self, i):
        return self.info[i]


class Teacher:
    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)


class Pupil:
    def __init__(self):
        self.knowledge = []

    def take(self, info):
        self.knowledge.append(info)
