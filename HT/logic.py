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

# функция возвращает 90 случайных значений для последовательного выбора игроками
def def_rand_90():
    def_rand_90 = [random.randint(1, 90) for i in range(10)]
    return def_rand_90

# запуск функции зачеркивания значения в карте Игрока "a"
def zamena_val(val):
    a = [['X' if x == val else x for x in sublist] for sublist in a]



# основное тело программы: выбор соперника и стар логики
while True:
    print('1. Игра Лотто Челове-Компьютер')
    print('2. Игра Лотто Человек - Человек')
    print('3. Выйте из игры')

    choice = input('Выберите пункт меню:')
    if choice == '1':
        print('Вы выбрали игру Лотто Челове-Компьютер')

        print('Карта игрока')
        a = blank_karta()  # Функция - список занчений для карты игрока из модуля Blank_karta.py
        print('Карта компьютера')
        a1 = blank_karta()  # Функция - список занчений для карты компа из модуля Blank_karta.py
        # функция - список 90 случ знач для послед вывода
        b = def_rand_90()
        print(b)

        # логический блок проверки ответов Игрока
        for i, val in enumerate(b):
            print(f'выбран боченок:{val} (ход № {i+1})')
            # функция проверки на правильный ввод 'y' или 'n'
            print(a)
            y_or_n = def_y_n(input(f'число {val} присутствует в карте Игрока? нажмите (y/n):'))

            if y_or_n == 'y':
                a = [zamena_val(val) for sublist in a if val in sublist and y_or_n == 'y']# запуск функции зачеркивания значения в карте
                print(' Правильно! функция - зачеркнуть val + переход к след i')

                print(f'[a]: {a}')
            elif y_or_n == 'n' and val not in a:
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
