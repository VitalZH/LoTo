import random
from blank_karta import blank_karta

# функция проверки правильности ввода "y" or "n" - обработка исключений
def def_y_n(y_or_n):
    while True:
        if y_or_n == 'y' or y_or_n == 'n':
            return y_or_n
        else:
            print('def:_Please enter y or n')
            y_or_n = def_y_n(input('def:_Please enter y or n: '))

# функция формирования списка для карты лотто 15 из 90 значений
def def_karta():
    a = random.sample(range(1,11), 5)
    return a

# функция возвращает 90 случайных значений для последовательного выбора игроками
def def_rand_90():
    def_rand_90 = random.sample(range(1,11), 10)
    return def_rand_90

# запуск функции зачеркивания значения в карте Игрока "a"
def zamena_val(val, list):
    a1 = ['X' if x == val else x for x in list]
    return a1

# функция проверки кто выиграл
def def_win(list):
    c = 0
    for x in list:
        if x == 'X':
            c += 1
    if c == len(list):
        return True
    else:
        return False

# основное тело программы: выбор соперника и стар логики
while True:
    print('1. Игра Лотто Челове-Компьютер')
    print('2. Игра Лотто Человек - Человек')
    print('3. Выйте из игры')

    choice = input('Выберите пункт меню:')
    if choice == '1':
        print('Вы выбрали игру Лотто Челове-Компьютер')
        a_igrok = def_karta()  # Функция - список занчений для карты игрока из модуля Blank_karta.py
        a_comp = def_karta()  # Функция - список занчений для карты компа из модуля Blank_karta.py
        b = def_rand_90() # функция - список 90 случ знач для послед вывода
        print(f'список случ чиc b: {b}')

        # логический блок проверки ответов Игрока и Компа
        for i, val in enumerate(b):
            print(f'выбран боченок:{val} (ход № {i + 1})')

            # функция зачеркивания ответов в карточке компа
            a_comp = zamena_val(val, a_comp)
            if def_win(a_comp) == True: # проверка победы компа
                print('Победил Компьютер!')
                break

            print(f'карта компа: {a_comp}')
            print(f'карта игрока: {a_igrok}')

            # функция проверки на правильный ввод 'y' или 'n'
            y_or_n = def_y_n(input(f'число {val} присутствует в карте Игрока? нажмите (y/n):'))

            if y_or_n == 'y' and val in a_igrok:
                print(' Правильно! функция - зачеркнуть val + переход к след i')
                a_igrok = zamena_val(val, a_igrok) # зачеркнуть значение в карте Игрока
                if def_win(a_igrok) == True:# проверка победы Игрока
                    print('Победил Игрок!')
                    break

            elif y_or_n == 'n' and val not in a_igrok:
                print('Правильно! следующий ход')

            else:
                print('вы проиграли, завершение программы')
                break

    elif choice == '2':
        print('Вы выбрали игру Лотто Человек')
        break
    elif choice == '3':
        print('Вы вышли из игры')
        break
    else:
        print('Вы выбрали неверный пункт меню')
