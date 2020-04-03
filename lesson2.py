# task1
my_list = [11, 1.1, None, 'None2', False, 'tree', 563, ('d', 'r', 7), [4, 0, True]]
for i in my_list:
    print(f"Type of {i} is ", type(i))

# task2
my_list = list()
n = int(input('Введите количество элементов списка: '))
print('Введите {} элементов списка'.format(n))
for i in range(n):
    my_list.append(input())
print('Ваш список: ', my_list)
for i in range(int(n/2)):
    v1 = my_list[2*i]
    my_list[2*i] = my_list[2*i + 1]
    my_list[2 * i + 1] = v1
print('Мой список: ', my_list)

# task3
# через список
season_list = ['зима', 'весна', 'лето', 'осень']
n = int(input('Введите номер месяца: '))
print(f"Это {season_list[(n%12)//3]}!")

# через словарь
season_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
print('Какой номер у Вашего любимого месяца?')
n = int(input())
print(f"Да это же {season_dict.get((n%12)//3 + 1)}!")

# task4
str1 = input('Введите строку: ')
for i, w in enumerate((str1.split()), 1):
    print(i, w[:10])

# task5
my_list = [7, 5, 3, 3, 2]
print('Исходный рейтинг: ', my_list)
n = int(input('Введите новый элемент: '))
i = my_list.__len__() - 1
while n > my_list[i] and i >= 0:
    i -= 1
my_list.insert(i + 1, n)
print('Новый рейтинг: ', my_list)

# task6
goods = list()
n = int(input('Количество товаров в списке: '))
for i in range(n):
    print(f"Товар {i + 1}")
    name = input('Название: ')
    price = float(input('цена: '))
    num = int(input('количество: '))
    units = input('единицы измерения: ')
    goods.append((i + 1, {'название': name, 'цена': price, 'количество': num, 'ед': units}))
print('\nДанные по товарам: ')
for i in range(n):
    print(goods[i])
good_dict = dict()
for j in goods[0][1].keys():
    s = set()
    for i in range(n):
        s.add(goods[i][1].get(j))
    good_dict.update({j: list(s)})
print('\nАналитика по товарам: ')
print(good_dict)
