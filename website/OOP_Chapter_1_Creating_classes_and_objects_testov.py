"""
Напишите программу по следующему описанию. Есть класс "Воин". 
От него создаются два экземпляра-юнита. Каждому устанавливается 
здоровье в 100 очков. В случайном порядке они бьют друг друга. 
Тот, кто бьет, здоровья не теряет. У того, кого бьют, оно 
уменьшается на 20 очков от одного удара. После каждого удара надо 
выводить сообщение, какой юнит атаковал, и сколько у противника 
осталось здоровья. Как только у кого-то заканчивается ресурс здоровья, 
программа завершается сообщением о том, кто одержал победу.
"""

import random


class Warrior:
    __health = 100
    __damage = 20

    def attacks(self, target):
        target.take_demage(self.__damage)
    
    def take_demage(self, demage):
        if self.__health < demage:
            self.__health = 0 
        else:
            self.__health -= demage

    def alive(self):
        return self.__health > 0 
    
    def get_health(self):
        return self.__health
        

         

winner = None
barbarian = Warrior()
mercenary = Warrior()

while barbarian.alive() and mercenary.alive():
    if random.randint(1, 2) == 1:
        barbarian.attacks(mercenary)
        print("Attacked barbarian, the mercenary has {0} health left.".format(mercenary.get_health()))
        winner = "barbarian"
    else:
        mercenary.attacks(barbarian)
        print("Attacked mercenary, the barbarian has {0} health left.".format(barbarian.get_health()))
        winner = "mercenary"

print("The victory was won by {0}.".format(winner))
