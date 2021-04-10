"""
Три персонажа.
Первый - рыцарь, умеет наносить удары, есть броня, уровень здоровья
Второй - лучник, умеет стрелять, нет брони
Третий - дракон, умеет наносить удары, нет брони, но много Здоровья

Игра начинается - появляется рыцарь, потом он отправляется в путешествие
по дороге встречает разбойников в лесу - лучников,
после сражений с лучниками - увеличивается сила удара и броня,
в финале встречает дракона и побеждает его.
"""
from random import randint
from time import sleep


class Character:
    # конструктор класса
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        print("->", self.name)
        print("Уровень здоровья:", self.health)
        print("Броня:", self.armor)
        print("Сила удара:", self.power)
        print("Оружие:", self.weapon)
        print()

    def strike(self, enemy):
        # выдает случайное число от 20% силы удара до 110%
        attack = randint(int(self.power * 0.2), int(self.power * 1.1))
        print("-> УДАР!", self.name, "атаковал", enemy.name, "с силой ", attack, "используя", self.weapon)
        print()
        sleep(1)
        attack -= enemy.armor
        if attack > 0:
            enemy.health -= attack
        if enemy.armor > 5:
            enemy.armor -= 5
        if enemy.health <= 0:
            print(enemy.name, "упал...")
        else:
            print(enemy.name, "покачнулся")
            print("Броня уменьшилась до", enemy.armor, "уровень здоровья до", enemy.health)
        print()

    def fight(self, enemy):
        print("Да начнется битва!")
        while self.health > 0 and enemy.health > 0:
            if randint(1, 2) == 1:
                self.strike(enemy)
            else:
                enemy.strike(self)
            sleep(1)
        if self.health <= 0:
            print(self.name, "пал в этом бою")
        if enemy.health <= 0:
            print(enemy.name, "пал в этом бою")
        print()



print("Игра квест начинается...")
print("В далеком государстве жил был рыцарь по имени ")

knight = Character(name="Richard", health=60, armor=20, power=20, weapon="Меч")
knight.print_info()
sleep(3)
print("Однажды он узнал что где то далеко сверепствует дракон ")

dragon = Character(name="Drago", health=100, armor=5, power=30, weapon="Пламя")
dragon.print_info()
print("и отправился на его поиски....")
sleep(3)

print("Ему предстоит пройти сквозь лес полный разбойиков")
n = randint(1, 3)
names = ["РобинГуд", 'Соловей-разбойник', "Петя"]
while n > 0:
    print("на рыцаря напал разбойник!!!")
    robion = Character(name=names[n], health=randint(15, 80), armor=0, power=randint(10, 30), weapon="лук")
    robion.print_info()
    robion.fight(knight)
    if knight.health <= 0:
        break
    print("Рыцарь хорошо провел этот бой, и после востановления здоровья и сил, его навыки выросли")
    knight.armor += randint(5, 15)
    knight.health += randint(15, 30)
    knight.power += randint(1, 5)
    knight.print_info()
    sleep(3)
    n -= 1


if knight.health > 0:
    print("И вот среди лесной чащи логово дракона...")
    knight.fight(dragon)
