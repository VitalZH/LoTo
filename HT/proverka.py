import random

class Lotto:
    def __init__(self):
        self.karta = self.def_karta()
        self.rand_90 = self.def_rand_90()

    # функция формирования списка случ знач для карты лотто 15 из 90 значений
    def def_karta(self):
        znach = random.sample(range(1, 91), 15)
        return znach

    # формируем список случайных значений
    def def_rand_90(self):
        rand_90 = random.sample(range(1, 91), 90)
        return rand_90

    # функция замены значений на "Х" при совпадении с рандомом боченков_для компа
    def do_replace_c(self, karta, i):
        print(f'выбран боченок:{self.rand_90[i]} (ход № {i + 1})')
        for j in range(len(karta)):
            if karta[j] == self.rand_90[i]: # проверка на совпадение значений в карте и боченка, замена на "Х"
                karta[j] = 'X'
        #num_x = sum(1 for j in karta if j == 'X') # подсчет количества Х в карте
        #print(karta, num_x)
        return karta

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
        self.num_x1 = sum(1 for j in self.karta_1 if j == 'X')
        self.karta_2 = self.def_karta()
        self.num_x2 = sum(1 for j in self.karta_2 if j == 'X')
        y_or_n = self.def_y_n(input(f'число {self.rand_90[i]} присутствует в карте Игрока? нажмите (y/n):'))

    def play_ci(self):
        print('rand_90', self.rand_90)
        for i in range(len(self.rand_90)):
            self.karta_1 = self.do_replace_c(self.karta_1, i)# вызываем функцию замены значений для карты 1(комп)

            # ниже логический блок проверки ответов иголка y\n и проверка нажатия клавиш
            print('Карат2-Игрок', self.karta_2, self.num_x2)
            #y_or_n = self.def_y_n(input(f'число {self.rand_90[i]} присутствует в карте Игрока? нажмите (y/n):'))
            if y_or_n == 'y' and self.rand_90[i] in self.karta_2:
                print(' Правильно! боченок зачеркнут')
                # зачеркнуть значение в карте Игрока (кара 2)
                self.karta_2 = self.do_replace_c(self.karta_2, i)
                if self.num_x1 == 15 or self.num_x2 == 15:
                    print(f'Выиграл Игрок # {1 if self.num_x1 == 15 else 2}')
                    break

            elif y_or_n == 'n' and self.rand_90[i] not in self.karta_2: # проверка на отсутствие боченка в карте
                print('Правильно! следующий ход')

            else:  # обработка двух случаев "ошибки игрока" - "у", но бочки нет, "н", но боченок есть
                print('вы проиграли, завершение программы')
                break

while True:
    print('2. Игра Лотто Компьютер - Игрок')
    print('4. Выйте из игры')

    choice = input('Выберите пункт меню:')
    if choice == '2':
        print('Вы выбрали игру Лотто Компьютер - Игрок')
        C_to_i().play_ci()

    elif choice == '4':
        print('Вы вышли из игры')
        # ___
        break
    else:
        print('Вы выбрали неверный пункт меню')
