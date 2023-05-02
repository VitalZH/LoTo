import random

# функция декоратор для разделения вывода красивых карточек

def print_separator(func):
    def wrapper(*args, **kwargs):
        print('-' * 25)
        result = func(*args, **kwargs)
        print('-' * 25)
        return result
    return wrapper

class Lotto:
    def __init__(self):
        self.karta = self.def_karta()
        self.karta_poz = self.def_poz()
        self.karta_stroki = self.def_karta_stroki()

    # функция формирования списка для карты лотто 15 из 90 значений
    def def_karta(self):
        znach = random.sample(range(1, 91), 15)
        return znach

    # функция определения индексов в пустой карте для заполнения знач из def_karta
    def def_poz(self):
        poz = [sorted(random.sample(range(0, 9), 5)) for i in range(3)]
        return poz

    # формирование карточки  ЛОТО с пробелами

    def def_karta_stroki(self):
        blank_karta = [[' ' for j in range(9)] for i in range(3)] #создаем пустую карту лото
        split_list = [sorted(map(str, self.karta[:5])), sorted(map(str, self.karta[5:10])), sorted(map(str, self.karta[10:]))]
        for i in range(3):
            for j, val in enumerate(self.karta_poz[i]):
                blank_karta[i][val] = split_list[i][j] # заполняем строки с 1 по 3 пустой карты лото
        #print('\n'.join([' '.join(str(j) for j in row) for row in blank_karta]))
        return blank_karta


class Class_2:
    def __init__(self, karta_c, karta_i):
        self.karta_c = karta_c
        self.karta_i = karta_i
        self.rand_90 = self.def_rand_90()

    def def_rand_90(self):
        rand_90 = random.sample(range(1, 91), 90)
        return rand_90

    # функция проверки окончания боченков, кто выиграл
    def def_win(self, karta_c):
        c = 0
        for x in self.karta_c:
            if x == 'X':
                c += 1
        # или код выше заменить на код: c = sum(1 for x in list if x == 'X')
        if c == len(karta_c):
            return True
        else:
            return False
# функция земены значеня на "Х" при совпадеиии с рандомом боченков
    def do_replace(self, karta_c, karta_i):
        for i in range(len(self.rand_90)):
            print(f'выбран боченок:{self.rand_90[i]} (ход № {i + 1})')
            self.karta_c = [['X' if j == str(self.rand_90[i]) else j for j in row] for row in self.karta_c]
            c = sum(1 for row in self.karta_c for j in row if j == 'X')
            self.karta_i = [['X' if j == str(self.rand_90[i]) else j for j in row] for row in self.karta_i]
            i = sum(1 for row in self.karta_i for j in row if j == 'X')
            print(f'____карта компа____ \n {self.karta_c}')
            print('c', c)
            print(f'____карта игрока____ \n {self.karta_i}')
            print('i', i)
        return self.karta_c, karta_i


# создаем объект(karta1,2) класса Lotto()
class_obj1 = Lotto()
karta_c = class_obj1.karta_stroki
print('karta1', karta_c)

class_obj2 = Lotto()
karta_i = class_obj2.karta_stroki
print('karta2', karta_i)

class2 = Class_2(karta_c, karta_i)
print('def_rnd', class2.def_rand_90())
print('rand_90', class2.rand_90)
class2.do_replace(karta_c, karta_i)


while True:
    print('1. Игра Лотто Челове-Компьютер')
    print('2. Игра Лотто Человек - Человек')
    print('3. Выйте из игры')

    choice = input('Выберите пункт меню:')
    if choice == '1':
        print('Вы выбрали игру Лотто Челове-Компьютер')
        #___
        break
    elif choice == '2':
        print('Вы выбрали игру Лотто Человек')
        # ___
        break
    elif choice == '3':
        print('Вы вышли из игры')
        # ___
        break
    else:
        print('Вы выбрали неверный пункт меню')


'''
#класс наследник класса lotto
class Comp(Lotto):
    def __init__(self,???):
        super().__init__(???)

    # две функции зачеркивания ответов в карточке компа и проверки на выигрыш
    a_comp = zamena_val(val-'случ бочен', a_comp-'числа в карт')
    if def_win(a_comp) == True:  # проверка победы компа
        print('Победил Компьютер!')
        break

    # запуск функции зачеркивания значения в карте Игрока "a"
    def zamena_val(val-'случ бочен', lst -'a_comp-числа в карт'):
        a1 = ['X' if x == val else x for x in lst]
        return a1

    # функция проверки кто выиграл
    def def_win(list-'число в карте'):
        c = 0
        for x in list:
            if x == 'X':
                c += 1
        # или код выше заменить на код: c = sum(1 for x in list if x == 'X')
        if c == len(list):
            return True
        else:
            return False
'''


