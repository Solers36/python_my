"""
Разработайте программу по следующему описанию.

В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный номер
 объекта, и свойство, в котором хранится принадлежность команде. У солдат есть метод "иду за героем", 
 который в качестве аргумента принимает объект типа "герой". У героев есть метод увеличения собственного уровня.

В основной ветке программы создается по одному герою для каждой команды. В цикле генерируются 
объекты-солдаты. Их принадлежность команде определяется случайно. Солдаты разных команд добавляются в разные списки.

Измеряется длина списков солдат противоборствующих команд и выводится на экран. У героя, принадлежащего 
команде с более длинным списком, поднимается уровень.

Отправьте одного из солдат первого героя следовать за ним. Выведите на экран идентификационные номера этих двух юнитов.
"""

import random



class Warrior:
    def __init__(self, team, number):
        self.number = number
        self.team = team

class Hero(Warrior):
    def __init__(self, team, number, level=1):
        Warrior.__init__(self, team, number)
        self.level = level

    def increase_level(self):
        self.level += 1

class Soldier(Warrior):
    def going_for_a_hero(self, hero):
        return print("Soldier number {0} followed by hero number {1}.".format(self.number, hero.number))


red_team =[]
red_hero = Hero("red", "red" + str(len(red_team) + 1))
red_team.append(red_hero)

blue_team =[]
blue_hero = Hero("blue", "blue" + str(len(blue_team) + 1))
blue_team.append(blue_hero)

for i in range(11):
    if random.randint(1, 2) == 1:
        soldier = Soldier("red", "red" + str(len(red_team) + 1))
        red_team.append(soldier)
    else:
        soldier = Soldier("blue", "blue" + str(len(blue_team) + 1))
        blue_team.append(soldier)

print("The red team consists of {0} warriors, and the blue team consists of {1} warriors."
      .format(len(red_team), len(blue_team)))

if len(red_team) > len(blue_team):
    red_hero.increase_level()
elif len(red_team) == len(blue_team):
    pass
else:
    blue_hero.increase_level()

red_team[random.randint(1, len(red_team))].going_for_a_hero(red_hero)

