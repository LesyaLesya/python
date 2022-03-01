# EASY

# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


print('EASY. Задания 1 и 2')
print('\n')


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
        self._start()

    def _start(self):
        print(f'{self.name} with speed {self.speed} km/h, color {self.color} and police status {self.is_police}\n')

    def get_speed(self):
        return self.speed

    def get_color(self):
        return self.color

    def get_name(self):
        return self.name

    def get_is_police(self):
        return self.is_police

    def go(self):
        print(f'Car {self.name} goes...')

    def stop(self):
        print(f'Car {self.name} stopped...')

    def turn(self, direction):
        self.direction = direction
        print(f'Car {self.name} turns to the {self.direction}')


class TownCar(Car):
    def for_use(self):
        print('Town car is for country trip')

    def rough_road(self):
        print('Turn on the rough road mode')


class SportCar(Car):
    def for_use(self):
        print('Sport car is for race')

    def turbo(self):
        print('Press turbo speed button')


class WorkCar(Car):
    def for_use(self):
        print('Work car is for business trip')

    def conditioner(self):
        print('Turn on a conditioner')


class PoliceCar(Car):
    def for_use(self):
        print('Police car is for catching criminals')

    def siren(self):
        print('Siren squeals....')


car1 = TownCar(130, 'green', 'Toyota Hillux', False)
car2 = SportCar(350, 'red', 'Ferrary F50', False)
car3 = WorkCar(180, 'black', 'Audi A5', False)
car4 = PoliceCar(200, 'white', 'Ford Crown Victoria', True)

car1.go()
car1.stop()
car1.turn('left')
car1.for_use()
car1.rough_road()
print('\n')

car2.go()
car2.stop()
car2.turn('right')
car2.for_use()
car2.turbo()
print('\n')

car3.go()
car3.stop()
car3.turn('right')
car3.for_use()
car3.conditioner()
print('\n')

car4.go()
car4.stop()
car4.turn('left')
car4.for_use()
car4.siren()

# NORMAL

# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

print('\n')
print('NORMAL. Заданиe 1')
print('\n')


class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    # Функция для подсчета урона
    def _calculate_damage(self, armor):
        return self.damage // armor

    # Функция атаки
    def attack(self, who_defend):
        damage = self._calculate_damage(who_defend.armor)
        who_defend.health -= damage
        print(
            f'{self.name} нанес {who_defend.name} урона {damage}, у противника осталось {who_defend.health} жизней.')


class Player(Person):
    pass


class Enemy(Person):
    pass


class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_game(self):
        last_attacker = self.player
        while self.player.health > 0 and self.enemy.health > 0:
            if last_attacker == self.player:
                self.enemy.attack(self.player)
                last_attacker = self.enemy
            else:
                self.player.attack(self.enemy)
                last_attacker = self.player

        if self.player.health > 0:
            print('Игрок победил!')
        else:
            print('Враг победил!')


player = Player('Alena', 80, 10, 7)
enemy = Enemy('Computer', 60, 20, 3)
game = Game(player, enemy)

game.start_game()

# HARD

# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

print('\n')
print('HARD. Задания 1 и 2')
print('\n')


class Toy:
    def __init__(self, name_toy, color_toy, type_toy):
        self.name_toy = name_toy
        self.color_toy = color_toy
        self.type_toy = type_toy

    def _start_prod(self):
        print('Начало производства')

    def _buy_materials(self):
        print('Закупка сырья для игрушки')

    def _sewing_toy(self):
        print('Пошив игрушки')

    def _paint_toy(self):
        print('Покраска игрушки')

    def create_toy(self):
        self._start_prod()
        self._buy_materials()
        self._sewing_toy()
        self._paint_toy()

        if self.type_toy == 'животное':
            return AnimalToy.ready_toy(self)
        elif self.type_toy == 'персонаж мульфильма':
            return CartoonToy.ready_toy(self)
        else:
            print('Производство провалилось')


class AnimalToy(Toy):
    def ready_toy(self):
        print(f'Готова игрушка-зверюшка {self.name_toy}, цвет - {self.color_toy} тип - {self.type_toy}\n')


class CartoonToy(Toy):
    def ready_toy(self):
        print(f'Готова игрушка сказочного персонажа {self.name_toy}, цвет - {self.color_toy} тип - {self.type_toy}\n')


toy1 = Toy('Крокодил Гена', 'зеленый', 'персонаж мульфильма')
toy2 = Toy('Кот Вася', 'белый', 'животное')
toy3 = Toy('Чудо-Юдо', 'фиолетоый', 'неведома зверушка')
toy1.create_toy()
toy2.create_toy()
toy3.create_toy()