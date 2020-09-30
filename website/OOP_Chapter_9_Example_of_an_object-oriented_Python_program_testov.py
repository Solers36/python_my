"""
Может ли в этой программе ученик учиться без учителя? Если да, пусть 
научится чему-нибудь сам.

Добавьте в класс Pupil метод, позволяющий ученику случайно "забывать" 
какую-нибудь часть своих знаний.
"""


import random


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

    def forgetfulness(self):
        random_list_item = random.randint(0, len(self.knowledge) - 1)
        self.knowledge.pop(random_list_item)


lesson = Data('class', 'object', 'inheritance',
              'polymorphism', 'encapsulation')
marIvanna = Teacher()
vasy = Pupil()
pety = Pupil()
marIvanna.teach(lesson[2], vasy, pety)
marIvanna.teach(lesson[0], pety)
vasy.take(lesson[4])
print(vasy.knowledge)
print(pety.knowledge)

pety.forgetfulness()
print(pety.knowledge)