import random
# функция-1 возвращ 15 рандом знач с разделениием по трем спискам
def split_list_15():
    list_15 = random.sample(range(0, 91), 15)
    split_list_15 = [sorted(list_15[:5]), sorted(list_15[5:10]), sorted(list_15[10:])]
    return split_list_15


# декоратор для вывода карточки с разделителями
def decor_karta(f):
    def wrapper(*args, **kwargs):
        print(f'-------sep---------')
        result = f(*args, **kwargs)
        print(f'-------sep---------')
        return result

    return wrapper


# функция-2 замена значений в пустой карточке на значения из рандомного списка функц 1
@decor_karta
def blank_karta(split_list_15):
    blank_karta = [[' ' for j in range(9)] for i in range(3)]
    for i in range(3):
        ind_in_lin = sorted(random.sample(range(0, 9), 5))
        for j, val in enumerate(ind_in_lin):
            blank_karta[i][val] = split_list_15[i][j]
        print(' '.join(str(j) for j in blank_karta[i]))
    return blank_karta


# (не включать) вывод карточки в формате строки для вывода на экран

a = blank_karta(split_list_15())
print('Chat GPT:', a)
for i in a:
    print(' '.join(str(j) for j in i))