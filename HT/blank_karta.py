import random

# декоратор для вывода карточки с разделителями
def decor_karta(f):
    def wrapper(*args, **kwargs):
        print(f'-------sep---------')
        result = f(*args, **kwargs)
        print(f'-------sep---------')
        return result
    return wrapper

# функция замена значений в пустой карточке на значения из рандомного списка - split_list_15
@decor_karta
def blank_karta():
    list_15 = random.sample(range(0, 91), 15) # возвращ 15 рандом знач для карты
    split_list_15 = [sorted(list_15[:5]), sorted(list_15[5:10]), sorted(list_15[10:])] #с разделение по трем спискам
    blank_karta = [[' ' for j in range(9)] for i in range(3)] #создаем пустую карту лото
    for i in range(3):
        ind_in_lin = sorted(random.sample(range(0, 9), 5)) # определяем заполняемые позиции в пустой карточке
        print(f' номера позиций для заполнения карточки {ind_in_lin}')
        for j, val in enumerate(ind_in_lin):
            blank_karta[i][val] = split_list_15[i][j] # заполняем строки с 1 по 3 пустой карты лото
        print(' '.join(str(j) for j in blank_karta[i]))
    return blank_karta


if __name__ == '__main__':
#  вывод результата работы функции def blank_karta
    a = blank_karta()
    print('Chat GPT:', a)
    for i in a:
        print(' '.join(str(j) for j in i))
