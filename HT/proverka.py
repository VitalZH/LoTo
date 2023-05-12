import random

class Lotto:
    def __init__(self):
        self.karta = self.def_karta()
        self.rand_90 = self.def_rand_90()
        self.poz1 = self.def_poz()
        self.poz2 = self.def_poz()

    # функция формирования списка случ знач для карты лотто 15 из 90 значений
    def def_karta(self):
        znach = random.sample(range(1, 91), 15)
        return znach

    # формируем список случайных значений - "боченков" от 1 до 90
    def def_rand_90(self):
        rand_90 = random.sample(range(1, 91), 90)
        return rand_90

    # функция замены значений на "Х" при совпадении с рандомом боченков_для компа
    def do_replace_c(self, karta, i):
        print(f'выбран боченок:{self.rand_90[i]} (ход № {i + 1})')
        for j in range(len(karta)):
            if karta[j] == self.rand_90[i]: # проверка на совпадение значений в карте и боченка, замена на "Х"
                karta[j] = 'X'
        num_x = sum(1 for j in karta if j == 'X') # подсчет количества Х в карте
        #print(karta, num_x)
        return karta, num_x

# ---------------------
    # функция вывода карточки лото на экран
    def def_karta_stroki(self, karta, poz):
        blank_karta = [[' ' for j in range(9)] for i in range(3)]  # создаем пустую карту лото
        split_list = [sorted(map(str, karta[:5])), sorted(map(str, karta[5:10])), sorted(map(str, karta[10:]))]  #разделение знач карты на три списка

        for i in range(3):
            for j, val in enumerate(poz[i]):
                blank_karta[i][val] = split_list[i][j]  # заполняем строки с 1 по 3 пустой карты лото
        return '\n'.join([' '.join(str(j) for j in row) for row in blank_karta])

    # функция определения места(индекса) для значения в пустой карте
    def def_poz(self):
        e = [sorted(random.sample(range(0, 9), 5)) for i in range(3)]
        return e
# ---------------
# класс потомок Lotto для типа игры Комп - Комп
class C_to_c(Lotto):
    def __init__(self):
        super().__init__()
        self.karta_1 = self.def_karta()
        self.num_x1 = self.def_karta()
        self.karta_2 = self.def_karta()
        self.num_x2 = self.def_karta()

# зачеркивание выпавш знач в карте (ссылка на родителя) + проверка кто из компов выиграл
    def play_cc(self):
        #print('rand_90', self.rand_90)
        for i in range(len(self.rand_90)):
            self.karta_1, self.num_x1 = self.do_replace_c(self.karta_1, i) # вызываем функцию замены значений для карты 1
            print('----- комп №1 -----', '\n', self.def_karta_stroki(self.karta_1, self.poz1), '\n', '-'*20) # вывод на экран карты 1
            self.karta_2, self.num_x2 = self.do_replace_c(self.karta_2, i) # вызываем функцию замены значений для карты 2
            print('----- комп №2 -----', '\n',self.def_karta_stroki(self.karta_2, self.poz2),'\n','-'*20) # вывод на экран карты 2
            if self.num_x1 == 15 or self.num_x2 == 15:
                print(f'Выиграл Комп # {1 if self.num_x1 == 15 else 2}')
                break

# класс потомок Lotto для типа игры Комп - Игрок
class C_to_i(Lotto):

    #функция проверки правильности ввода "y" or "n" Игрока - обработка исключений
    def def_y_n(self, y_or_n):
        while True:
            if y_or_n == 'y' or y_or_n == 'n':
                return y_or_n
            else:
                print('def:_Please enter y or n')
                y_or_n = self.def_y_n(input('def:_Please enter y or n: '))

    def __init__(self):
        super().__init__()
        self.karta_1 = self.def_karta()
        self.num_x1 = self.karta_1.count('X')
        self.karta_2 = self.def_karta()
        self.num_x2 = self.karta_2.count('X')
        y_or_n = self.def_y_n

    def play_ci(self):
        print('rand_90', self.rand_90)
        print('Карта Компа', self.karta_1)
        print('Карта Игрока', self.karta_2)
        for i in range(len(self.rand_90)):
            self.karta_1, self.num_x1 = self.do_replace_c(self.karta_1, i)# вызываем функцию замены значений для карты 1(комп)
            print('------- комп -------', '\n', self.def_karta_stroki(self.karta_1, self.poz1), '\n', '-'*20)

            # ниже логический блок проверки ответов иголка y\n и проверка нажатия клавиш
            y_or_n = self.def_y_n(input(f'число {self.rand_90[i]} присутствует в карте Игрока? нажмите (y/n):'))
            if y_or_n == 'y' and self.rand_90[i] in self.karta_2:
                # зачеркнуть значение в карте Игрока (кара 2)
                self.karta_2, self.num_x2 = self.do_replace_c(self.karta_2, i)
                print('------- игрок -------', '\n', self.def_karta_stroki(self.karta_2, self.poz2), '\n', '-'*20)
                if self.num_x1 == 15 or self.num_x2 == 15:
                    print(f'Выиграл Игрок # {1 if self.num_x1 == 15 else 2}')
                    break

            elif y_or_n == 'n' and self.rand_90[i] not in self.karta_2: # проверка на отсутствие боченка в карте
                self.karta_2, self.num_x2 = self.do_replace_c(self.karta_2, i)
                print('------- игрок -------', '\n', self.def_karta_stroki(self.karta_2, self.poz2), '\n', '-'*20)

            else:  # обработка двух случаев "ошибки игрока" - "у", но бочки нет, "н", но боченок есть
                print('---вы проиграли, завершение программы---')
                break

while True:
    print('2. Игра Лотто Компьютер - Игрок')
    print('3. Игра Лотто Компьютер - Компьютер')
    print('4. Выйте из игры')

    choice = input('Выберите пункт меню:')
    if choice == '2':
        print('Вы выбрали игру Лотто Компьютер - Игрок')
        C_to_i().play_ci()

    if choice == '3':
        print('Вы выбрали игру Лотто Компьютер - Компьютер')
        C_to_c().play_cc()

    elif choice == '4':
        print('Вы вышли из игры')
        # ___
        break
    else:
        print('Вы выбрали неверный пункт меню')
