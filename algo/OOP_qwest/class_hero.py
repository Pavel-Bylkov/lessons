from time import sleep
from random import randint
class Hero():
   #конструктор класса
   def __init__(self, name, health, armor, power, weapon):
       self.name = name
       self.health = health #число
       self.armor = armor #строка
       self.power = power #число
       self.weapon = weapon #строка
   #печать инфо о персонаже:
   def print_info(self):
       print('->' + self.name)
       print('Уровень здоровья:', self.health)
       print('Класс брони:', self.armor)
       print('Сила удара:', self.power)
       print('Оружие:', self.weapon, '\n')
   #нанести удар по другому персонажу
   def strike(self, enemy):
       attack = randint(self.power-5, self.power+5)
       print('-> УДАР! ' + self.name + ' атакует ' + enemy.name + ' с силой ' 
                + str(attack) + ', используя ' + self.weapon + '\n')
       enemy.armor -= attack
       if enemy.armor < 0:
           enemy.health += enemy.armor
           enemy.armor = 0
       print(enemy.name + ' покачнулся.\nКласс его брони упал до ' 
            + str(enemy.armor) + ', а уровень здоровья до ' + str(enemy.health) + '\n')
   #вступить в поединок
   def fight(self, enemy):
       while self.health and enemy.health > 0:
            if randint(1,2) == 1:
                self.strike(enemy)
                if enemy.health <= 0:
                    print(enemy.name, 'пал в этом нелегком бою!\n')
                    break
            else:
                enemy.strike(self)
                if self.health <= 0:
                    print(self.name, 'пал в этом нелегком бою!\n')
                    break
            sleep(4)
