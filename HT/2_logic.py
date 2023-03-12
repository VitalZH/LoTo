import random

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
        a = [2, 3]  # карта Лото здесь замеить на код из модуля Blank_karta.py
        print(f' карта Лото: {a}')
        b = [random.randint(1, 2) for i in range(4)]
        print(b)
        for i in b:
            print('выбран боченок:', i)
            y_or_n = def_y_n(
                input(f'число {i} присутствует в карте? нажмите (y/n):'))  # проверка на правильный ввод 'y' или 'n'

            if y_or_n == 'y' and i in a:
                print('старт функции зачеркнуть i + переход к след i')
            elif y_or_n == 'n' and i not in a:
                print('iпереход к след i')
            else:
                print('вы проиграли')
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
