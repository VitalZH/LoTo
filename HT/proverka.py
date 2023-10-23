import random

class Lotto:
    def __init__(self, karta, rand_90, poz1, poz2):
        self.karta = karta
        self.rand_90 = rand_90
        self.poz1 = poz1
        self.poz2 = poz2

    def def_karta(self):
        znach = random.sample(range(1, 91), 15)
        return znach

    def def_rand_90(self):
        rand_90 = random.sample(range(1, 91), 90)
        return rand_90

    def do_replace_c(self, karta, i):
        print(f'выбран боченок:{self.rand_90[i]} (ход № {i + 1})')
        for j in range(len(karta)):
            if karta[j] == self.rand_90[i]:
                karta[j] = 'X'
        num_x = sum(1 for j in karta if j == 'X')
        return karta, num_x

    def def_karta_stroki(self, karta, poz):
        blank_karta = [[' ' for j in range(9)] for i in range(3)]
        split_list = [sorted(map(str, karta[:5])), sorted(map(str, karta[5:10])), sorted(map(str, karta[10:]))]

        for i in range(3):
            for j, val in enumerate(poz[i]):
                blank_karta[i][val] = split_list[i][j]
        return '\n'.join([' '.join(str(j) for j in row) for row in blank_karta])

    def def_poz(self):
        e = [sorted(random.sample(range(0, 9), 5)) for i in range(3)]
        return e

    def __str__(self):
        return self.def_karta_stroki(self.karta, self.poz1)

class C_to_c(Lotto):
    def __init__(self):
        karta = self.def_karta()
        rand_90 = self.def_rand_90()
        poz1 = self.def_poz()
        poz2 = self.def_poz()
        Lotto.__init__(self, karta, rand_90, poz1, poz2)
        self.karta_1 = self.def_karta()
        self.num_x1 = self.karta_1.count('X')
        self.karta_2 = self.def_karta()
        self.num_x2 = self.karta_2.count('X')

    def play_cc(self):
        for i in range(len(self.rand_90)):
            self.karta_1, self.num_x1 = self.do_replace_c(self.karta_1, i)
            self.karta_2, self.num_x2 = self.do_replace_c(self.karta_2, i)
            if self.num_x1 == 15 or self.num_x2 == 15:
                return f'Выиграл Комп # {1 if self.num_x1 == 15 else 2}'
        return 'Игра закончена'

    def __str__(self):
        return f'Карта Компьютера #1:\n{self.def_karta_stroki(self.karta_1, self.poz1)}\n\nКарта Компьютера #2:\n{self.def_karta_stroki(self.karta_2, self.poz2)}'

class C_to_i(Lotto):
    def def_y_n(self, y_or_n):
        while True:
            if y_or_n == 'y' or y_or_n == 'n':
                return y_or_n
            else:
                print('Пожалуйста, введите "y" или "n".')
                y_or_n = self.def_y_n(input('Пожалуйста, введите "y" или "n: '))

    def __init__(self):
        karta = self.def_karta()
        rand_90 = self.def_rand_90()
        poz1 = self.def_poz()
        poz2 = self.def_poz()
        Lotto.__init__(self, karta, rand_90, poz1, poz2)
        self.karta_1 = self.def_karta()
        self.num_x1 = self.karta_1.count('X')
        self.karta_2 = self.def_karta()
        self.num_x2 = self.karta_2.count('X')
        self.y_or_n = self.def_y_n

    def play_ci(self):
        for i in range(len(self.rand_90)):
            self.karta_1, self.num_x1 = self.do_replace_c(self.karta_1, i)
            y_or_n = self.def_y_n(input(f'Число {self.rand_90[i]} присутствует в вашей карте? Нажмите (y/n): '))
            if y_or_n == 'y' and self.rand_90[i] in self.karta_2:
                self.karta_2, self.num_x2 = self.do_replace_c(self.karta_2, i)
                if self.num_x1 == 15 or self.num_x2 == 15:
                    return f'Выиграл Игрок # {1 if self.num_x1 == 15 else 2}'
            elif y_or_n == 'n' and self.rand_90[i] not in self.karta_2:
                self.karta_2, self.num_x2 = self.do_replace_c(self.karta_2, i)
            else:
                return 'Вы проиграли, завершение программы'

    def __str__(self):
        return f'Ваша карта:\n{self.def_karta_stroki(self.karta_2, self.poz2)}'

while True:
    print('2. Игра Лотто Компьютер - Игрок')
    print('3. Игра Лотто Компьютер - Компьютер')
    print('4. Выйте из игры')

    choice = input('Выберите пункт меню: ')
    if choice == '2':
        print('Вы выбрали игру Лотто Компьютер - Игрок')
        game = C_to_i()
        print(game)
        result = game.play_ci()
        print(result)

    if choice == '3':
        print('Вы выбрали игру Лотто Компьютер - Компьютер')
        game = C_to_c()
        print(game)
        result = game.play_cc()
        print(result)

    elif choice == '4':
        print('Вы вышли из игры')
        break
    else:
        print('Вы выбрали неверный пункт меню')
