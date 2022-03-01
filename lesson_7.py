# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
# 	Если цифра есть на карточке - она зачеркивается и игра продолжается.
# 	Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
# 	Если цифра есть на карточке - игрок проигрывает и игра завершается.
# 	Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 11     - 14    87
#       16 49    55 77    88
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html

import random


class Card:
    def __init__(self, name_player):
        self.name_player = name_player
        self.card = [
            [],
            [],
            []]
        self.numbers_stroked = 0
        NEED_SPACES = 4
        NEED_NUMBERS = 5
        self.numbers = random.sample(range(1, 91), 15)

        for line in self.card:
            for i in range(NEED_SPACES):
                line.append(' ')
            for i in range(NEED_NUMBERS):
                line.append(self.numbers.pop())

        # Данная функция возвращает либо число, которое непосредственно на линии, либо случайное, чтобы случайно расставить пробелы.
        def check_sort_item(item):
            if isinstance(item, int):
                return item
            return random.randint(1, 90)

        for index, line in enumerate(self.card):
            self.card[index] = sorted(line, key=check_sort_item)

    def has_number(self, number):
        for line in self.card:
            if number in line:
                return True
        return False

    def stroke_number(self, number):
        for index, line in enumerate(self.card):
            for num_idx, num_card in enumerate(line):
                if number == num_card:
                    self.card[index][num_idx] = '-'
                    self.numbers_stroked += 1
                    if self.numbers_stroked >= 15:
                        raise Exception(f'{self.name_player} победил!')
                    return True
        return False

    def __str__(self):
        header = f'\n{self.name_player}:\n***************************\n'
        body = '\n'
        for line in self.card:
            for i in line:
                body += str(i).ljust(3)
            body += '\n'
        return header + body


class Game:
    def __init__(self, player, comp):
        self._player = player
        self._comp = comp
        self._number_in_bag = [i for i in range(1, 91)]
        random.shuffle(self._number_in_bag)

    def get_number(self):
        return self._number_in_bag.pop()

    def start(self):
        for i in range(90):
            print(self._player, self._comp)
            number = self.get_number()
            if len(self._number_in_bag) >= 1:
                print(f'Новый бочонок {number}, осталось {len(self._number_in_bag)}.')
                user_choice = input('Хотите зачеркнуть цифру? y/n\n')
                user_choice = user_choice.lower()
                while len(user_choice) == 0 or user_choice not in 'yn':
                    print('Вы ввели некорректный ответ')
                    print(self._player, self._comp)
                    print(f'Новый бочонок {number}, осталось {len(self._number_in_bag)}.')
                    user_choice = input('Хотите зачеркнуть цифру? y/n\n')
                    user_choice = user_choice.lower()
                if user_choice == 'y':
                    if not self._player.stroke_number(number):
                        print('Игрок проиграл')
                        break
                elif self._player.has_number(number):
                    print('Игрок проиграл')
                    break
                if self._comp.has_number(number):
                    self._comp.stroke_number(number)
            else:
                print('Бочонки закончились!\n')
                ask_game = input('Начать игру заново? y/n')
                if ask_game == 'y':
                    user = Card('Игрок')
                    computer = Card('Компьютер')
                    game = Game(user, computer)
                    game.start()
                else:
                    print('До свидания!')
                    break

user = Card('Игрок')
computer = Card('Компьютер')
game = Game(user, computer)
game.start()
