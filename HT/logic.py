import random

# функция проверки правильности ввода "y" or "n" Игрока - обработка исключений
def def_y_n(y_or_n):
    while True:
        if y_or_n == 'y' or y_or_n == 'n':
            return y_or_n
        else:
            print('def:_Please enter y or n')
            y_or_n = def_y_n(input('def:_Please enter y or n: '))

# функция формирования списка для карты лотто 15 из 90 значений
def def_karta():
    a = random.sample(range(1,91), 15)
    return a

 # функция определения индексов в пустой карте для заполнения знач из def_karta
def def_poz():
    e = [sorted(random.sample(range(0, 9), 5)) for i in range(3)]
    return e

# функция возвращает 90 случайных значений для последовательного выбора игроками
def def_rand_90():
    def_rand_90 = random.sample(range(1,91), 90)
    return def_rand_90

# запуск функции зачеркивания значения в карте Игрока "a"
def zamena_val(val, lst):
    a1 = ['X' if x == val else x for x in lst]
    return a1
'''
            if num in a_igrok:
                idx = a_igrok.index(num)
                a_igrok[idx] = " "
'''

# функция проверки кто выиграл
def def_win(list):
    c = 0
    for x in list:
        if x == 'X':
            c += 1
    # или код выше заменить на код: c = sum(1 for x in list if x == 'X')
    if c == len(list):
        return True
    else:
        return False

# функция вывода красивой ЛОТО карточки с пробелами
def def_karta_stroki(list, poz):
    blank_karta = [[' ' for j in range(9)] for i in range(3)] #создаем пустую карту лото
    #split_list = [sorted(list[:5]), sorted(list[5:10]), sorted(list[10:])] #разделение знач карты на три списка
    split_list = [sorted(map(str, list[:5])), sorted(map(str, list[5:10])), sorted(map(str, list[10:]))]

    for i in range(3):
        for j, val in enumerate(poz[i]):
            blank_karta[i][val] = split_list[i][j] # заполняем строки с 1 по 3 пустой карты лото
    return '\n'.join([' '.join(str(j) for j in row) for row in blank_karta])

    #split_list = [sorted(map(str, list[:5])), sorted(map(str, list[5:10])), sorted(map(str, list[10:]))]

# основное тело программы: выбор соперника и стар логики
while True:
    print('1. Игра Лотто Челове-Компьютер')
    print('2. Игра Лотто Человек - Человек')
    print('3. Выйте из игры')

    choice = input('Выберите пункт меню:')
    if choice == '1':
        print('Вы выбрали игру Лотто Челове-Компьютер')
        a_igrok = def_karta()  # Функция - список занчений для карты игрока
        a_igrok_poz = def_poz()  # Функция - список № позиций для карты игрока

        a_comp = def_karta()  # Функция - список занчений для карты компа
        a_comp_poz = def_poz()  # Функция - список № позиций для карты компа

        b = def_rand_90() # функция - список 90 случ знач для послед вывода
        print(f'список СЛУЧАЙНЫХ чиcел: {b}')


        # логический блок - рандом боченка и проверки ответов Игрока и Компа
        for i, val in enumerate(b):
            print(f'выбран боченок:{val} (ход № {i + 1})')

            # функция зачеркивания ответов в карточке компа
            a_comp = zamena_val(val, a_comp)
            if def_win(a_comp) == True: # проверка победы компа
                print('Победил Компьютер!')
                break

            print(f'карта компа: \n {def_karta_stroki(a_comp, a_comp_poz)}')
            print(f'карта игрока: \n {def_karta_stroki(a_igrok, a_igrok_poz)}')

            # функция проверки на правильный ввод 'y' или 'n' Игрока
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
