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
    health = 100
    damage = 20

    def attacks(self, other):
        other.health -= self.damage
         

winner = None
barbarian = Warrior()
mercenary = Warrior()

while barbarian.health > 0 and mercenary.health > 0:
    if random.randint(1, 2) == 1:
        barbarian.attacks(mercenary)
        print("Attacked barbarian, the mercenary has {0} health left.".format(mercenary.health))
        winner = "barbarian"
    else:
        mercenary.attacks(barbarian)
        print("Attacked mercenary, the barbarian has {0} health left.".format(barbarian.health))
        winner = "mercenary"

print("The victory was won by {0}.".format(winner))
