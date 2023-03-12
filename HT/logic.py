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

# основное тело программы: выбор соперника и стар логики
while True:
    print('1. Игра Лотто Челове-Компьютер')
    print('2. Игра Лотто Человек - Человек')
    print('3. Выйте из игры')

    choice = input('Выберите пункт меню:')
    if choice == '1':
        print('Вы выбрали игру Лотто Челове-Компьютер')

        # ________Блок логики рандом № боченка и его наличия в карте_________
        print('Карта игрока')
        a = blank_karta()  # Функция - список занчений для карты игрока из модуля Blank_karta.py
        print('Карта компьютера')
        a1 = blank_karta()  # Функция - список занчений для карты компа из модуля Blank_karta.py
        b = [random.randint(1, 2) for i in range(4)]
        print(b)
        for i, val in enumerate(b):
            print(f'выбран боченок:{val} (ход № {i+1})')
            y_or_n = def_y_n(
                input(f'число {val} присутствует в карте Игрока? нажмите (y/n):'))  # проверка на правильный ввод 'y' или 'n'

            if y_or_n == 'y' and val in a:
                print('старт функции зачеркнуть i + переход к след i')
            elif y_or_n == 'n' and val not in a:
                print('iпереход к след i')
            else:
                print('вы проиграли, завершение программы')
                break
        # ________Окончание блока логики_________

    elif choice == '2':
        print('Вы выбрали игру Лотто Человек')
        break
    elif choice == '3':
        print('Вы вышли из игры')
        break
    else:
        print('Вы выбрали неверный пункт меню')
